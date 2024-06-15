from Emitter import Emitter
from Frame import Frame

from abc import ABC
from AST import *
from Visitor import *
from CodeGenError import *
from typing import List

# Additional types
class MType(Type):
    def __init__(self, partype: List[Type], rettype: Type):
        self.partype = partype
        self.rettype = rettype

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

class CName(Val):
    def __init__(self, value: str):
        self.value = value

# Symbol class
class Symbol:
    def __init__(self, name: str, mtype: Type, value: Val, defined = True):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.defined = defined

class Access():
    def __init__(self, frame: Frame, sym: List[Symbol], isLeft: bool, expr: Expr = None):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.expr = expr

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
    
    def infer_symbol(self, name: str, typ: Type, env: List[Symbol], isMType: bool):
        if isMType:
            symbol_list = filter(lambda symbol: type(symbol.mtype) is MType, env)
        else:
            symbol_list = filter(lambda symbol: type(symbol.mtype) is not MType, env)
        symbol = next(filter(lambda sym: sym.name == name, symbol_list))
        if isMType:
            symbol.mtype.rettype = typ
        else:
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
    
    def isUnknown(self, ast: Type):
        return (type(ast) is Unknown) or (type(ast) is ArrayType and type(ast.eleType) is Unknown)
    
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
        ele = self.get_default_value(eleType) if len(dimensions) == 1 else self.get_default_array(dimensions[1:], eleType)
        return ArrayLiteral([ele for _ in range(int(dimensions[0]))])
    
    def genMETHOD(self, funcdecl: FuncDecl, o: List[Symbol], frame: Frame):
        """Generate code as a method for the equivalent function declaration in ZCode."""
        func_symbol = next(filter(lambda sym: sym.name == funcdecl.name.name and type(sym.mtype) is MType, o))
        isClinit = funcdecl.name.name == "<clinit>"
        isInit = funcdecl.name.name == "<init>"
        isMain = funcdecl.name.name == "main"
        mtype = MType([ArrayType([0.0], StringType())], VoidType()) if isMain else func_symbol.mtype # MType, might have Unknown return type
        code = ""
        
        frame.enterScope(True)
        startLabel = frame.getStartLabel()
        endLabel = frame.getEndLabel()
        local_subbody = SubBody(frame, [Symbol("<func>", None, None)] + o)
        
        # Generate parameter declarations
        if isInit:
            code += self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), startLabel, endLabel, frame)
        elif isMain:
            code += self.emit.emitVAR(frame.getNewIndex(), "args", mtype.partype[0], startLabel, endLabel, frame)
        else:
            for param in funcdecl.param:
                _, local_subbody = param.accept(self, local_subbody)
        
        code += self.emit.emitLABEL(startLabel, frame)
        
        # Generate statements in body
        if isInit:
            code += self.emit.emitREADVAR("this", ClassType(self.className), 0, frame)
            code += self.emit.emitINVOKESPECIAL(frame)
        else:
            code += funcdecl.body.accept(self, local_subbody)
        
        code += self.emit.emitLABEL(endLabel, frame)
        
        # After visiting the body, we now have inferred the types of all used variables and the function itself.
        # Let's call emitVAR and emitMETHOD
        if not any([isInit, isClinit, isMain]):
            for sym in local_subbody.sym:
                if sym.name == "<func>":
                    break
                if type(sym.mtype) is Unknown:
                    sym.mtype = NumberType() # Not used anyway so doesn't matter
                code = self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, startLabel, endLabel, frame) + code
        
        if type(mtype.rettype) is Unknown:
            mtype.rettype = VoidType()
        if type(mtype.rettype) is VoidType:
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
        init = FuncDecl(Id("<init>"), [], Block([]))
        
        # Visit all global variables first to get the symbols
        global_subbody = SubBody(None, self.env)
        for decl in filter(lambda decl: type(decl) is VarDecl, ast.decl):
            _, global_subbody = decl.accept(self, global_subbody)
        
        # Generate static initializer and default constructor
        mtype, cname = MType([], VoidType()), CName(self.className)
        self.genMETHOD(self.clinit, [Symbol("<clinit>", mtype, cname)] + global_subbody.sym, Frame("<clinit>", VoidType()))
        self.genMETHOD(init, [Symbol("<init>", mtype, cname)], Frame("<init>", VoidType()))
        
        # Generate static methods for functions
        for decl in filter(lambda decl: type(decl) is FuncDecl, ast.decl):
            global_subbody = decl.accept(self, global_subbody)
        
        # Generate static fields for global variables (after inference)
        code = ""
        for var in global_subbody.sym:
            if type(var.mtype) is not MType:
                if type(var.mtype) is Unknown:
                    var.mtype = NumberType()
                code = self.emit.emitATTRIBUTE(var.name, var.mtype, False) + code
        self.emit.printout_prepend(code)
        self.emit.printout_prepend(self.emit.emitPROLOG(self.className, ""))
        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        var_symbol = Symbol(ast.name.name, ast.varType if ast.varType else Unknown(), None)
        ret_subbody = SubBody(o.frame, [var_symbol] + o.sym)
        code = ""
        
        if o.frame:
            # Local variable
            var_symbol.value = Index(o.frame.getNewIndex())
            if ast.varInit:
                code = self.visit(Assign(ast.name, ast.varInit), ret_subbody)
            elif ast.varType:
                code = self.visit(Assign(ast.name, self.get_default_value(ast.varType)), ret_subbody)
        else:
            # Global variable
            var_symbol.value = CName(self.className)
            if ast.varInit:
                self.clinit.body.stmt.append(Assign(ast.name, ast.varInit))
            elif ast.varType:
                self.clinit.body.stmt.append(Assign(ast.name, self.get_default_value(ast.varType)))
        
        return code, ret_subbody
    
    def visitFuncDecl(self, ast: FuncDecl, o: SubBody):
        # If the AST does not have a body (no implementation part), create a symbol and return
        if not ast.body:
            func_symbol = Symbol(
                ast.name.name,
                MType([param.varType for param in ast.param], Unknown()),
                CName(self.className),
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
        frame = o.frame
        local_subbody = SubBody(frame, [Symbol("<block>", None, None)] + o.sym)
        code = ""
        frame.enterScope(False)
        startLabel = frame.getStartLabel()
        endLabel = frame.getEndLabel()
        
        code += self.emit.emitLABEL(startLabel, frame)
        for stmt in ast.stmt:
            if type(stmt) is VarDecl:
                init_c, local_subbody = stmt.accept(self, local_subbody)
                code += init_c
            else:
                code += stmt.accept(self, local_subbody)
        code += self.emit.emitLABEL(endLabel, frame)
        
        for sym in local_subbody.sym:
            if sym.name == "<block>":
                break
            if type(sym.mtype) is Unknown:
                sym.mtype = NumberType() # Not used anyway so doesn't matter
            code = self.emit.emitVAR(sym.value.value, sym.name, sym.mtype, startLabel, endLabel, frame) + code
        frame.exitScope()
        return code
    
    def visitReturn(self, ast: Return, o: SubBody):
        func_symbol = next(filter(lambda sym: sym.name == o.frame.name and type(sym.mtype) is MType, o.sym))
        expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False)) if ast.expr else ("", VoidType())
        
        if self.isUnknown(func_symbol.mtype.rettype):
            func_symbol.mtype.rettype = expr_t
        if self.isUnknown(expr_t):
            self.infer(ast.expr, func_symbol.mtype.rettype, o.sym)
            expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False))
        
        return expr_c + self.emit.emitRETURN(expr_t, o.frame)
    
    def visitAssign(self, ast: Assign, o: SubBody):
        if type(ast.lhs) is ArrayCell:
            cell_c, _ = ast.lhs.accept(self, Access(o.frame, o.sym, True, ast.rhs))
            return cell_c
        
        readAccess = Access(o.frame, o.sym, False)
        writeAccess = Access(o.frame, o.sym, True)
        
        right_c, right_t = ast.rhs.accept(self, readAccess)
        left_c, left_t = ast.lhs.accept(self, writeAccess)
        
        if type(left_t) is Unknown:
            self.infer(ast.lhs, right_t, o.sym)
            left_c, left_t = ast.lhs.accept(self, writeAccess)
        if self.isUnknown(right_t):
            self.infer(ast.rhs, left_t, o.sym)
            right_c, right_t = ast.rhs.accept(self, readAccess)
            left_c, left_t = ast.lhs.accept(self, writeAccess)
        
        return right_c + left_c
    
    def visitIf(self, ast: If, o: SubBody):
        expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False))
        if self.isUnknown(expr_t):
            self.infer(ast.expr, BoolType(), o.sym)
            expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False))
        code = expr_c
        exitLabel = o.frame.getNewLabel()
        
        if len(ast.elifStmt) == 0:
            if not ast.elseStmt:
                code += self.emit.emitIFFALSE(exitLabel, o.frame)
                code += ast.thenStmt.accept(self, o)
            else:
                elseLabel = o.frame.getNewLabel()
                code += self.emit.emitIFFALSE(elseLabel, o.frame)
                code += ast.thenStmt.accept(self, o)
                code += self.emit.emitGOTO(exitLabel, o.frame)
                code += self.emit.emitLABEL(elseLabel, o.frame)
                code += ast.elseStmt.accept(self, o)
        else:
            length = len(ast.elifStmt)
            elifLabel = o.frame.getNewLabel()
            code += self.emit.emitIFFALSE(elifLabel, o.frame)
            code += ast.thenStmt.accept(self, o)
            code += self.emit.emitGOTO(exitLabel, o.frame)
            if not ast.elseStmt:
                for i in range(length):
                    code += self.emit.emitLABEL(elifLabel, o.frame)
                    expr, stmt = ast.elifStmt[i]
                    expr_c, expr_t = expr.accept(self, Access(o.frame, o.sym, False))
                    if self.isUnknown(expr_t):
                        self.infer(ast.expr, BoolType(), o.sym)
                        expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False))
                    code += expr_c
                    elifLabel = o.frame.getNewLabel()
                    code += self.emit.emitIFFALSE(elifLabel if i != length - 1 else exitLabel, o.frame)
                    code += stmt.accept(self, o)
                    if i != length - 1:
                        code += self.emit.emitGOTO(exitLabel, o.frame)
            else:
                elseLabel = o.frame.getNewLabel()
                for i in range(length):
                    code += self.emit.emitLABEL(elifLabel, o.frame)
                    expr, stmt = ast.elifStmt[i]
                    expr_c, expr_t = expr.accept(self, Access(o.frame, o.sym, False))
                    if self.isUnknown(expr_t):
                        self.infer(ast.expr, BoolType(), o.sym)
                        expr_c, expr_t = ast.expr.accept(self, Access(o.frame, o.sym, False))
                    code += expr_c
                    elifLabel = o.frame.getNewLabel()
                    code += self.emit.emitIFFALSE(elifLabel if i != length - 1 else elseLabel, o.frame)
                    code += stmt.accept(self, o)
                    code += self.emit.emitGOTO(exitLabel, o.frame)
                code += self.emit.emitLABEL(elseLabel, o.frame)
                code += ast.elseStmt.accept(self, o)
        code += self.emit.emitLABEL(exitLabel, o.frame)
        return code
    
    def visitFor(self, ast: For, o: SubBody):
        # Store the initial value to reset it after the loop
        id_c, id_t = ast.name.accept(self, Access(o.frame, o.sym, False))
        if type(id_t) is Unknown:
            self.infer_symbol(ast.name.name, NumberType(), o.sym, False)
            id_c, id_t = ast.name.accept(self, Access(o.frame, o.sym, False))
        code = id_c
        
        o.frame.enterLoop()
        breakLabel = o.frame.getBreakLabel()
        continueLabel = o.frame.getContinueLabel()
        conditionLabel = o.frame.getNewLabel()
        
        code += self.emit.emitLABEL(conditionLabel, o.frame)
        cond_c, cond_t = ast.condExpr.accept(self, Access(o.frame, o.sym, False))
        if self.isUnknown(cond_t):
            self.infer(ast.condExpr, BoolType(), o.sym)
            cond_c, cond_t = ast.condExpr.accept(self, Access(o.frame, o.sym, False))
        code += cond_c
        code += self.emit.emitIFTRUE(breakLabel, o.frame)
        code += ast.body.accept(self, o)
        code += self.emit.emitLABEL(continueLabel, o.frame)
        code += self.visit(Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr)), o)
        code += self.emit.emitGOTO(conditionLabel, o.frame)
        code += self.emit.emitLABEL(breakLabel, o.frame)
        o.frame.exitLoop()
        
        # Reset the initial value
        id_c, id_t = ast.name.accept(self, Access(o.frame, o.sym, True))
        code += id_c
        return code
    
    def visitBreak(self, ast: Break, o: SubBody):
        return self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame)
    
    def visitContinue(self, ast: Continue, o: SubBody):
        return self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame)
    
    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        func_symbol = next(filter(lambda sym: sym.name == ast.name.name and type(sym.mtype) is MType, o.sym))
        if type(func_symbol.mtype.rettype) is Unknown:
            func_symbol.mtype.rettype = VoidType()
        code = ""
        
        for i in range(len(ast.args)):
            arg_c, arg_t = ast.args[i].accept(self, Access(o.frame, o.sym, False))
            param_t = func_symbol.mtype.partype[i]
            
            if self.isUnknown(arg_t):
                self.infer(ast.args[i], param_t, o.sym)
                arg_c, arg_t = ast.args[i].accept(self, Access(o.frame, o.sym, False))
            
            code += arg_c
        code += self.emit.emitINVOKESTATIC(func_symbol.value.value + "/" + ast.name.name, func_symbol.mtype, o.frame)
        return code
    
    def visitBinaryOp(self, ast: BinaryOp, o: Access):
        if ast.op in ['+', '-', '*', '/', '%']:
            in_t = out_t = NumberType()
        elif ast.op in ['and', 'or']:
            in_t = out_t = BoolType()
        elif ast.op == "...":
            in_t = out_t = StringType()
        elif ast.op in ['=', '!=', '<', '>', '<=', '>=']:
            in_t, out_t = NumberType(), BoolType()
        else:
            in_t, out_t = StringType(), BoolType()
        
        left_c, left_t = ast.left.accept(self, o)
        if self.isUnknown(left_t):
            self.infer(ast.left, in_t, o.sym)
            left_c, left_t = ast.left.accept(self, o)
        
        right_c, right_t = ast.right.accept(self, o)
        if self.isUnknown(right_t):
            self.infer(ast.right, in_t, o.sym)
            right_c, right_t = ast.right.accept(self, o)
        
        if ast.op in ['+', '-']:
            op_c = self.emit.emitADDOP(ast.op, left_t, o.frame)
        elif ast.op in ['*', '/']:
            op_c = self.emit.emitMULOP(ast.op, left_t, o.frame)
        elif ast.op == "%":
            op_c = self.emit.emitMOD(left_t, o.frame)
        elif ast.op == 'and':
            op_c = self.emit.emitANDOP(o.frame)
        elif ast.op == 'or':
            op_c = self.emit.emitOROP(o.frame)
        elif ast.op == "...":
            op_c = self.emit.emitCONCAT(o.frame)
        else:
            op_c = self.emit.emitREOP(ast.op, left_t, o.frame)
        
        return left_c + right_c + op_c, out_t
    
    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        if ast.op == '-':
            res_t = NumberType()
        else:
            res_t = BoolType()
        
        expr_c, expr_t = ast.operand.accept(self, o)
        if self.isUnknown(expr_t):
            self.infer(ast.operand, res_t, o.sym)
            expr_c, expr_t = ast.operand.accept(self, o)
        
        if ast.op == '-':
            op_c = self.emit.emitNEGOP(expr_t, o.frame)
        else:
            op_c = self.emit.emitNOT(expr_t, o.frame)
        
        return expr_c + op_c, expr_t
    
    def visitCallExpr(self, ast: CallExpr, o: Access):
        func_symbol = next(filter(lambda sym: sym.name == ast.name.name and type(sym.mtype) is MType, o.sym))
        return_t = func_symbol.mtype.rettype
        code = ""
        
        if type(return_t) is Unknown:
            return "", return_t
        
        for i in range(len(ast.args)):
            arg_c, arg_t = ast.args[i].accept(self, o)
            param_t = func_symbol.mtype.partype[i]
            
            if self.isUnknown(arg_t):
                self.infer(ast.args[i], param_t, o.sym)
                arg_c, arg_t = ast.args[i].accept(self, o)
            
            code += arg_c
        code += self.emit.emitINVOKESTATIC(func_symbol.value.value + "/" + ast.name.name, func_symbol.mtype, o.frame)
        return code, return_t
    
    def visitId(self, ast: Id, o: Access):
        symbol = next(filter(lambda sym: sym.name == ast.name and type(sym.mtype) is not MType, o.sym))
        typ = symbol.mtype
        
        if type(typ) is Unknown:
            return "", typ
        
        if o.isLeft:
            try:
                if type(symbol.value) is Index:
                    code = self.emit.emitWRITEVAR(ast.name, typ, symbol.value.value, o.frame)
                else:
                    code = self.emit.emitPUTSTATIC(symbol.value.value + "." + ast.name, typ, o.frame)
            except IllegalRuntimeException: # Illegal Runtime: Pop empty stack
                o.frame.push()
                return "", typ
        else:
            if type(symbol.value) is Index:
                code = self.emit.emitREADVAR(ast.name, typ, symbol.value.value, o.frame)
            else:
                code = self.emit.emitGETSTATIC(symbol.value.value + "." + ast.name, typ, o.frame)
        
        return code, typ
    
    def visitArrayCell(self, ast: ArrayCell, o: Access):
        length = len(ast.idx)
        code = ""
        
        if o.isLeft:
            rhs = o.expr
            o.frame.push() # Simulate pushing the array reference
            o.frame.push() # Simulate pushing the array index
            
            right_c, right_t = rhs.accept(self, Access(o.frame, o.sym, False))
            o.frame.pop() # Pop simulated-array to actually push the array reference
            arr_c, arr_t = ast.arr.accept(self, Access(o.frame, o.sym, False)) # Id or CallExpr
            
            if type(arr_t) is Unknown:
                self.infer(ast, right_t, o.sym)
                arr_c, arr_t = ast.arr.accept(self, Access(o.frame, o.sym, False))
            if self.isUnknown(right_t):
                self.infer(ast.rhs, arr_t.eleType, o.sym)
                right_c, right_t = ast.rhs.accept(self, Access(o.frame, o.sym, False))
            
            o.frame.pop() # Pop simulated-index to actually push the index
            o.frame.pop() # Simulate not pushing the rhs yet
        else:
            arr_c, arr_t = ast.arr.accept(self, Access(o.frame, o.sym, False)) # Id or CallExpr
            if type(arr_t) is Unknown:
                return "", arr_t
        
        for i in range(length):
            idx_c, idx_t = ast.idx[i].accept(self, Access(o.frame, o.sym, False))
            if self.isUnknown(idx_t):
                self.infer(ast.idx[i], NumberType(), o.sym)
                idx_c, idx_t = ast.idx[i].accept(self, Access(o.frame, o.sym, False))
            
            code += idx_c
            code += self.emit.emitF2I(o.frame)
            if i != length - 1:
                code += self.emit.emitALOAD(ArrayType([], None), o.frame)
        
        if o.isLeft:
            o.frame.push() # Push the rhs again
            code = arr_c + code + right_c
            code += self.emit.emitASTORE(arr_t.eleType, o.frame)
        else:
            code = arr_c + code
            code += self.emit.emitALOAD(arr_t.eleType, o.frame)
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
        if common_t is None:
            return "", ArrayType([float(length)], Unknown())
        
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
            if self.isUnknown(ele_t):
                self.infer(ast.value[i], common_t, o.sym)
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
