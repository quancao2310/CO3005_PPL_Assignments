from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import List

class FuncType(Type):
    def __init__(self, param_type: List[Type], ret_type: Type):
        self.param_type = param_type
        self.ret_type = ret_type
    def __str__(self):
        return f"FuncType({[str(typ) for typ in self.param_type]}, {str(self.ret_type)})"

class Symbol:
    def __init__(self, name: str, typ: Type, value = None):
        self.name = name
        self.typ = typ
        self.value = value

class StaticChecker(BaseVisitor, Utils):
    global_env = [
        Symbol("readNumber", FuncType([], NumberType())),
        Symbol("writeNumber", FuncType([NumberType()], VoidType())),
        Symbol("readBool", FuncType([], BoolType())),
        Symbol("writeBool", FuncType([BoolType()], VoidType())),
        Symbol("readString", FuncType([], StringType())),
        Symbol("writeString", FuncType([StringType()], VoidType()))
    ]
    
    def __init__(self, ast: AST):
        self.ast = ast
    
    def check(self):
        return self.ast.accept(self, StaticChecker.global_env)
    
    def visitProgram(self, ast, param):
        raise NoEntryPoint()
    
    def visitVarDecl(self, ast, param):
        pass
    
    def visitFuncDecl(self, ast, param):
        pass
    
    def visitNumberType(self, ast, param):
        pass
    
    def visitBoolType(self, ast, param):
        pass
    
    def visitStringType(self, ast, param):
        pass
    
    def visitArrayType(self, ast, param):
        pass
    
    def visitBinaryOp(self, ast, param):
        pass
    
    def visitUnaryOp(self, ast, param):
        pass
    
    def visitCallExpr(self, ast, param):
        pass
    
    def visitId(self, ast, param):
        pass
    
    def visitArrayCell(self, ast, param):
        pass
    
    def visitBlock(self, ast, param):
        pass
    
    def visitIf(self, ast, param):
        pass
    
    def visitFor(self, ast, param):
        pass
    
    def visitContinue(self, ast, param):
        pass
    
    def visitBreak(self, ast, param):
        pass
    
    def visitReturn(self, ast, param):
        pass
    
    def visitAssign(self, ast, param):
        pass
    
    def visitCallStmt(self, ast, param):
        pass
    
    def visitNumberLiteral(self, ast, param):
        pass
    
    def visitBooleanLiteral(self, ast, param):
        pass
    
    def visitStringLiteral(self, ast, param):
        pass
    
    def visitArrayLiteral(self, ast, param):
        pass
