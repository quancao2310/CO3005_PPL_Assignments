from abc import ABC
from AST import *

class Kind(ABC):
    def __str__(self):
        return self.__class__.__name__

class Identifier(Kind):
    pass

class Variable(Kind):
    pass

class Function(Kind):
    pass

class Parameter(Kind):
    pass


class StaticError(Exception):
    pass

class Redeclared(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Redeclared {str(self.kind)}: {self.name}"

class Undeclared(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Undeclared {str(self.kind)}: {self.name}"

class TypeMismatchInExpression(StaticError):
    def __init__(self, expr: Expr):
        self.expr = expr

    def __str__(self):
        return f"Type Mismatch In Expression: {str(self.expr)}"

class TypeMismatchInStatement(StaticError):
    def __init__(self, stmt: Stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Type Mismatch In Statement: {str(self.stmt)}"

class TypeCannotBeInferred(StaticError):
    def __init__(self, stmt: Stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Type Cannot Be Inferred: {str(self.stmt)}"

class NoDefinition(StaticError):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"No Function Definition: {self.name}"

class MustInLoop(StaticError):
    def __init__(self, stmt: Stmt):
        self.stmt = stmt

    def __str__(self):
        return f"{str(self.stmt)} Not In Loop"

class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"
