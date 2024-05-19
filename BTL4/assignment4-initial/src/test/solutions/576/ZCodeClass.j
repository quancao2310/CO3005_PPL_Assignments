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

.method public static sum([F)F
.var 0 is a [F from Label0 to Label1
Label0:
.var 1 is i F from Label2 to Label3
.var 2 is sum F from Label2 to Label3
Label2:
	fconst_0
	fstore_1
	fconst_0
	fstore_2
	fload_1
Label6:
	fload_1
	ldc 10.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
	fload_2
	aload_0
	fload_1
	f2i
	faload
	fadd
	fstore_2
Label4:
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
	fload_2
	freturn
Label3:
Label1:
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
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
	invokestatic ZCodeClass/sum([F)F
	invokestatic io/writeNumber(F)V
	ldc 10.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_2
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_2
	fastore
	dup
	iconst_3
	ldc 4.0
	fastore
	dup
	iconst_4
	fconst_0
	fastore
	dup
	iconst_5
	ldc 5.0
	fastore
	dup
	bipush 6
	fconst_1
	fastore
	dup
	bipush 7
	ldc 9.0
	fastore
	dup
	bipush 8
	fconst_0
	fastore
	dup
	bipush 9
	fconst_0
	fastore
	invokestatic ZCodeClass/sum([F)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method
