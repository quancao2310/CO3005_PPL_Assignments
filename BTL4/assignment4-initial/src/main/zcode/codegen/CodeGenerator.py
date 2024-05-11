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
    def __str__(self):
        return f"MType({[str(typ) for typ in self.partype]}, {str(self.rettype)})"

class ClassType(Type): # For ZCodeClass
    def __init__(self, className: str):
        self.className = className

class Unknown(Type):
    def __str__(self):
        return "Unknown"

# Val class for value of Symbol
class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value: int):
        self.value = value
    def __str__(self):
        return f"Index({self.value})"

class CName(Val):
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        return f"CName({self.value})"

# Symbol class
class Symbol:
    def __init__(self, name: str, mtype: Type, value: Val, startLabel = None, endLabel = None, defined = True):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.startLabel = startLabel
        self.endLabel = endLabel
        self.defined = defined
    def __str__(self):
        return f"Symbol({self.name}, {str(self.mtype)}, {str(self.value)}, {self.startLabel}, {self.endLabel}, {self.defined})"

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

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree: AST, env: List[Symbol], path: str):
        self.astTree = astTree
        self.env = env
        self.path = path
    
    def infer_symbol(self, name: str, typ: Type, env: List[Symbol], isMType: bool) -> Type:
        if isMType:
            symbol_list = filter(lambda symbol: type(symbol.mtype) is MType, env)
        else:
            symbol_list = filter(lambda symbol: type(symbol.mtype) is not MType, env)
        symbol = next(filter(lambda sym: sym.name == name, symbol_list))
        symbol.mtype = typ
    
    def infer_array(self, ast: ArrayLiteral, typ: ArrayType, env: List[Symbol]):
        eleType = typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType)
        for expr in ast.value:
            self.infer(expr, eleType, env)
    
    def infer(self, expr: Expr, typ: Type, env: List[Symbol]):
        if type(expr) is Id:
            self.infer_symbol(expr.name, typ, env, False)
        elif type(expr) is CallExpr:
            self.infer_symbol(expr.name.name, typ, env, True)
        elif type(expr) is ArrayLiteral:
            self.infer_array(expr, typ, env)
        elif type(expr) is ArrayCell:
            self.infer(expr.arr, ArrayType([0 for _ in range(len(expr.idx))], typ), env)
    
    def emit_var_after_inference(self, symbol: Symbol, frame: Frame) -> str:
        if type(symbol.value) is Index:
            return self.emit.emitVAR(symbol.value.value, symbol.name, symbol.mtype, symbol.startLabel, symbol.endLabel, frame)
        else:
            return self.emit.emitATTRIBUTE(symbol.name, symbol.mtype, False)
    
    def isUnknown(self, ast: Type):
        return (type(ast) is Unknown) or (type(ast) is ArrayType and type(ast.eleType) is Unknown) or (type(ast) is MType and type(ast.rettype) is Unknown)
    
    def get_default_value(self, typ: Type):
        if type(typ) is NumberType:
            return NumberLiteral(0.0)
        if type(typ) is BoolType:
            return BooleanLiteral(False)
        if type(typ) is StringType:
            return StringLiteral("")
        if type(typ) is ArrayType:
            return self.get_default_array(typ.size, typ.eleType)
    
    def get_default_array(self, dimensions: List[float], eleType: Type):
        if len(dimensions) == 1:
            return ArrayLiteral([self.get_default_value(eleType) for _ in range(int(dimensions[0]))])
        else:
            return ArrayLiteral([self.get_default_array(dimensions[1:], eleType) for _ in range(int(dimensions[0]))])
    
    def genMETHOD(self, funcdecl: FuncDecl, o: List[Symbol], frame: Frame):
        """
        Generate code as a method for the equivalent function declaration in ZCode.
        If the function has a declaration-only part, do not generate anything.
        """
        func_symbol = next(filter(lambda sym: sym.name == funcdecl.name.name and type(sym.mtype) is MType, o), None)
        isClinit = funcdecl.name.name == "<clinit>"
        isInit = funcdecl.name.name == "<init>"
        isMain = funcdecl.name.name == "main"
        code = ""
        
        if isInit or isClinit:
            mtype = MType([], VoidType())
        elif isMain:
            mtype = MType([ArrayType([0.0], StringType())], VoidType())
        else:
            mtype = func_symbol.mtype # MType, might have Unknown return type
        
        # Enter scope of function and generate parameter and body first
        frame.enterScope(True)
        startLabel = frame.getStartLabel()
        endLabel = frame.getEndLabel()
        local_subbody = SubBody(frame, [Symbol("!!!", None, None)] + o)
        
        # Generate parameter declarations
        if isInit:
            code += self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), startLabel, endLabel, frame)
        elif isMain:
            code += self.emit.emitVAR(frame.getNewIndex(), "args", mtype.partype[0], startLabel, endLabel, frame)
        else:
            local_subbody = reduce(lambda prev, curr: curr.accept(self, prev), funcdecl.param, local_subbody)
        
        code += self.emit.emitLABEL(startLabel, frame)
        
        # Generate statements in body
        if isInit:
            code += self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)
            code += self.emit.emitINVOKESPECIAL(frame)
            code += self.emit.emitRETURN(VoidType(), frame)
        else:
            code += funcdecl.body.accept(self, local_subbody)
        
        code += self.emit.emitLABEL(endLabel, frame)
        
        # After visiting the body, we now have inferred the types of all used variables and the function itself.
        # Let's call emitVAR and emitMETHOD
        if not any([isInit, isClinit, isMain]):
            for sym in local_subbody.sym:
                if sym.name == "!!!":
                    break
                if type(sym.mtype) is Unknown:
                    sym.mtype = NumberType() # Not used anyway so doesn't matter
                code = self.emit_var_after_inference(sym, frame) + code
        
        if type(mtype.rettype) is Unknown:
            mtype.rettype = VoidType()
            code += self.emit.emitRETURN(VoidType(), frame)
        code = self.emit.emitMETHOD(funcdecl.name.name, mtype, not isInit, frame) + code
        code += self.emit.emitENDMETHOD(frame)
        self.emit.printout(code)
        frame.exitScope()
    
    def visitProgram(self, ast: Program, o):
        # Default class for program
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.clinit = FuncDecl(Id("<clinit>"), [], Block([]))
        self.init = FuncDecl(Id("<init>"), [], Block([]))
        
        o = SubBody(None, [])
        for decl in ast.decl:
            if type(decl) is VarDecl:
                o = decl.accept(self, o)
        static_vars = [sym for sym in o.sym]
        o.sym += self.env
        
        # Generate static initializer (class constructor)
        self.clinit.body.stmt.append(Return())
        self.genMETHOD(self.clinit, [Symbol("<clinit>", MType([], VoidType()), CName(self.className))] + o.sym, Frame("<clinit>", VoidType()))
        
        # Generate default constructor
        self.genMETHOD(self.init, [], Frame("<init>", VoidType()))
        
        # Generate static methods for functions
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                o = decl.accept(self, o)
        
        # Generate static fields for global variables
        code = ""
        for var in static_vars:
            code = self.emit.emitATTRIBUTE(var.name, var.mtype, False) + code
        self.emit.printout_prepend(code)
        self.emit.printout_prepend(self.emit.emitPROLOG(self.className, ""))
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        var_symbol = Symbol(ast.name.name, ast.varType if ast.varType else Unknown(), None)
        ret_subbody = SubBody(o.frame, [var_symbol] + o.sym)
        
        if o.frame:
            # Local variable
            idx = o.frame.getNewIndex()
            var_symbol.startLabel = o.frame.getStartLabel()
            var_symbol.endLabel = o.frame.getEndLabel()
            if ast.varInit:
                code = self.visit(Assign(ast.name, ast.varInit), ret_subbody)
                self.emit.printout(code)
            elif ast.varType:
                code = self.visit(Assign(ast.name, self.get_default_value(ast.varType)), ret_subbody)
                self.emit.printout(code)
            val = Index(idx)
        else:
            # Global variable
            if ast.varInit:
                _, init_t = ast.varInit.accept(self, Access(Frame("", Unknown()), ret_subbody.sym, False))
                var_symbol.mtype = init_t
                self.clinit.body.stmt.append(Assign(ast.name, ast.varInit))
            elif ast.varType:
                self.clinit.body.stmt.append(Assign(ast.name, self.get_default_value(ast.varType)))
            val = CName(self.className)
        
        var_symbol.value = val
        return ret_subbody
    
    def visitFuncDecl(self, ast: FuncDecl, o: SubBody):
        # If the AST does not have a body (no implementation part), create a symbol and return
        if not ast.body:
            func_symbol = Symbol(
                ast.name.name,
                MType([param.varType for param in ast.param], Unknown()),
                CName(self.className),
                None,
                None,
                False,
            )
            return SubBody(None, [func_symbol] + o.sym)
        
        # Otherwise, process the function
        frame = Frame(ast.name.name, Unknown())
        # The function might have been declared, try to get its symbol. If not, create a symbol.
        func_symbol = next(filter(lambda sym: sym.name == ast.name.name and type(sym.mtype) is MType, o.sym), None)
        if func_symbol is None:
            func_symbol = Symbol(
                ast.name.name,
                MType([param.varType for param in ast.param], Unknown()),
                CName(self.className),
            )
            ret_subbody = SubBody(None, [func_symbol] + o.sym)
        else:
            func_symbol.defined = True
            frame.returnType = func_symbol.mtype.rettype
            ret_subbody = SubBody(None, o.sym)
        
        # Generate a ZCodeClass method for this function
        self.genMETHOD(ast, ret_subbody.sym, frame)
        return ret_subbody
    
    def visitBlock(self, ast: Block, o: SubBody):
        code = ""
        o.frame.enterScope(False)
        for stmt in ast.stmt:
            code += stmt.accept(self, o)
        o.frame.exitScope()
        return code
    
    def visitReturn(self, ast: Return, o: SubBody):
        func_symbol = next(filter(lambda sym: sym.name == o.frame.name and type(sym.mtype) is MType, o.sym))
        expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False)) if ast.expr else ("", VoidType())
        
        if self.isUnknown(func_symbol.mtype):
            func_symbol.mtype.rettype = expr_t
        
        return expr_c + self.emit.emitRETURN(expr_t, o.frame)
    
    def visitAssign(self, ast: Assign, o: SubBody):
        right_c, right_t = ast.rhs.accept(self, Access(o.frame, o.sym, False))
        
        if type(ast.lhs) is ArrayCell:
            left_c, left_t = ast.lhs.accept(self, Access(o.frame, o.sym, True))
            left_c_arr, left_c_store = left_c
            
            if type(left_t) is Unknown:
                self.infer(ast.lhs, right_t, o.sym)
            if self.isUnknown(right_t):
                self.infer(ast.rhs, left_t, o.sym)
            
            return left_c_arr + right_c + left_c_store
        if type(ast.lhs) is Id:
            left_c, left_t = ast.lhs.accept(self, Access(o.frame, o.sym, True))
            
            if type(left_t) is Unknown:
                self.infer(ast.lhs, right_t, o.sym)
                left_c, left_t = ast.lhs.accept(self, Access(o.frame, o.sym, True))
            if self.isUnknown(right_t):
                self.infer(ast.rhs, left_t, o.sym)
            
            return right_c + left_c
    
    def visitIf(self, ast: If, o: SubBody):
        return
    
    def visitFor(self, ast: For, o: SubBody):
        return
    
    def visitBreak(self, ast: Break, o: SubBody):
        return
    
    def visitContinue(self, ast: Continue, o: SubBody):
        return
    
    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        # print([str(sym) for sym in o.sym])
        func_symbol = next(filter(lambda sym: sym.name == ast.name.name and type(sym.mtype) is MType, o.sym))
        if type(func_symbol.mtype.rettype) is Unknown:
            func_symbol.mtype.rettype = VoidType()
        cname = func_symbol.value.value
        ctype = func_symbol.mtype
        
        code = ""
        for i in range(len(ast.args)):
            arg_c, arg_t = ast.args[i].accept(self, Access(o.frame, o.sym, False))
            param_t = func_symbol.mtype.partype[i]
            
            if self.isUnknown(arg_t):
                arg_t = self.infer(ast.args[i], param_t, o)
            
            code += arg_c
        code += self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, o.frame)
        
        # code = self.emit.emitGETSTATIC("ZCodeClass.e", NumberType(), o.frame)
        # code += self.emit.emitINVOKESTATIC("io.writeNumber", MType([NumberType()], VoidType()), o.frame)
        return code
    
    def visitBinaryOp(self, ast: BinaryOp, o: Access):
        return
    
    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        return
    
    def visitCallExpr(self, ast: CallExpr, o: Access):
        # symbol = next(filter(lambda sym: sym.name == ast.name.name and type(sym.mtype) is MType, o.sym))
        # for i in range(len(ast.args)):
        #     arg_c, arg_t = ast.args[i].accept(self, o)
        #     # tmpp: MType = symbol.mtype
        #     param_t = symbol.mtype.partype[i]
            
        #     if self.isUnknown(arg_t):
        #         self.infer(ast.args[i], param_t, o.sym)
        return
    
    def visitId(self, ast: Id, o: Access):
        symbol = next(filter(lambda sym: sym.name == ast.name and type(sym.mtype) is not MType, o.sym))
        typ = symbol.mtype
        
        if type(typ) is Unknown:
            return "", Unknown()
        
        if type(symbol.value) is Index:
            idx = symbol.value.value
            if o.isLeft:
                code = self.emit.emitWRITEVAR(ast.name, typ, idx, o.frame)
            else:
                code = self.emit.emitREADVAR(ast.name, typ, idx, o.frame)
        elif type(symbol.value) is CName:
            lexeme = symbol.value.value + "." + ast.name
            if o.isLeft:
                code = self.emit.emitPUTSTATIC(lexeme, typ, o.frame)
            else:
                code = self.emit.emitGETSTATIC(lexeme, typ, o.frame)
        
        return code, typ
    
    def visitArrayCell(self, ast: ArrayCell, o: Access):
        arr_c, arr_t = ast.arr.accept(self, Access(o.frame, o.sym, False)) # For Id or CallExpr
        length = len(ast.idx)
        
        if type(arr_t) is Unknown:
            return "", Unknown()
        
        for i in range(length):
            _, idx_t = ast.idx[i].accept(self, o)
            
            if self.isUnknown(idx_t):
                self.infer(ast.idx[i], NumberType(), o.sym)
        
        for i in range(length - 1):
            idx_c, _ = ast.idx[i].accept(self, Access(o.frame, o.sym, False))
            arr_c += idx_c
            arr_c += self.emit.emitALOAD(arr_t, o.frame)
        
        last_idx_c, _ = ast.idx[-1].accept(self, Access(o.frame, o.sym, False))
        arr_c += last_idx_c
        if o.isLeft:
            # Left-hand side of assignment
            code = [arr_c, self.emit.emitASTORE(arr_t.eleType, o.frame)]
        else:
            code = arr_c + self.emit.emitALOAD(arr_t.eleType, o.frame)
        return code, arr_t.eleType
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o: Access):
        length = len(ast.value)
        
        # Find the first known type
        common_t = None
        for i in range(length):
            _, expr_t = ast.value[i].accept(self, o)
            if not self.isUnknown(expr_t):
                common_t = expr_t
                break
        
        # If there is none, it may exist an array of Unknowns
        # Choose it instead to check size constraint
        if common_t is None:
            for i in range(length):
                _, expr_t = ast.value[i].accept(self, o)
                if type(expr_t) is ArrayType:
                    common_t = expr_t
                    break
            
            if common_t is None:
                return "", ArrayType([float(length)], Unknown())
        
        # Infer elements' type from the common_t Type
        for i in range(length):
            ele_c, ele_t = ast.value[i].accept(self, o)
            
            if self.isUnknown(ele_t):
                self.infer(ast.value[i], common_t, o.sym)
        
        # Create the ArrayType of this array literal
        size = [float(length)] + (common_t.size if type(common_t) is ArrayType else [])
        eleType = common_t.eleType if type(common_t) is ArrayType else common_t
        arrayType = ArrayType(size, eleType)
        
        # Generate code for array literal
        code = self.emit.emitPUSHARRAY(arrayType, o.frame)
        for i in range(length):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            ele_c, ele_t = ast.value[i].accept(self, o)
            code += ele_c
            code += self.emit.emitASTORE(ele_t, o.frame)
        return code, arrayType
    
    def visitNumberLiteral(self, ast: NumberLiteral, o: Access):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        jvm_str = "\"" + ast.value.replace("\'\"", "\\\"") + "\""
        typ = StringType()
        return self.emit.emitPUSHCONST(jvm_str, typ, o.frame), typ
    
    def visitArrayType(self, ast: ArrayType, o):
        return ast
    
    def visitNumberType(self, ast: NumberType, o):
        return ast
    
    def visitBoolType(self, ast: BoolType, o):
        return ast
    
    def visitStringType(self, ast: StringType, o):
        return ast
