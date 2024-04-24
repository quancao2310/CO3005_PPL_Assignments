from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List

class Unknown(Type):
    def __str__(self):
        return "Unknown"

class Symbol:
    pass

class VarSymbol(Symbol):
    def __init__(self, name: str, typ: Type):
        self.name = name
        self.typ = typ

class FuncSymbol(Symbol):
    def __init__(self, name: str, typ: Type, param_list: List[VarSymbol] = [], defined = True):
        self.name = name
        self.typ = typ
        self.param_list = param_list
        self.defined = defined

class StaticChecker(BaseVisitor, Utils):
    builtin_env = [
        FuncSymbol("readNumber", NumberType(), []),
        FuncSymbol("readBool", BoolType(), []),
        FuncSymbol("readString", StringType(), []),
        FuncSymbol("writeNumber", VoidType(), [VarSymbol("<arg>", NumberType())]),
        FuncSymbol("writeBool", VoidType(), [VarSymbol("<arg>", BoolType())]),
        FuncSymbol("writeString", VoidType(), [VarSymbol("<arg>", StringType())]),
    ]
    
    def __init__(self, ast: AST):
        self.ast = ast
    
    def check(self):
        return self.ast.accept(self, StaticChecker.builtin_env)
    
    def infer_symbol(self, name: str, typ: Type, env: List[List[Symbol]], symType = Symbol) -> Type:
        for symbol_list in env:
            symbol = self.lookup(
                name,
                filter(lambda symbol: type(symbol) is symType, symbol_list),
                lambda symbol: symbol.name
            )
            if symbol:
                symbol.typ = typ
                return typ
        return Unknown()
    
    def infer_array(self, ast: ArrayLiteral, typ: ArrayType, env: List[List[Symbol]]):
        eleType = typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType)
        
        for expr in ast.value:
            self.infer(expr, eleType, env, TypeMismatchInExpression(ast))
        
        return typ
    
    def infer(self, expr: Expr, typ: Type, env: List[List[Symbol]], error: StaticError):
        if type(expr) is Id:
            self.infer_symbol(expr.name, typ, env, VarSymbol)
        elif type(expr) is CallExpr:
            self.infer_symbol(expr.name.name, typ, env, FuncSymbol)
        elif type(expr) is ArrayLiteral:
            if type(typ) is ArrayType and self.isCompatibleArrayType(expr.accept(self, env), typ):
                self.infer_array(expr, typ, env)
            else:
                raise error if error else StaticError()
        elif type(expr) is ArrayCell:
            self.infer(expr.arr, ArrayType([0 for _ in range(len(expr.idx))], typ), env, error)
        return typ
    
    def isCompatibleArrayType(self, arr_typ1: ArrayType, arr_typ2: ArrayType):
        """
        Check if the first array type is compatible with the second one,
        so that it can be inferred to the latter.
        """
        if len(arr_typ1.size) > len(arr_typ2.size):
            return False
        if type(arr_typ1.eleType) not in [Unknown, type(arr_typ2.eleType)]:
            return False
        return all(arr_typ1.size[i] == arr_typ2.size[i] for i in range(len(arr_typ1.size)))
    
    def isUnknown(self, ast: Type):
        """
        Check if the Type instance is Unknown or has Unknown elements.
        These kinds of Expr may have Unknown Type: Id, CallExpr, ArrayLiteral.
        """
        return (type(ast) is Unknown) or (type(ast) is ArrayType and type(ast.eleType) is Unknown)
    
    def isSameType(self, type1: Type, type2: Type) -> bool:
        """
        Check if two Types are exactly the same.
        """
        if type(type1) is ArrayType or type(type2) is ArrayType:
            if type(type1) is not ArrayType or type(type2) is not ArrayType:
                return False
            if type(type1.eleType) is not type(type2.eleType):
                return False
            if len(type1.size) != len(type2.size):
                return False
            return all(type1.size[i] == type2.size[i] for i in range(len(type1.size)))
        return type(type1) is type(type2)
    
    def visitProgram(self, ast: Program, o: List[FuncSymbol]):
        # o = StaticChecker.builtin_env
        # The global scope will be env[-1]
        env = reduce(lambda prev, curr: curr.accept(self, prev), ast.decl, [o])
        
        checkMain = False
        for symbol in env[-1]:
            if type(symbol) is FuncSymbol:
                if not symbol.defined:
                    raise NoDefinition(symbol.name)
                if symbol.name == "main" and len(symbol.param_list) == 0 and type(symbol.typ) is VoidType:
                    checkMain = True
        
        if not checkMain:
            raise NoEntryPoint()
    
    def visitVarDecl(self, ast: VarDecl, o: List[List[Symbol]]):
        # Check variable redeclaration (same scope)
        var_symbol = self.lookup(
            ast.name.name,
            filter(lambda symbol: type(symbol) is VarSymbol, o[0]),
            lambda symbol: symbol.name
        )
        if var_symbol:
            raise Redeclared(Variable(), ast.name.name)
        
        # Create symbol and add to the environment
        var_symbol = VarSymbol(ast.name.name, ast.varType if ast.varType else Unknown())
        ret_env = [o[0] + [var_symbol]] + o[1:]
        
        # Check/Infer type if initialized
        if ast.varInit:
            try:
                init_t = ast.varInit.accept(self, ret_env)
                var_t = var_symbol.typ
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            
            if type(var_t) is Unknown and self.isUnknown(init_t):
                raise TypeCannotBeInferred(ast)
            
            if type(var_t) is Unknown:
                var_t = var_symbol.typ = init_t
            
            if self.isUnknown(init_t):
                init_t = self.infer(ast.varInit, var_t, ret_env, TypeCannotBeInferred(ast))
            
            if not self.isSameType(init_t, var_t):
                raise TypeMismatchInStatement(ast)
        
        return ret_env
    
    def visitFuncDecl(self, ast: FuncDecl, o: List[List[Symbol]]):
        # Check function redeclaration (in global scope - the only place to declare functions)
        # If function was not defined/implemented yet, just get its symbol
        func_symbol = self.lookup(
            ast.name.name,
            filter(lambda symbol: type(symbol) is FuncSymbol, o[-1]),
            lambda symbol: symbol.name
        )
        if func_symbol:
            error = Redeclared(Function(), ast.name.name)
            if func_symbol.defined or not ast.body or len(func_symbol.param_list) != len(ast.param):
                raise error
            for i in range(len(func_symbol.param_list)):
                if not self.isSameType(func_symbol.param_list[i].typ, ast.param[i].varType):
                    raise error
        
        # If the AST does not have a body (no implementation part),
        # create a symbol and return
        if not ast.body:
            func_symbol = FuncSymbol(
                ast.name.name,
                Unknown(),
                [VarSymbol("<param>", param.varType) for param in ast.param],
                False
            )
            return [o[0] + [func_symbol]] + o[1:]
        
        # Otherwise (AST has a body), process it
        # Create a symbol and add it to the environment if there has not been one
        if not func_symbol:
            func_symbol = FuncSymbol(ast.name.name, Unknown(), [], True)
            ret_env = [o[0] + [func_symbol]] + o[1:]
        else:
            func_symbol.defined = True
            ret_env = o
        
        # Visit parameters
        try:
            local_env = reduce(lambda prev, curr: curr.accept(self, prev), ast.param, [[]] + ret_env) # Add function scope
        except Redeclared as e:
            raise Redeclared(Parameter(), e.name)
        
        # Change the func_symbol's param_list to the processed parameter list
        func_symbol.param_list = local_env[0]
        
        # Visit body
        ast.body.accept(self, [[func_symbol]] + local_env) # Add function environment for return statement
        
        if type(func_symbol.typ) is Unknown:
            func_symbol.typ = VoidType()
        return ret_env
    
    def visitBlock(self, ast: Block, o: List[List[Symbol]]):
        reduce(lambda prev, curr: curr.accept(self, prev), ast.stmt, [[]] + o) # Add block scope
        return o
    
    def visitReturn(self, ast: Return, o: List[List[Symbol]]):
        try:
            expr_t = ast.expr.accept(self, o) if ast.expr else VoidType()
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        
        for symbol_list in o:
            if len(symbol_list) > 0 and type(symbol_list[0]) is FuncSymbol:
                func_symbol = symbol_list[0]
                func_t = func_symbol.typ
                
                if type(func_t) is Unknown and self.isUnknown(expr_t):
                    raise TypeCannotBeInferred(ast)
                
                if type(func_t) is Unknown:
                    func_t = func_symbol.typ = expr_t
                    return o
                
                if self.isUnknown(expr_t):
                    expr_t = self.infer(ast.expr, func_t, o, TypeCannotBeInferred(ast))
                
                if not self.isSameType(expr_t, func_t):
                    raise TypeMismatchInStatement(ast)
                break
        return o
    
    def visitAssign(self, ast: Assign, o: List[List[Symbol]]):
        try:
            right_t = ast.rhs.accept(self, o)
            left_t = ast.lhs.accept(self, o)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        
        if type(left_t) is Unknown and self.isUnknown(right_t):
            raise TypeCannotBeInferred(ast)
        
        if type(left_t) is Unknown:
            left_t = self.infer_symbol(ast.lhs.name, right_t, o, VarSymbol)
        
        if self.isUnknown(right_t):
            right_t = self.infer(ast.rhs, left_t, o, TypeCannotBeInferred(ast))
        
        if not self.isSameType(right_t, left_t):
            raise TypeMismatchInStatement(ast)
        
        return o
    
    def visitIf(self, ast: If, o: List[List[Symbol]]) -> List[List[Symbol]]:
        expr_stmt_list = [(ast.expr, ast.thenStmt)] + ast.elifStmt
        ret_env = o
        
        for expr, stmt in expr_stmt_list:
            # Check/Infer type of the conditional expression
            try:
                expr_t = expr.accept(self, ret_env)
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            
            if self.isUnknown(expr_t):
                expr_t = self.infer(expr, BoolType(), ret_env, TypeCannotBeInferred(ast))
            
            if type(expr_t) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            # Check the corresponding statement
            ret_env = stmt.accept(self, ret_env)
        
        # Check the else-statement if exists
        if ast.elseStmt:
            ret_env = ast.elseStmt.accept(self, ret_env)
        
        return ret_env
    
    def visitFor(self, ast: For, o: List[List[Symbol]]):
        # Check/Infer type of the loop variable
        try:
            id_t = ast.name.accept(self, o)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(id_t) is Unknown:
            id_t = self.infer_symbol(ast.name.name, NumberType(), o, VarSymbol)
        if type(id_t) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        # Check/Infer type of the conditional expression
        try:
            cond_t = ast.condExpr.accept(self, o)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if self.isUnknown(cond_t):
            cond_t = self.infer(ast.condExpr, BoolType(), o, TypeCannotBeInferred(ast))
        if type(cond_t) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        # Check/Infer type of the update expression
        try:
            upd_t = ast.updExpr.accept(self, o)
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if self.isUnknown(upd_t):
            upd_t = self.infer(ast.updExpr, NumberType(), o, TypeCannotBeInferred(ast))
        if type(upd_t) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        # Check the statement
        loop_env = [o[0] + [VarSymbol("<loop>", VoidType())]] + o[1:]
        exit_env = ast.body.accept(self, loop_env) # exit_env: [[..., <loop>, (<var>)?], ...]
        
        if exit_env[0][-1].name != "<loop>":
            return [o[0] + [exit_env[0][-1]]] + o[1:]
        return o
    
    def visitBreak(self, ast: Break, o: List[List[Symbol]]):
        for symbol_list in o:
            if self.lookup("<loop>", symbol_list, lambda symbol: symbol.name):
                return o
        raise MustInLoop(ast)
    
    def visitContinue(self, ast: Continue, o: List[List[Symbol]]):
        for symbol_list in o:
            if self.lookup("<loop>", symbol_list, lambda symbol: symbol.name):
                return o
        raise MustInLoop(ast)
    
    def visitCallStmt(self, ast: CallStmt, o: List[List[Symbol]]):
        func_symbol = self.lookup(
            ast.name.name,
            filter(lambda symbol: type(symbol) is FuncSymbol, o[-1]),
            lambda symbol: symbol.name
        )
        if not func_symbol:
            raise Undeclared(Function(), ast.name.name)
        
        if type(func_symbol.typ) is Unknown:
            func_symbol.typ = VoidType()
        if type(func_symbol.typ) is not VoidType:
            raise TypeMismatchInStatement(ast)
        
        if len(ast.args) != len(func_symbol.param_list):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(ast.args)):
            arg_t = ast.args[i].accept(self, o)
            param_t = func_symbol.param_list[i].typ
            
            if self.isUnknown(arg_t):
                arg_t = self.infer(ast.args[i], param_t, o, TypeCannotBeInferred(ast))
            
            if not self.isSameType(arg_t, param_t):
                raise TypeMismatchInStatement(ast)
        
        return o
    
    def visitBinaryOp(self, ast: BinaryOp, o: List[List[Symbol]]) -> Type:
        if ast.op in ['+', '-', '*', '/', '%', 'and', 'or', '...']:
            # The operators that can be applied to operands of the same type and produce a result of the same type
            if ast.op in ['+', '-', '*', '/', '%']:
                infer_type = NumberType
            elif ast.op in ['and', 'or']:
                infer_type = BoolType
            else:
                infer_type = StringType
            
            # Check/Infer type of left operand
            left_t = ast.left.accept(self, o)
            if self.isUnknown(left_t):
                left_t = self.infer(ast.left, infer_type(), o, TypeCannotBeInferred(ast))
            if type(left_t) is not infer_type:
                raise TypeMismatchInExpression(ast)
            
            # Check/Infer type of right operand
            right_t = ast.right.accept(self, o)
            if self.isUnknown(right_t):
                right_t = self.infer(ast.right, infer_type(), o, TypeCannotBeInferred(ast))
            if type(right_t) is not infer_type:
                raise TypeMismatchInExpression(ast)
            
            return infer_type()
        elif ast.op in ['=', '!=', '<', '>', '<=', '>=', '==']:
            # The (relational) operators that can be applied to operands of the same type and produce a result of BoolType
            if ast.op == '==':
                infer_type = StringType
            else:
                infer_type = NumberType
            
            # Check/Infer type of left operand
            left_t = ast.left.accept(self, o)
            if self.isUnknown(left_t):
                left_t = self.infer(ast.left, infer_type(), o, TypeCannotBeInferred(ast))
            if type(left_t) is not infer_type:
                raise TypeMismatchInExpression(ast)
            
            # Check/Infer type of right operand
            right_t = ast.right.accept(self, o)
            if self.isUnknown(right_t):
                right_t = self.infer(ast.right, infer_type(), o, TypeCannotBeInferred(ast))
            if type(right_t) is not infer_type:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o: List[List[Symbol]]) -> Type:
        if ast.op in ['-', 'not']:
            if ast.op == '-':
                infer_type = NumberType
            else:
                infer_type = BoolType
            
            # Check/Infer type of operand
            expr_t = ast.operand.accept(self, o)
            if self.isUnknown(expr_t):
                expr_t = self.infer(ast.operand, infer_type(), o, TypeCannotBeInferred(ast))
            if type(expr_t) is not infer_type:
                raise TypeMismatchInExpression(ast)
            
            return infer_type()
    
    def visitCallExpr(self, ast: CallExpr, o: List[List[Symbol]]):
        func_symbol = self.lookup(
            ast.name.name,
            filter(lambda symbol: type(symbol) is FuncSymbol, o[-1]),
            lambda symbol: symbol.name
        )
        if not func_symbol:
            raise Undeclared(Function(), ast.name.name)
        
        if type(func_symbol.typ) is VoidType:
            raise TypeMismatchInExpression(ast)
        
        if len(ast.args) != len(func_symbol.param_list):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(ast.args)):
            arg_t = ast.args[i].accept(self, o)
            param_t = func_symbol.param_list[i].typ
            
            if self.isUnknown(arg_t):
                arg_t = self.infer(ast.args[i], param_t, o, TypeCannotBeInferred(ast))
            
            if not self.isSameType(arg_t, param_t):
                raise TypeMismatchInExpression(ast)
        
        return func_symbol.typ
    
    def visitId(self, ast: Id, o: List[List[Symbol]]) -> Type:
        for symbol_list in o:
            symbol = self.lookup(
                ast.name,
                filter(lambda symbol: type(symbol) is VarSymbol, symbol_list),
                lambda symbol: symbol.name
            )
            if symbol:
                return symbol.typ
        raise Undeclared(Identifier(), ast.name)
    
    def visitArrayCell(self, ast: ArrayCell, o: List[List[Symbol]]) -> Type:
        arr_t = ast.arr.accept(self, o)
        
        if type(arr_t) is Unknown:
            # raise TypeCannotBeInferred("")
            return Unknown() # Debatable
        if type(arr_t) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if len(arr_t.size) != len(ast.idx):
            raise TypeMismatchInExpression(ast) # Will not be covered in testcases
        
        for i in range(len(ast.idx)):
            idx_t = ast.idx[i].accept(self, o)
            
            if self.isUnknown(idx_t):
                idx_t = self.infer(ast.idx[i], NumberType(), o, TypeCannotBeInferred(ast))
            
            if type(idx_t) is not NumberType:
                raise TypeMismatchInExpression(ast)
        
        return arr_t.eleType
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o: List[List[Symbol]]):
        length = len(ast.value)
        
        # Find the first known type
        expr_types = [expr.accept(self, o) for expr in ast.value] # List[Type]
        common_t = next(filter(lambda typ: not self.isUnknown(typ), expr_types), None)
        
        # If there is none, it may exist an array of Unknowns. Choose it instead to check size constraint.
        if common_t is None:
            common_t = next(filter(lambda typ: type(typ) is not Unknown, expr_types), None)
            
            if common_t is None:
                return ArrayType([float(length)], Unknown())
        
        # Check/Infer elements' type from the common_t Type
        for i in range(length):
            ele_t = ast.value[i].accept(self, o)
            
            if self.isUnknown(ele_t):
                ele_t = self.infer(ast.value[i], common_t, o, TypeMismatchInExpression(ast))
            
            if not self.isSameType(ele_t, common_t):
                raise TypeMismatchInExpression(ast)
        
        size = [float(length)] + (common_t.size if type(common_t) is ArrayType else [])
        eleType = common_t.eleType if type(common_t) is ArrayType else common_t
        return ArrayType(size, eleType)
    
    def visitNumberLiteral(self, ast: NumberLiteral, o):
        return NumberType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        return BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o):
        return StringType()
    
    def visitArrayType(self, ast: ArrayType, o):
        return ast
    
    def visitNumberType(self, ast: NumberType, o):
        return ast
    
    def visitBoolType(self, ast: BoolType, o):
        return ast
    
    def visitStringType(self, ast: StringType, o):
        return ast
