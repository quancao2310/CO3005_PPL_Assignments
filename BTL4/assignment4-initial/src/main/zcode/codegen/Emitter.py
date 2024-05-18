from MachineCode import JasminCode
import CodeGenerator as cgen
from CodeGenError import IllegalOperandException
from AST import *
from Utils import *

class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()
    
    def getJVMType(self, inType):
        typeIn = type(inType)
        
        if typeIn is NumberType:
            return "F"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "[" * len(inType.size) + self.getJVMType(inType.eleType)
        elif typeIn is cgen.MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType:
            return "L" + inType.className + ";"
    
    def getFullType(self, inType):
        typeIn = type(inType)
        
        if typeIn is NumberType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
        elif typeIn is cgen.ClassType:
            return inType.className
    
    def emitPUSHICONST(self, in_, frame):
        # in: Int or String
        # frame: Frame
        
        if type(in_) is int:
            frame.push()
            i = in_
            if i >= -1 and i <= 5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            else:
                return self.jvm.emitLDC(str(i))
        elif type(in_) is str:
            if in_ == "True":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "False":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)
    
    def emitPUSHFCONST(self, in_, frame):
        # in_: String
        # frame: Frame
        
        f = float(in_)
        frame.push()
        if f == 0.0 or f == 1.0 or f == 2.0:
            return self.jvm.emitFCONST(str(f))
        else:
            return self.jvm.emitLDC(in_)
    
    ''' generate code to push a constant onto the operand stack.
    *   @param in the lexeme of the constant
    *   @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        # in_: String
        # typ: Type
        # frame: Frame
        
        if type(typ) is NumberType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is BoolType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        else:
            raise IllegalOperandException(in_)
    
    ''' generate code to push an array reference onto the operand stack.
    *   only generate array for the first dimension.
    *   @param in the type of the array (dimensions and element type)
    '''
    def emitPUSHARRAY(self, in_: ArrayType, frame):
        # in_: ArrayType([x], NumberType/BoolType) -> newarray
        # in_: ArrayType([x], StringType) -> anewarray
        # in_: ArrayType([x, y, z...], any) -> anewarray
        result = list()
        result.append(self.emitPUSHFCONST(str(in_.size[0]), frame))
        result.append(self.jvm.emitF2I())
        
        if len(in_.size) > 1:
            typ = self.getJVMType(ArrayType(in_.size[1:], in_.eleType))
        else:
            typ = self.getFullType(in_.eleType)
        
        frame.pop()
        if len(in_.size) == 1 and type(in_.eleType) in [NumberType, BoolType]:
            result.append(self.jvm.emitNEWARRAY(typ))
        else:
            result.append(self.jvm.emitANEWARRAY(typ))
        return ''.join(result)
    
    ##############################################################
    
    def emitALOAD(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index -> ..., value
        
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))
    
    def emitASTORE(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., arrayref, index, value -> ...
        
        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))
    
    ''' generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label of the scope where the variable is active.
    '''
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        # in_: Int
        # varName: String
        # inType: Type
        # fromLabel: Int
        # toLabel: Int
        # frame: Frame
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)
    
    def emitREADVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ... -> ..., value
        
        frame.push()
        if type(inType) is NumberType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is cgen.ClassType or type(inType) is StringType or type(inType) is ArrayType:
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)
    
    ''' generate the second instruction for array cell access
    *
    '''
    def emitREADVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ... -> ..., value
        
        # frame.push()
        raise IllegalOperandException(name)
    
    ''' generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''
    def emitWRITEVAR(self, name, inType, index, frame):
        # name: String
        # inType: Type
        # index: Int
        # frame: Frame
        # ..., value -> ...
        
        frame.pop()
        if type(inType) is NumberType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        elif type(inType) is cgen.ClassType or type(inType) is StringType or type(inType) is ArrayType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)
    
    ''' generate the second instruction for array cell access
    *
    '''
    def emitWRITEVAR2(self, name, typ, frame):
        # name: String
        # typ: Type
        # frame: Frame
        # ..., value -> ...
        
        # frame.push()
        raise IllegalOperandException(name)
    
    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''
    def emitATTRIBUTE(self, lexeme, in_, isFinal, value = None):
        # lexeme: String
        # in_: Type
        # isFinal: Boolean
        # value: String
        return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal)
    
    def emitGETSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        
        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))
    
    def emitPUTSTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))
    
    def emitGETFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))
    
    def emitPUTFIELD(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        
        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))
    
    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method (i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        # lexeme: String
        # in_: MType
        # frame: Frame
        
        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))
    
    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        # lexeme: String
        # in_: MType
        # frame: Frame
        
        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()
    
    ''' generate code to invoke a virtual method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        # lexeme: String
        # in_: MType
        # frame: Frame
        
        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))
    
    ''' generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_, frame):
        # in_: Type
        # frame: Frame
        # ..., value -> ..., result
        if type(in_) is NumberType:
            return self.jvm.emitFNEG()
        return self.jvm.emitINEG()
    
    def emitNOT(self, in_, frame):
        # in_: Type
        # frame: Frame
        
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("True", in_, frame))
        frame.pop()
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("False", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)
    
    ''' generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result
        
        frame.pop()
        if lexeme == "+":
            if type(in_) is NumberType:
                return self.jvm.emitFADD()
        else:
            if type(in_) is NumberType:
                return self.jvm.emitFSUB()
    
    ''' generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitMULOP(self, lexeme, in_, frame):
        # lexeme: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result
        
        frame.pop()
        if lexeme == "*":
            if type(in_) is NumberType:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is NumberType:
                return self.jvm.emitFDIV()
    
    def emitDIV(self, frame):
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIDIV()
    
    def emitMOD(self, in_, frame):
        # frame: Frame
        
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFREM()
        return self.jvm.emitIREM()
    
    ''' generate iand
    '''
    def emitANDOP(self, frame):
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIAND()
    
    ''' generate ior
    '''
    def emitOROP(self, frame):
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIOR()
    
    ''' generate code to concat strings
    '''
    def emitCONCAT(self, frame):
        # frame: Frame
        return self.emitINVOKEVIRTUAL("java/lang/String/concat", cgen.MType([StringType()], StringType()), frame)
    
    def emitREOP(self, op, in_, frame):
        # op: String
        # in_: Type
        # frame: Frame
        # ..., value1, value2 -> ..., result
        
        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()
        
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            result.append(self.jvm.emitFCMPL())
            if op == ">":
                result.append(self.jvm.emitIFLE(labelF))
            elif op == ">=":
                result.append(self.jvm.emitIFLT(labelF))
            elif op == "<":
                result.append(self.jvm.emitIFGE(labelF))
            elif op == "<=":
                result.append(self.jvm.emitIFGT(labelF))
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(labelF))
            elif op == "=":
                result.append(self.jvm.emitIFNE(labelF))
            result.append(self.emitPUSHCONST("True", BoolType(), frame))
            frame.pop()
            result.append(self.emitGOTO(labelO, frame))
            result.append(self.emitLABEL(labelF, frame))
            result.append(self.emitPUSHCONST("False", BoolType(), frame))
            result.append(self.emitLABEL(labelO, frame))
        elif type(in_) is StringType:
            frame.push()
            result.append(self.jvm.emitINVOKEVIRTUAL("java/lang/String/equals", "(Ljava/lang/Object;)Z"))
        return ''.join(result)
    
    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        # op: String
        # in_: Type
        # trueLabel: Int
        # falseLabel: Int
        # frame: Frame
        # ..., value1, value2 -> ..., result
        
        result = list()
        
        frame.pop()
        frame.pop()
        if type(in_) is NumberType:
            result.append(self.jvm.emitFCMPL())
            if op == ">":
                result.append(self.jvm.emitIFLE(falseLabel))
            elif op == ">=":
                result.append(self.jvm.emitIFLT(falseLabel))
            elif op == "<":
                result.append(self.jvm.emitIFGE(falseLabel))
            elif op == "<=":
                result.append(self.jvm.emitIFGT(falseLabel))
            elif op == "!=":
                result.append(self.jvm.emitIFEQ(falseLabel))
            elif op == "=":
                result.append(self.jvm.emitIFNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)
    
    ''' generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''
    def emitMETHOD(self, lexeme, in_, isStatic, frame):
        # lexeme: String
        # in_: MType
        # isStatic: Boolean
        # frame: Frame
        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)
    
    ''' generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        # frame: Frame
        
        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)
    
    ''' generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''
    
    ''' generate code to jump to label if the value on top of operand stack is true.
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        # label: Int
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIFGT(label)
    
    ''' generate code to jump to label if the value on top of operand stack is false.
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        # label: Int
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIFLE(label)
    
    def emitIFICMPGT(self, label, frame):
        # label: Int
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIFICMPGT(label)
    
    def emitIFICMPLT(self, label, frame):
        # label: Int
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitIFICMPLT(label)
    
    ''' generate code to duplicate the value on the top of the operand stack.
    *   Stack:
    *   Before: ..., value1
    *   After:  ..., value1, value1
    '''
    def emitDUP(self, frame):
        # frame: Frame
        
        frame.push()
        return self.jvm.emitDUP()
    
    def emitPOP(self, frame):
        # frame: Frame
        
        frame.pop()
        return self.jvm.emitPOP()
    
    ''' generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        # frame: Frame
        return self.jvm.emitI2F()
    
    ''' generate code to exchange a floating-point number on top of stack to an integer.
    '''
    def emitF2I(self, frame):
        # frame: Frame
        return self.jvm.emitF2I()
    
    ''' generate code to return.
    *   @param in the type of the returned expression.
    '''
    def emitRETURN(self, in_, frame):
        # in_: Type
        # frame: Frame
        
        if type(in_) is VoidType:
            return self.jvm.emitRETURN()
        frame.pop()
        if type(in_) is NumberType:
            return self.jvm.emitFRETURN()
        elif type(in_) is BoolType:
            return self.jvm.emitIRETURN()
        elif type(in_) is cgen.ClassType or type(in_) is StringType or type(in_) is ArrayType:
            return self.jvm.emitARETURN()
    
    ''' generate code that represents a label
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        # label: Int
        # frame: Frame
        return self.jvm.emitLABEL(label)
    
    ''' generate code to jump to a label
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        # label: Int
        # frame: Frame
        return self.jvm.emitGOTO(label)
    
    ''' generate some starting directives for a class.
    *   .source MPC.CLASSNAME.java
    *   .class public MPC.CLASSNAME
    *   .super java/lang/Object
    '''
    def emitPROLOG(self, name, parent):
        # name: String
        # parent: String
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER(
            "java/lang/Object" if parent == "" else parent))
        return ''.join(result)
    
    def emitLIMITSTACK(self, num):
        # num: Int
        return self.jvm.emitLIMITSTACK(num)
    
    def emitLIMITLOCAL(self, num):
        # num: Int
        return self.jvm.emitLIMITLOCAL(num)
    
    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()
    
    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        # in_: String
        self.buff.append(in_)
    
    def printout_prepend(self, in_):
        # in_: String
        self.buff.insert(0, in_)
    
    def clearBuff(self):
        self.buff.clear()
