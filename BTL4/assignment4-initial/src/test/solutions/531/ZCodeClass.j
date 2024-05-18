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
.var 1 is a [[[F from Label2 to Label3
.var 2 is b [[F from Label2 to Label3
.var 3 is c [[[Z from Label2 to Label3
.var 4 is d [[Ljava/lang/String; from Label2 to Label3
Label2:
	fconst_1
	f2i
	anewarray [[F
	dup
	iconst_0
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
	aastore
	astore_1
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
	fastore
	dup
	iconst_1
	fconst_2
	fastore
	dup
	iconst_2
	ldc 3.0
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
	fastore
	dup
	iconst_1
	ldc 5.0
	fastore
	dup
	iconst_2
	ldc 6.0
	fastore
	aastore
	astore_2
	fconst_2
	f2i
	anewarray [[Z
	dup
	iconst_0
	fconst_2
	f2i
	anewarray [Z
	dup
	iconst_0
	ldc 3.0
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
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	ldc 3.0
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
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	anewarray [Z
	dup
	iconst_0
	ldc 3.0
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
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	ldc 3.0
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
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	aastore
	astore_3
	fconst_2
	f2i
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	fconst_2
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
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "very"
	aastore
	dup
	iconst_1
	ldc "hard"
	aastore
	aastore
	astore 4
	aload_2
	fconst_1
	f2i
	aaload
	fconst_0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_3
	fconst_1
	f2i
	aaload
	fconst_1
	f2i
	aaload
	fconst_1
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload 4
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 10
.limit locals 5
.end method
