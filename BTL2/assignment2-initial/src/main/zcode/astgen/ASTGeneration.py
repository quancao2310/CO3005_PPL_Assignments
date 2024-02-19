from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(ctx.decl_list().accept(self))
    
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.decl().accept(self)]
        return [ctx.decl().accept(self)] + ctx.decl_list().accept(self)
    
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return ctx.getChild(0).accept(self)
    
    def visitVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        return ctx.getChild(0).accept(self)
    
    def visitPrimitive_decl(self, ctx:ZCodeParser.Primitive_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = ctx.primitive_type().accept(self)
        modifier = None
        varInit = ctx.optional_init().accept(self)
        return VarDecl(name, varType, modifier, varInit)
    
    def visitVar_keyword_decl(self, ctx:ZCodeParser.Var_keyword_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = None
        modifier = ctx.VAR().getText()
        varInit = ctx.expression().accept(self)
        return VarDecl(name, varType, modifier, varInit)
    
    def visitDynamic_keyword_decl(self, ctx:ZCodeParser.Dynamic_keyword_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = None
        modifier = ctx.DYNAMIC().getText()
        varInit = ctx.optional_init().accept(self)
        return VarDecl(name, varType, modifier, varInit)
    
    def visitOptional_init(self, ctx:ZCodeParser.Optional_initContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.expression().accept(self)
    
    def visitArray_decl(self, ctx:ZCodeParser.Array_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = ArrayType(ctx.array_dimensions().accept(self), ctx.primitive_type().accept(self))
        modifier = None
        varInit = ctx.optional_array_init().accept(self)
        return VarDecl(name, varType, modifier, varInit)
    
    def visitArray_dimensions(self, ctx:ZCodeParser.Array_dimensionsContext):
        return ctx.dimension_list().accept(self)
    
    def visitDimension_list(self, ctx:ZCodeParser.Dimension_listContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBER_LIT().getText())]
        return [float(ctx.NUMBER_LIT().getText())] + ctx.dimension_list().accept(self)
    
    def visitOptional_array_init(self, ctx:ZCodeParser.Optional_array_initContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.expression().accept(self)
    
    def visitFunction_decl(self, ctx:ZCodeParser.Function_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = ctx.param_decl().accept(self)
        body = ctx.optional_impl().accept(self)
        return FuncDecl(name, param, body)
    
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        return ctx.param_list().accept(self)
    
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.param_list_prime().accept(self)
    
    def visitParam_list_prime(self, ctx:ZCodeParser.Param_list_primeContext):
        if ctx.getChildCount() == 1:
            return [ctx.param().accept(self)]
        return [ctx.param().accept(self)] + ctx.param_list_prime().accept(self)
    
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        name = Id(ctx.IDENTIFIER().getText())
        modifier = None
        varInit = None
        if ctx.array_dimensions():
            varType = ArrayType(ctx.array_dimensions().accept(self), ctx.primitive_type().accept(self))
        else:
            varType = ctx.primitive_type().accept(self)
        return VarDecl(name, varType, modifier, varInit)
    
    def visitOptional_impl(self, ctx:ZCodeParser.Optional_implContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.body().accept(self)
    
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return ctx.getChild(0).accept(self)
    
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return ctx.getChild(0).accept(self)
    
    def visitVariable_stmt(self, ctx:ZCodeParser.Variable_stmtContext):
        return ctx.variable_decl().accept(self)
    
    def visitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        lhs = ctx.lhs_asmt().accept(self)
        rhs = ctx.expression().accept(self)
        return Assign(lhs, rhs)
    
    def visitLhs_asmt(self, ctx:ZCodeParser.Lhs_asmtContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        return ArrayCell(Id(ctx.IDENTIFIER().getText()), ctx.expr_list().accept(self))
    
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        expr = ctx.expression().accept(self)
        thenStmt = ctx.statement().accept(self)
        elifStmt = ctx.elif_list().accept(self)
        elseStmt = ctx.else_stmt().accept(self)
        return If(expr, thenStmt, elifStmt, elseStmt)
    
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return (ctx.expression().accept(self), ctx.statement().accept(self))
    
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [ctx.elif_stmt().accept(self)] + ctx.elif_list().accept(self)
    
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.statement().accept(self)
    
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = ctx.expression(0).accept(self)
        updExpr = ctx.expression(1).accept(self)
        body = ctx.statement().accept(self)
        return For(name, condExpr, updExpr, body)
    
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return Continue()
    
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return Return(ctx.return_value().accept(self))
    
    def visitReturn_value(self, ctx:ZCodeParser.Return_valueContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.expression().accept(self)
    
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        call_expr = ctx.call_expr().accept(self)
        return CallStmt(call_expr.name, call_expr.args)
    
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return Block(ctx.stmt_list().accept(self))
    
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [ctx.statement().accept(self)] + ctx.stmt_list().accept(self)
    
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.CONCAT().getText(), ctx.expr1(0).accept(self), ctx.expr1(1).accept(self))
        return ctx.expr1(0).accept(self)
    
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.rel_op().accept(self), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self))
        return ctx.expr2(0).accept(self)
    
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.expr2():
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr2().accept(self), ctx.expr3().accept(self))
        return ctx.expr3().accept(self)
    
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.expr3():
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr3().accept(self), ctx.expr4().accept(self))
        return ctx.expr4().accept(self)
    
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.expr4():
            return BinaryOp(ctx.getChild(1).getText(), ctx.expr4().accept(self), ctx.expr5().accept(self))
        return ctx.expr5().accept(self)
    
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.expr5():
            return UnaryOp(ctx.NOT().getText(), ctx.expr5().accept(self))
        return ctx.expr6().accept(self)
    
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.expr6():
            return UnaryOp(ctx.SUB().getText(), ctx.expr6().accept(self))
        return ctx.expr7().accept(self)
    
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.index_expr():
            return ctx.index_expr().accept(self)
        return ctx.operand().accept(self)
    
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.boolean_lit():
            return ctx.boolean_lit().accept(self)
        if ctx.array_lit():
            return ctx.array_lit().accept(self)
        if ctx.call_expr():
            return ctx.call_expr().accept(self)
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return ctx.expression().accept(self)
    
    def visitBoolean_lit(self, ctx:ZCodeParser.Boolean_litContext):
        return BooleanLiteral(ctx.getChild(0).getText() == 'true')
    
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return ArrayLiteral(ctx.expr_list().accept(self))
    
    def visitCall_expr(self, ctx:ZCodeParser.Call_exprContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), ctx.argument_list().accept(self))
    
    def visitArgument_list(self, ctx:ZCodeParser.Argument_listContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.expr_list().accept(self)
    
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return ArrayCell(ctx.expr_for_indexing().accept(self), ctx.expr_list().accept(self))
    
    def visitExpr_for_indexing(self, ctx:ZCodeParser.Expr_for_indexingContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return ctx.call_expr().accept(self)
    
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        if ctx.NUMBER():
            return NumberType()
        if ctx.BOOL():
            return BoolType()
        return StringType()
    
    def visitRel_op(self, ctx:ZCodeParser.Rel_opContext):
        return ctx.getChild(0).getText()
    
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.expression().accept(self)]
        return [ctx.expression().accept(self)] + ctx.expr_list().accept(self)
    
    def visitNonempty_newline_list(self, ctx:ZCodeParser.Nonempty_newline_listContext):
        return None
    
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return None
