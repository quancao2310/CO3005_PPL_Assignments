from Emitter import Emitter
from Frame import Frame

from abc import ABC
from AST import *
from Visitor import *
from Utils import Utils

from functools import reduce
from typing import List

# Additional types
class MType(Type):
    def __init__(self, partype: List[Type], rettype: Type):
        self.partype = partype
        self.rettype = rettype

class ClassType(Type): # For ZCodeClass
    def __init__(self, className: str):
        self.className = className

# Val class for value of Symbol
class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value: int):
        self.value = value

class CName(Val):
    def __init__(self, value: str):
        self.value = value

# Symbol class
class Symbol:
    def __init__(self, name: str, mtype: Type, value: Val = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    
    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"

class Access():
    def __init__(self, frame: Frame, sym: List[Symbol], isLeft: bool, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class SubBody():
    def __init__(self, frame: Frame, sym: List[Symbol]):
        self.frame = frame
        self.sym = sym

class CodeGenerator:
    def __init__(self):
        self.libName = "io"
    
    def init(self):
        return [
            Symbol("readNumber", MType([], NumberType()), CName(self.libName)),
            Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
            Symbol("readBool", MType([], BoolType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName)),
            Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName)),
        ]
    
    def gen(self, ast: AST, path: str):
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree: AST, env: List[Symbol], path: str):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast: Program, o):
        # Generate default class for program
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, ""))
        # Generate default constructor
        init = FuncDecl(Id("<init>"), [], Block([]))
        self.genMETHOD(init, o, Frame("<init>", VoidType()))
        main = FuncDecl(Id("main"), [], Block([]))
        self.genMETHOD(main, o, Frame("main", VoidType()))
        # Generate code for declarations
        self.emit.emitEPILOG()
        return o

    # def visitClassDecl(self, ast, c):
    #     self.className = ast.classname.name
    #     self.emit = Emitter(self.path+"/" + self.className + ".j")
    #     self.emit.printout(self.emit.emitPROLOG(
    #         self.className, "java.lang.Object"))
    #     [self.visit(ele, SubBody(None, self.env))
    #      for ele in ast.memlist if type(ele) == MethodDecl]
    #     # generate default constructor
    #     self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
    #     ), None, Block([], [])), c, Frame("<init>", VoidType()))
    #     self.emit.emitEPILOG()
    #     return c

    def genMETHOD(self, funcdecl: FuncDecl, o, frame: Frame):
        isInit = funcdecl.name.name == "<init>"
        isMain = funcdecl.name.name == "main"
        if isInit:
            # print("Generating default constructor")
            self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        if isMain:
            # print("Generating main")
            self.emit.printout(self.emit.emitMETHOD("main", MType([ArrayType([0.0], StringType())], VoidType()), True, frame))
        frame.enterScope(False)
        startLabel = frame.getStartLabel()
        endLabel = frame.getEndLabel()
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), startLabel, endLabel, frame))
            self.emit.printout(self.emit.emitLABEL(startLabel, frame))
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0.0], StringType()), startLabel, endLabel, frame))
            self.emit.printout(self.emit.emitLABEL(startLabel, frame))
            self.emit.printout(self.emit.emitGETSTATIC("java/lang/System/out", ClassType("java/io/PrintStream"), frame))
            self.emit.printout(self.emit.emitPUSHCONST("1.0", NumberType(), frame))
            self.emit.printout(self.emit.emitINVOKEVIRTUAL("java/io/PrintStream/print", MType([NumberType()], VoidType()), frame))
            self.emit.printout(self.emit.emitLABEL(endLabel, frame))
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    # def visitMethodDecl(self, ast, o):
    #     frame = Frame(ast.name, ast.returnType)
    #     self.genMETHOD(ast, o.sym, frame)
    #     return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    # def visitCallStmt(self, ast, o):
    #     ctxt = o
    #     frame = ctxt.frame
    #     nenv = ctxt.sym
    #     sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
    #     cname = sym.value.value
    #     ctype = sym.mtype
    #     in_ = ("", list())
    #     for x in ast.param:
    #         str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
    #         in_ = (in_[0] + str1, in_[1].append(typ1))
    #     self.emit.printout(in_[0])
    #     self.emit.printout(self.emit.emitINVOKESTATIC(
    #         cname + "/" + ast.method.name, ctype, frame))

    # def visitNumberLiteral(self, ast, o):
    #     return self.emit.emitPUSHFCONST(ast.value, o.frame), IntType()

    # def visitBinaryOp(self, ast, o):
    #     e1c, e1t = self.visit(ast.left, o)
    #     e2c, e2t = self.visit(ast.right, o)
    #     return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
