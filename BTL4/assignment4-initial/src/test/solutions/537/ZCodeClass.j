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

.method public static createArray()[F
Label0:
.var 0 is x [F from Label2 to Label3
Label2:
	ldc 10.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_1
	fastore
	dup
	iconst_1
	fconst_2
	fastore
	dup
	iconst_2
	ldc 3.0
	fastore
	dup
	iconst_3
	ldc 4.0
	fastore
	dup
	iconst_4
	ldc 5.0
	fastore
	dup
	iconst_5
	ldc 6.0
	fastore
	dup
	bipush 6
	ldc 7.0
	fastore
	dup
	bipush 7
	ldc 8.0
	fastore
	dup
	bipush 8
	ldc 9.0
	fastore
	dup
	bipush 9
	ldc 10.0
	fastore
	astore_0
	aload_0
	areturn
Label3:
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [F from Label2 to Label3
.var 2 is brr [F from Label2 to Label3
Label2:
	invokestatic ZCodeClass/createArray()[F
	astore_1
	invokestatic ZCodeClass/createArray()[F
	astore_2
	aload_1
	ldc 5.0
	f2i
	faload
	aload_2
	ldc 5.0
	f2i
	faload
	fadd
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 3
.end method
