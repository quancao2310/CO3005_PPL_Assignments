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

.method public static foo(F)F
.var 0 is x F from Label0 to Label1
Label0:
	fload_0
	fconst_1
	fadd
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [F from Label2 to Label3
.var 2 is b [[F from Label2 to Label3
Label2:
	ldc 15.0
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
	dup
	bipush 10
	ldc 11.0
	fastore
	dup
	bipush 11
	ldc 12.0
	fastore
	dup
	bipush 12
	ldc 13.0
	fastore
	dup
	bipush 13
	ldc 14.0
	fastore
	dup
	bipush 14
	ldc 15.0
	fastore
	astore_1
	ldc 3.0
	f2i
	anewarray [F
	dup
	iconst_0
	ldc 4.0
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
	aastore
	dup
	iconst_1
	ldc 4.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 5.0
	fastore
	dup
	iconst_1
	ldc 6.0
	fastore
	dup
	iconst_2
	ldc 7.0
	fastore
	dup
	iconst_3
	ldc 8.0
	fastore
	aastore
	dup
	iconst_2
	ldc 4.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 9.0
	fastore
	dup
	iconst_1
	ldc 10.0
	fastore
	dup
	iconst_2
	ldc 11.0
	fastore
	dup
	iconst_3
	ldc 12.0
	fastore
	aastore
	astore_2
	aload_1
	ldc 3.0
	fconst_2
	invokestatic ZCodeClass/foo(F)F
	fadd
	f2i
	aload_1
	aload_2
	fconst_2
	f2i
	aaload
	ldc 3.0
	f2i
	faload
	f2i
	faload
	ldc 4.0
	fadd
	fastore
	aload_1
	ldc 6.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method
