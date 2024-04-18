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
        FuncSymbol("writeString", VoidType(), [VarSymbol("<arg>", StringType())])
    ]
    
    def __init__(self, ast: AST):
        self.ast = ast
    
    def check(self):
        return self.ast.accept(self, StaticChecker.builtin_env)
    
    def infer(self, name: str, typ: Type, env: List[List[Symbol]], symType = Symbol) -> Type:
        for symbol_list in env:
            for symbol in symbol_list:
                if type(symbol) is symType and symbol.name == name:
                    symbol.typ = typ
                    return typ
        return Unknown()
    
    def inferArray(self, ast: ArrayLiteral, typ: ArrayType, env: List[List[Symbol]], skipIdx: int = -1):
        # typ: Type instance of the array literal: ArrayType(size=[...], eleType=primitive_type)
        eleType = typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType)
        
        for i in range(len(ast.value)):
            if i == skipIdx:
                continue
            
            expr = ast.value[i]
            if type(expr) is Id:
                self.infer(expr.name, eleType, env, VarSymbol)
            if type(expr) is CallExpr:
                self.infer(expr.name.name, eleType, env, FuncSymbol)
            if type(expr) is ArrayLiteral:
                self.inferArray(expr, eleType, env)
    
    def isCompatibleArrayType(self, arr_typ1: ArrayType, arr_typ2: ArrayType) -> bool:
        """
        Check if the first array type is compatible with the second one.
        The latter must be fixed, that is, its eleType is already known.
        Its size should also be greater than the former's.
        """
        if len(arr_typ1.size) > len(arr_typ2.size):
            return self.isCompatibleArrayType(arr_typ2, arr_typ1)
        if type(arr_typ2.eleType) is Unknown:
            return False
        if type(arr_typ1.eleType) not in [Unknown, type(arr_typ2.eleType)]:
            return False
        for i in range(len(arr_typ1.size)):
            if arr_typ1.size[i] != arr_typ2.size[i]:
                return False
        return True
    
    def isUnknown(self, ast: Type):
        """
        Check if the Type instance is related to Unknown
        These kinds of Expr may have Unknown Type: Id, CallExpr, ArrayLiteral
        """
        return (type(ast) is Unknown) or (type(ast) is ArrayType and type(ast.eleType) is Unknown)
    
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
        # ast: name: Id(name: str), varType: Type, modifier: str, varInit: Expr
        # Check variable redeclaration (same scope)
        for symbol in o[0]:
            if type(symbol) is VarSymbol and symbol.name == ast.name.name:
                raise Redeclared(Variable(), ast.name.name)
        
        # Create symbol
        typ = ast.varType if ast.varType is not None else Unknown()
        var_symbol = VarSymbol(ast.name.name, typ)
        
        # Check/Infer type if initialized
        if ast.varInit:
            pass
        
        # Add symbol to the environment
        ret_env = [o[0] + [var_symbol]] + o[1:]
        return ret_env
    
    def visitFuncDecl(self, ast: FuncDecl, o: List[List[Symbol]]):
        # ast: name: Id(name: str), param: List[VarDecl], body: Stmt
        # Check function redeclaration (in global scope - the only place to declare functions)
        # If function was not defined/implemented yet, just get its symbol
        func_symbol = None
        for symbol in o[-1]:
            if type(symbol) is FuncSymbol and symbol.name == ast.name.name:
                if not symbol.defined:
                    func_symbol = symbol
                    break
                raise Redeclared(Function(), ast.name.name)
        
        # If this function's AST doesn't have a body (no implementation part),
        # create a symbol if not have yet and return
        if not ast.body:
            if not func_symbol:
                func_symbol = FuncSymbol(
                    ast.name.name, 
                    Unknown(), 
                    [VarSymbol("<param>", param_decl.varType) for param_decl in ast.param],
                    False
                )
                return [o[0] + [func_symbol]] + o[1:]
            else:
                return o
        
        # Otherwise (AST has a body), process it
        # Create a symbol and add it to the environment if not have yet
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
        
        # Change the func_symbol's param_list with the processed parameter list
        func_symbol.param_list = local_env[0]
        
        # Visit body
        ast.body.accept(self, [[func_symbol]] + local_env)
        
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
                
                if type(func_symbol.typ) is Unknown and self.isUnknown(expr_t):
                    raise TypeCannotBeInferred(ast)
                
                if type(func_symbol.typ) is Unknown:
                    func_symbol.typ = expr_t
                    return o
                
                if self.isUnknown(expr_t):
                    if type(ast.expr) is Id:
                        self.infer(ast.expr.name, func_symbol.typ, o, VarSymbol)
                    elif type(ast.expr) is CallExpr:
                        self.infer(ast.expr.name.name, func_symbol.typ, o, FuncSymbol)
                    elif type(ast.expr) is ArrayLiteral:
                        if type(func_symbol.typ) is ArrayType and self.isCompatibleArrayType(expr_t, func_symbol.typ):
                            self.inferArray(ast.expr, func_symbol.typ, o)
                        else:
                            raise TypeMismatchInStatement(ast)
                    else:
                        print("This cannot be happening!!!")
                    return o
                
                if type(expr_t) is not type(func_symbol.typ):
                    raise TypeMismatchInStatement(ast)
                break
        return o
    
    def visitAssign(self, ast: Assign, o: List[List[Symbol]]):
        try:
            right_t = ast.rhs.accept(self, o) # Type
            left_t = ast.lhs.accept(self, o) # Type
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        
        if type(left_t) is Unknown and self.isUnknown(right_t):
            raise TypeCannotBeInferred(ast)
        
        if type(left_t) is Unknown:
            # lhs: Id
            self.infer(ast.lhs.name, right_t, o, VarSymbol)
            return o
        
        if self.isUnknown(right_t):
            # rhs: Id | CallExpr | ArrayLiteral
            if type(ast.rhs) is Id:
                self.infer(ast.rhs.name, left_t, o, VarSymbol)
            elif type(ast.rhs) is CallExpr:
                self.infer(ast.rhs.name.name, left_t, o, FuncSymbol)
            elif type(ast.rhs) is ArrayLiteral:
                if type(left_t) is ArrayType and self.isCompatibleArrayType(right_t, left_t):
                    self.inferArray(ast.rhs, left_t, o)
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                print("This cannot be happening!!!")
            return o
        
        if type(right_t) is not type(left_t):
            raise TypeMismatchInStatement(ast)
        return o
    
    def visitIf(self, ast: If, o: List[List[Symbol]]):
        return o
    
    def visitFor(self, ast: For, o: List[List[Symbol]]):
        return o
    
    def visitBreak(self, ast: Break, o: List[List[Symbol]]):
        return o
    
    def visitContinue(self, ast: Continue, o: List[List[Symbol]]):
        return o
    
    def visitCallStmt(self, ast: CallStmt, o: List[List[Symbol]]):
        func_symbol = None
        for symbol in o[-1]: # All functions are in global scope
            if type(symbol) is FuncSymbol and symbol.name == ast.name.name:
                func_symbol = symbol
                break
        
        if not func_symbol:
            raise Undeclared(Function(), ast.name.name)
        
        if type(func_symbol.typ) is Unknown:
            func_symbol.typ = VoidType()
        if type(func_symbol.typ) is not VoidType:
            raise TypeMismatchInStatement(ast)
        
        if len(ast.args) != len(func_symbol.param_list):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(ast.args)):
            arg = ast.args[i] # Expr
            arg_type = arg.accept(self, o) # Type
            param_type = func_symbol.param_list[i].typ # Type
            
            if self.isUnknown(arg_type):
                if type(arg) is Id:
                    self.infer(arg.name, param_type, o, VarSymbol)
                elif type(arg) is CallExpr:
                    self.infer(arg.name.name, param_type, o, FuncSymbol)
                elif type(arg) is ArrayLiteral:
                    if type(param_type) is ArrayType and self.isCompatibleArrayType(arg_type, param_type):
                        self.inferArray(arg, param_type, o)
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    print("This cannot be happening!!!")
                continue
            
            if type(arg_type) is not type(param_type):
                raise TypeMismatchInStatement(ast)
        
        return o
    
    def visitBinaryOp(self, ast: BinaryOp, o: List[List[Symbol]]) -> Type:
        left_t = ast.left.accept(self, o)
        right_t = ast.right.accept(self, o)
        
        if ast.op in ['+', '-', '*', '/', '%', 'and', 'or', '...']:
            # The operators that can be applied to operands of the same type and produce a result of the same type
            if ast.op in ['+', '-', '*', '/', '%']:
                infer_type = NumberType
            elif ast.op in ['and', 'or']:
                infer_type = BoolType
            else:
                infer_type = StringType
            
            if type(left_t) is Unknown:
                if type(ast.left) is Id:
                    left_t = self.infer(ast.left.name, infer_type(), o, VarSymbol)
                else:
                    left_t = self.infer(ast.left.name.name, infer_type(), o, FuncSymbol)
            if type(right_t) is Unknown:
                if type(ast.right) is Id:
                    left_t = self.infer(ast.right.name, infer_type(), o, VarSymbol)
                else:
                    left_t = self.infer(ast.right.name.name, infer_type(), o, FuncSymbol)
            
            if type(left_t) is infer_type and type(right_t) is infer_type:
                return infer_type()
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['=', '!=', '<', '>', '<=', '>=', '==']:
            # The (relational) operators that can be applied to operands of the same type and produce a result of BoolType
            if ast.op == '==':
                infer_type = StringType
            else:
                infer_type = NumberType
            
            if type(left_t) is Unknown:
                if type(ast.left) is Id:
                    left_t = self.infer(ast.left.name, infer_type(), o, VarSymbol)
                else:
                    left_t = self.infer(ast.left.name.name, infer_type(), o, FuncSymbol)
            if type(right_t) is Unknown:
                if type(ast.right) is Id:
                    left_t = self.infer(ast.right.name, infer_type(), o, VarSymbol)
                else:
                    left_t = self.infer(ast.right.name.name, infer_type(), o, FuncSymbol)
            
            if type(left_t) is infer_type and type(right_t) is infer_type:
                return BoolType()
            raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast: UnaryOp, o: List[List[Symbol]]) -> Type:
        e_t = ast.operand.accept(self, o)
        
        if ast.op in ['-', 'not']:
            if ast.op == '-':
                infer_type = NumberType
            else:
                infer_type = BoolType
            
            if type(e_t) is Unknown:
                if type(ast.operand) is Id:
                    e_t = self.infer(ast.operand.name, infer_type(), o, VarSymbol)
                else:
                    e_t = self.infer(ast.operand.name.name, infer_type(), o, FuncSymbol)
            
            if type(e_t) is infer_type:
                return infer_type()
            raise TypeMismatchInExpression(ast)
    
    def visitCallExpr(self, ast: CallExpr, o: List[List[Symbol]]):
        func_symbol = None
        for symbol in o[-1]: # All functions are in global scope
            if type(symbol) is FuncSymbol and symbol.name == ast.name.name:
                func_symbol = symbol
                break
        
        if not func_symbol:
            raise Undeclared(Function(), ast.name.name)
        
        if type(func_symbol.typ) is VoidType:
            raise TypeMismatchInExpression(ast)
        
        if len(ast.args) != len(func_symbol.param_list):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(ast.args)):
            arg = ast.args[i] # Expr
            arg_type = arg.accept(self, o) # Type
            param_type = func_symbol.param_list[i].typ # Type
            
            if self.isUnknown(arg_type):
                if type(arg) is Id:
                    self.infer(arg.name, param_type, o, VarSymbol)
                elif type(arg) is CallExpr:
                    self.infer(arg.name.name, param_type, o, FuncSymbol)
                elif type(arg) is ArrayLiteral:
                    if type(param_type) is ArrayType and self.isCompatibleArrayType(arg_type, param_type):
                        self.inferArray(arg, param_type, o)
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    print("This cannot be happening!!!")
                continue
            
            if type(arg_type) is not type(param_type):
                raise TypeMismatchInExpression(ast)
        
        return func_symbol.typ
    
    def visitId(self, ast: Id, o: List[List[Symbol]]):
        for symbol_list in o:
            for symbol in symbol_list:
                if type(symbol) is VarSymbol and symbol.name == ast.name:
                    return symbol.typ
        raise Undeclared(Identifier(), ast.name)
    
    def visitArrayCell(self, ast: ArrayCell, o: List[List[Symbol]]) -> Type:
        arr_type = ast.arr.accept(self, o)
        idx_types = [expr.accept(self, o) for expr in ast.idx]
        
        if type(arr_type) is Unknown:
            raise TypeCannotBeInferred("")
        if type(arr_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if len(arr_type.size) != len(idx_types):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(idx_types)):
            if type(idx_types[i]) is Unknown:
                if type(ast.idx[i]) is Id:
                    self.infer(ast.idx[i].name, NumberType(), o, VarSymbol)
                else:
                    self.infer(ast.idx[i].name.name, NumberType(), o, FuncSymbol)
                continue
            
            if type(idx_types[i]) is not NumberType:
                raise TypeMismatchInExpression(ast)
        
        return arr_type.eleType
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o: List[List[Symbol]]):
        expr_list = ast.value # List[Expr]
        length = len(expr_list)
        
        # Find the first known type
        expr_types = [expr.accept(self, o) for expr in ast.value] # List[Type]
        common_type = next(filter(lambda typ: not self.isUnknown(typ), expr_types), None)
        if common_type is None:
            common_type = next(filter(lambda typ: type(typ) is not Unknown, expr_types), None)
            size = [float(length)] + (common_type.size if type(common_type) is ArrayType else [])
            return ArrayType(size, Unknown)
        
        # Check or infer elements' type from the common_type
        for i in range(length):
            expr = expr_list[i]
            typ = expr_types[i]
            # typ = expr.accept(self, o)
            
            if type(typ) is ArrayType:
                if type(common_type) is ArrayType and self.isCompatibleArrayType(typ, common_type):
                    self.inferArray(expr, common_type, o)
                raise TypeMismatchInExpression(expr)
            elif type(typ) is Unknown:
                # expr: Id | CallExpr
                if type(expr) is Id:
                    self.infer(expr.name, common_type, o, VarSymbol)
                else:
                    self.infer(expr.name.name, common_type, o, FuncSymbol)
            elif type(typ) is not type(common_type):
                raise TypeMismatchInExpression(expr)
        
        size = [float(length)] + (common_type.size if type(common_type) is ArrayType else [])
        eleType = common_type.eleType if type(common_type) is ArrayType else common_type
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
