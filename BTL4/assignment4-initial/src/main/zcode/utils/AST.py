from abc import ABC, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple

# Base class for all AST nodes
class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass

class Type(AST):
    __metaclass__ = ABCMeta
    pass

class Stmt(AST):
    __metaclass__ = ABCMeta
    pass

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

# Expressions
# Literal
class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

class NumberLiteral(Literal):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"NumLit({str(self.value)})"

class StringLiteral(Literal):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"StringLit({self.value})"

class BooleanLiteral(Literal):
    def __init__(self, value: bool):
        self.value = value

    def __str__(self):
        return f"BooleanLit({'True' if self.value else 'False'})"

@dataclass
class ArrayLiteral(Literal):
    def __init__(self, value: List[Expr]):
        self.value = value

    def __str__(self):
        return f"ArrayLit({', '.join(str(i) for i in self.value)})"

# LHS
class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Id(LHS):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Id({self.name})"

class ArrayCell(LHS):
    def __init__(self, arr: Expr, idx: List[Expr]):
        self.arr = arr
        self.idx = idx

    def __str__(self):
        return f"ArrayCell({str(self.arr)}, [{', '.join(str(i) for i in self.idx)}])"

# Other expressions
# used for binary expression
class BinaryOp(Expr):
    def __init__(self, op: str, left: Expr, right: Expr):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinaryOp({self.op}, {str(self.left)}, {str(self.right)})"

# used for unary expression with orerand like !,+,-
class UnaryOp(Expr):
    def __init__(self, op: str, operand: Expr):
        self.op = op
        self.operand = operand

    def __str__(self):
        return f"UnaryOp({self.op}, {str(self.operand)})"

class CallExpr(Expr):
    def __init__(self, name: Id, args: List[Expr]):
        self.name = name
        self.args = args

    def __str__(self):
        return f"CallExpr({str(self.name)}, [{', '.join(str(i) for i in self.args)}])"

# Types
class NumberType(Type):
    def __str__(self):
        return "NumberType"

class BoolType(Type):
    def __str__(self):
        return "BoolType"

class StringType(Type):
    def __str__(self):
        return "StringType"
    
class VoidType(Type):
    def __str__(self):
        return "VoidType"

class ArrayType(Type):
    def __init__(self, size: List[float], eleType: Type):
        self.size = size
        self.eleType = eleType

    def __str__(self):
        return f"ArrayType([{', '.join(str(i) for i in self.size)}], {str(self.eleType)})"

# Statements
class Assign(Stmt):
    def __init__(self, lhs: Expr, rhs: Expr):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"AssignStmt({str(self.lhs)}, {str(self.rhs)})"

class If(Stmt):
    def __init__(self, expr: Expr, thenStmt: Stmt, elifStmt: List[Tuple[Expr, Stmt]] = [], elseStmt: Stmt = None):
        self.expr = expr
        self.thenStmt = thenStmt
        self.elifStmt = elifStmt # empty list if there is no elif statement
        self.elseStmt = elseStmt # None if there is no else branch

    def __str__(self):
        return f"If(({str(self.expr)}, {str(self.thenStmt)}), [{', '.join(f'({str(x[0])}, {str(x[1])})' for x in self.elifStmt)}], {str(self.elseStmt) if self.elseStmt else 'None'})"

class For(Stmt):
    def __init__(self, name: Id, condExpr: Expr, updExpr: Expr, body: Stmt):
        self.name = name
        self.condExpr = condExpr
        self.updExpr = updExpr
        self.body = body

    def __str__(self):
        return f"For({str(self.name)}, {str(self.condExpr)}, {str(self.updExpr)}, {str(self.body)})"

class Break(Stmt):
    def __str__(self):
        return "Break"

class Continue(Stmt):
    def __str__(self):
        return "Continue"

class Return(Stmt):
    def __init__(self, expr: Expr = None):
        self.expr = expr # None if there is no expression after return

    def __str__(self):
        return f"Return({str(self.expr) if self.expr else ''})"

class CallStmt(Stmt):
    def __init__(self, name: Id, args: List[Expr]):
        self.name = name
        self.args = args

    def __str__(self):
        return f"CallStmt({str(self.name)}, [{', '.join(str(i) for i in self.args)}])"

class Block(Stmt):
    def __init__(self, stmt: List[Stmt]):
        self.stmt = stmt # empty list if there is no statement in block

    def __str__(self):
        return f"Block([{', '.join(str(i) for i in self.stmt)}])"

# Declarations
# used for variable or parameter declaration
class VarDecl(Decl, Stmt):
    def __init__(self, name: Id, varType: Type = None, modifier: str = None, varInit: Expr = None):
        self.name = name
        self.varType = varType # None if there is no type
        self.modifier = modifier # None if there is no modifier
        self.varInit = varInit # None if there is no initial

    def __str__(self):
        return f"VarDecl({str(self.name)}, {str(self.varType) if self.varType else 'None'}, {str(self.modifier) if self.modifier else 'None'}, {str(self.varInit) if self.varInit else 'None'})"

# used for a function declaration
class FuncDecl(Decl):
    # name
    # param 
    # body= None 

    def __init__(self, name: Id, param: List[VarDecl], body: Stmt = None):
        self.name = name
        self.param = param
        self.body = body # None if this is just a declaration-part

    def __str__(self):
        return f"FuncDecl({str(self.name)}, [{', '.join(str(i) for i in self.param)}], {str(self.body) if self.body else 'None'})"

# Program
class Program(AST):
    def __init__(self, decl: List[Decl]):
        self.decl = decl

    def __str__(self):
        return f"Program([{', '.join(str(i) for i in self.decl)}])"
