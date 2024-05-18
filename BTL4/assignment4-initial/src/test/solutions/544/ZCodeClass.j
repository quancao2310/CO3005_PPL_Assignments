.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a [[[[F
.field static b [F
.field static c F

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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d F from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	ldc 4.0
	fstore_1
	fconst_2
	f2i
	anewarray [[[F
	dup
	iconst_0
	fconst_1
	f2i
	anewarray [[F
	dup
	iconst_0
	fconst_1
	f2i
	anewarray [F
	dup
	iconst_0
	getstatic ZCodeClass.b [F
	aastore
	aastore
	aastore
	dup
	iconst_1
	fconst_1
	f2i
	anewarray [[F
	dup
	iconst_0
	fconst_1
	f2i
	anewarray [F
	dup
	iconst_0
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	getstatic ZCodeClass.c F
	fastore
	dup
	iconst_1
	fload_1
	fastore
	aastore
	aastore
	aastore
	putstatic ZCodeClass.a [[[[F
	getstatic ZCodeClass.a [[[[F
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	faload
	getstatic ZCodeClass.a [[[[F
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_1
	f2i
	faload
	fadd
	getstatic ZCodeClass.a [[[[F
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	faload
	fadd
	getstatic ZCodeClass.a [[[[F
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_1
	f2i
	faload
	fadd
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 13
.limit locals 2
.end method

.method public static init()V
Label0:
Label2:
	fconst_2
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
	putstatic ZCodeClass.b [F
	ldc 3.0
	putstatic ZCodeClass.c F
Label3:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
