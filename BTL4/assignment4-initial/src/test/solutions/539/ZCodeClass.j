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
.var 1 is a [F from Label2 to Label3
.var 2 is b [F from Label2 to Label3
.var 3 is c [F from Label2 to Label3
.var 4 is x [[F from Label2 to Label3
Label2:
	ldc 3.0
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
	astore_1
	ldc 3.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 4.0
	fastore
	dup
	iconst_1
	ldc 5.0
	fastore
	dup
	iconst_2
	ldc 6.0
	fastore
	astore_2
	ldc 3.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 7.0
	fastore
	dup
	iconst_1
	ldc 8.0
	fastore
	dup
	iconst_2
	ldc 9.0
	fastore
	astore_3
	ldc 3.0
	f2i
	anewarray [F
	dup
	iconst_0
	aload_1
	aastore
	dup
	iconst_1
	aload_2
	aastore
	dup
	iconst_2
	aload_3
	aastore
	astore 4
	aload_1
	fconst_0
	f2i
	faload
	aload_2
	fconst_1
	f2i
	faload
	fadd
	aload_3
	fconst_2
	f2i
	faload
	fadd
	aload 4
	fconst_2
	f2i
	aaload
	fconst_0
	f2i
	faload
	fadd
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 5
.end method
