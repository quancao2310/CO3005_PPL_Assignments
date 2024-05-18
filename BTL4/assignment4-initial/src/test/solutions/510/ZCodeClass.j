.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

.method public static <clinit>()V
Label0:
Label2:
	return
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LZCodeClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(FZZ)V
.var 0 is x F from Label0 to Label1
.var 1 is y Z from Label0 to Label1
.var 2 is z Z from Label0 to Label1
Label0:
	return
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fconst_1
	iconst_1
	iconst_0
	invokestatic ZCodeClass/foo(FZZ)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
