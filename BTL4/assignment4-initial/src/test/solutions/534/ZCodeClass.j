.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

.method public static <clinit>()V
Label0:
Label2:
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
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [[F from Label2 to Label3
Label2:
	fconst_2
	f2i
	anewarray [F
	dup
	iconst_0
	ldc 3.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	aastore
	dup
	iconst_1
	ldc 3.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	aastore
	astore_1
	aload_1
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	fconst_1
	fastore
	aload_1
	fconst_0
	f2i
	aaload
	fconst_1
	f2i
	fconst_2
	fastore
	aload_1
	fconst_0
	f2i
	aaload
	fconst_2
	f2i
	ldc 3.0
	ldc 4.0
	fadd
	fastore
	aload_1
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	ldc 5.0
	ldc 6.0
	fmul
	fastore
	aload_1
	fconst_1
	f2i
	aaload
	fconst_1
	f2i
	ldc 7.0
	ldc 8.0
	fsub
	fastore
	aload_1
	fconst_1
	f2i
	aaload
	fconst_2
	f2i
	ldc 9.0
	ldc 10.0
	fdiv
	fastore
	aload_1
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	fconst_0
	f2i
	aaload
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	fconst_0
	f2i
	aaload
	fconst_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	faload
	aload_1
	fconst_1
	f2i
	aaload
	fconst_1
	f2i
	faload
	fadd
	aload_1
	fconst_1
	f2i
	aaload
	fconst_2
	f2i
	faload
	fadd
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
.end method
