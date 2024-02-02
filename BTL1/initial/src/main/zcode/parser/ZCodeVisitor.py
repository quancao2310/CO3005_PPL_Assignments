# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_decl.
    def visitVariable_decl(self, ctx:ZCodeParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_decl.
    def visitPrimitive_decl(self, ctx:ZCodeParser.Primitive_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_keyword_decl.
    def visitVar_keyword_decl(self, ctx:ZCodeParser.Var_keyword_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_keyword_decl.
    def visitDynamic_keyword_decl(self, ctx:ZCodeParser.Dynamic_keyword_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_init.
    def visitOptional_init(self, ctx:ZCodeParser.Optional_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_decl.
    def visitArray_decl(self, ctx:ZCodeParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_dimensions.
    def visitArray_dimensions(self, ctx:ZCodeParser.Array_dimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimension_list.
    def visitDimension_list(self, ctx:ZCodeParser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_array_init.
    def visitOptional_array_init(self, ctx:ZCodeParser.Optional_array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_decl.
    def visitFunction_decl(self, ctx:ZCodeParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl.
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list_prime.
    def visitParam_list_prime(self, ctx:ZCodeParser.Param_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_impl.
    def visitOptional_impl(self, ctx:ZCodeParser.Optional_implContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_stmt.
    def visitVariable_stmt(self, ctx:ZCodeParser.Variable_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:ZCodeParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs_asmt.
    def visitLhs_asmt(self, ctx:ZCodeParser.Lhs_asmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_value.
    def visitReturn_value(self, ctx:ZCodeParser.Return_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_stmt.
    def visitCall_stmt(self, ctx:ZCodeParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolean_lit.
    def visitBoolean_lit(self, ctx:ZCodeParser.Boolean_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#call_expr.
    def visitCall_expr(self, ctx:ZCodeParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argument_list.
    def visitArgument_list(self, ctx:ZCodeParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_for_indexing.
    def visitExpr_for_indexing(self, ctx:ZCodeParser.Expr_for_indexingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_type.
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#rel_op.
    def visitRel_op(self, ctx:ZCodeParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nonempty_newline_list.
    def visitNonempty_newline_list(self, ctx:ZCodeParser.Nonempty_newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list.
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return self.visitChildren(ctx)



del ZCodeParser