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
.var 2 is b [Z from Label2 to Label3
.var 3 is c [Ljava/lang/String; from Label2 to Label3
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
	astore_1
	ldc 5.0
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
	dup
	iconst_2
	iconst_1
	bastore
	dup
	iconst_3
	iconst_0
	bastore
	dup
	iconst_4
	iconst_1
	bastore
	astore_2
	ldc 4.0
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "PPL"
	aastore
	dup
	iconst_1
	ldc "is"
	aastore
	dup
	iconst_2
	ldc "very"
	aastore
	dup
	iconst_3
	ldc "hard"
	aastore
	astore_3
	aload_1
	ldc 5.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_2
	ldc 3.0
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_3
	fconst_0
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
.end method
