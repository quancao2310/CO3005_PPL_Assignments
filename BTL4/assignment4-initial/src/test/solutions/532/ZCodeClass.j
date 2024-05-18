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
.var 2 is b [Z from Label2 to Label3
.var 3 is c [Ljava/lang/String; from Label2 to Label3
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
	ldc 3.0
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_1
	iconst_1
	ior
	bastore
	dup
	iconst_1
	iconst_0
	iconst_0
	iand
	bastore
	dup
	iconst_2
	iconst_1
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	bastore
	astore_2
	fconst_2
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "PPL "
	ldc "is "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aastore
	dup
	iconst_1
	ldc "very "
	ldc "hard"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aastore
	astore_3
	aload_1
	fconst_0
	f2i
	aaload
	fconst_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_2
	fconst_1
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_3
	fconst_1
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 4
.end method
