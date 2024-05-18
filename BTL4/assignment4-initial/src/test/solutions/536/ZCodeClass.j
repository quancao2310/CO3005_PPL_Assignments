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

.method public static foo([F[[Z[Ljava/lang/String;)V
.var 0 is a [F from Label0 to Label1
.var 1 is b [[Z from Label0 to Label1
.var 2 is c [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	aload_0
	fconst_1
	f2i
	ldc 5.0
	fastore
	aload_1
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	iconst_1
	bastore
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x [F from Label2 to Label3
.var 2 is y [[Z from Label2 to Label3
Label2:
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
	astore_1
	ldc 3.0
	f2i
	anewarray [Z
	dup
	iconst_0
	fconst_2
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	astore_2
	aload_1
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_2
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_1
	aload_2
	fconst_2
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "PPL"
	aastore
	dup
	iconst_1
	ldc "hard"
	aastore
	invokestatic ZCodeClass/foo([F[[Z[Ljava/lang/String;)V
	aload_1
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_2
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	baload
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method
