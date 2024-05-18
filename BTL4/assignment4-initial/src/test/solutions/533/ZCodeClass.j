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
.var 2 is b F from Label2 to Label3
.var 3 is c F from Label2 to Label3
.var 4 is d F from Label2 to Label3
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
	fconst_1
	fconst_2
	fadd
	fastore
	dup
	iconst_1
	fconst_2
	ldc 3.0
	fmul
	fastore
	dup
	iconst_2
	ldc 3.0
	ldc 4.0
	fdiv
	fastore
	aastore
	dup
	iconst_1
	ldc 3.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 4.0
	ldc 5.0
	fsub
	fastore
	dup
	iconst_1
	ldc 5.0
	fconst_2
	frem
	fastore
	dup
	iconst_2
	ldc 6.0
	ldc 3.0
	fdiv
	fastore
	aastore
	astore_1
	aload_1
	fconst_1
	f2i
	aaload
	fconst_2
	f2i
	faload
	fstore_2
	fconst_1
	aload_1
	fconst_1
	f2i
	aaload
	fconst_1
	f2i
	faload
	fadd
	fstore_3
	aload_1
	fconst_0
	f2i
	aaload
	fconst_2
	f2i
	faload
	fconst_2
	fmul
	fstore 4
	fload_2
	invokestatic io/writeNumber(F)V
	fload_3
	invokestatic io/writeNumber(F)V
	fload 4
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 5
.end method
