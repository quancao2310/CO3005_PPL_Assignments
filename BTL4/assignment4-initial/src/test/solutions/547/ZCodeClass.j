.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a [F

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
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a [F
	fconst_0
	f2i
	ldc 5.0
	fastore
	getstatic ZCodeClass.a [F
	fconst_1
	f2i
	ldc 4.0
	fastore
	getstatic ZCodeClass.a [F
	fconst_0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.a [F
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.a [F
	fconst_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static init()V
Label0:
Label2:
	ldc 5.0
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
	putstatic ZCodeClass.a [F
Label3:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
