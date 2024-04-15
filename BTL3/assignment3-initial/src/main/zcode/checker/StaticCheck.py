from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List

# class FuncType(Type):
#     def __init__(self, param_type: List[Type], ret_type: Type):
#         self.param_type = param_type
#         self.ret_type = ret_type
#     def __str__(self):
#         return f"FuncType({[str(typ) for typ in self.param_type]}, {str(self.ret_type)})"
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
        FuncSymbol("writeNumber", VoidType(), [VarSymbol("arg", NumberType())]),
        FuncSymbol("writeBool", VoidType(), [VarSymbol("arg", BoolType())]),
        FuncSymbol("writeString", VoidType(), [VarSymbol("arg", StringType())])
    ]
    
    def __init__(self, ast: AST):
        self.ast = ast
    
    def check(self):
        return self.ast.accept(self, StaticChecker.builtin_env)
    
    def infer(self, name: str, typ: Type, env: List[List[Symbol]]) -> Type:
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ
        return Unknown()
    
    def inferArray(self, ast: ArrayLiteral, typ: Type, env: List[List[Symbol]], skipIdx: int = -1) -> Type:
        # typ: Type instance for each element of the array literal
        for i in range(len(ast.value)):
            if i == skipIdx:
                continue
            
            expr = ast.value[i]
            if type(expr) is Id:
                self.infer(expr.name, typ, env)
            if type(expr) is CallExpr:
                pass
            if type(expr) is ArrayLiteral:
                # typ: ArrayType(size=[...], eleType=primitive_type)
                eletyp = typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType)
                self.inferArray(expr, eletyp, env)
    
    def isUnknown(self, ast: Type):
        # Check if the Type instance is related to Unknown
        # These kinds of Expr may have Unknown Type: Id, CallExpr, ArrayLiteral
        return (type(ast) is Unknown) or (type(ast) is ArrayType and type(ast.eleType) is Unknown)
    
    def visitProgram(self, ast: Program, o: List[FuncSymbol]):
        # o = StaticChecker.builtin_env
        # The global scope will be env[-1]
        obj = {
            "env": [o],
            "kind": Variable()
        }
        for decl in ast.decl:
            obj["env"] = decl.accept(self, obj)
        
        checkMain = False
        for symbol in obj["env"][-1]:
            if type(symbol) is FuncSymbol:
                if not symbol.defined:
                    raise NoDefinition(symbol.name)
                if symbol.name == "main" and len(symbol.param_list) == 0 and type(symbol.typ) is VoidType:
                    checkMain = True
        
        if not checkMain:
            raise NoEntryPoint()
    
    def visitVarDecl(self, ast: VarDecl, o):
        # ast: name: Id(name: str), varType: Type, modifier: str, varInit: Expr
        # o: dict{ "env": List[List[Symbol]], "kind": Variable | Parameter }
        env, kind = o["env"], o["kind"]
        
        # Check variable/parameter redeclaration (same scope)
        for symbol in env[0]:
            if type(symbol) is VarSymbol and symbol.name == ast.name.name:
                raise Redeclared(kind, ast.name)
        
        # Create symbol
        typ = ast.varType if ast.varType is not None else Unknown()
        var_symbol = VarSymbol(ast.name.name, typ)
        
        # Check/Infer type if initialized
        if ast.varInit:
            pass
        
        # Add symbol to the environment
        ret_env = [env[0] + [var_symbol]] + env[1:]
        return ret_env
    
    def visitFuncDecl(self, ast: FuncDecl, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        env = o["env"]
        
        # Check function redeclaration (in global scope)
        # If function was not defined/implemented yet, just get its symbol
        func_symbol = None
        for symbol in env[-1]:
            if type(symbol) is FuncSymbol and symbol.name == ast.name.name:
                if not symbol.defined:
                    func_symbol = symbol
                    break
                raise Redeclared(Function(), ast.name)
        
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
                return [env[0] + [func_symbol]] + env[1:]
            else:
                return env
        
        # Otherwise (AST has a body), process it
        # Create a symbol and add it to the environment if not have yet
        if not func_symbol:
            func_symbol = FuncSymbol(ast.name.name, Unknown(), [], True)
            ret_env = [env[0] + [func_symbol]] + env[1:]
        else:
            func_symbol.defined = True
            ret_env = env
        
        # Visit parameters
        obj = {
            "env": [[]] + ret_env, # Add function scope
            "kind": Parameter()
        }
        for param in ast.param:
            obj["env"] = param.accept(self, obj)
        
        # Visit body
        obj["env"] = [[]] + obj["env"] # Add local scope
        obj["kind"] = Variable()
        ast.body.accept(self, obj)
        
        return ret_env
    
    def visitBlock(self, ast: Block, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable }
        pass
    
    def visitReturn(self, ast: Return, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitAssign(self, ast: Assign, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitIf(self, ast: If, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitFor(self, ast: For, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitBreak(self, ast: Break, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitContinue(self, ast: Continue, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitCallStmt(self, ast: CallStmt, o):
        # o: dict{ "env": List[List[Symbol]], "kind": Variable (unused) }
        pass
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        pass
    
    def visitUnaryOp(self, ast: UnaryOp, o):
        pass
    
    def visitCallExpr(self, ast: CallExpr, o):
        pass
    
    def visitId(self, ast: Id, o):
        pass
    
    def visitArrayCell(self, ast: ArrayCell, o):
        pass
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o: List[List[Symbol]]):
        # ast.value: List[Expr]
        expr_list = ast.value
        length = len(expr_list)
        
        # Find the first known type
        expr_types = [expr.accept(self, o) for expr in ast.value] # List[Type]
        common_type = next(filter(lambda typ: not self.isUnknown(typ), expr_types), Unknown())
        if type(common_type) is Unknown:
            # size = 
            return ArrayType([], Unknown)
        
        # Check or infer elements' type from the common_type
        for i in range(length):
            expr = expr_list[i]
            typ = expr.accept(self, o)
            if self.isUnknown(typ):
                if type(typ) is Unknown:
                    # expr: Id | CallExpr
                    self.infer(expr.name, common_type, o)
                else:
                    # expr: ArrayLiteral
                    self.inferArray(expr, common_type, o)
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
