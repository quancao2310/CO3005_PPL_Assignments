.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static fib [F

.method public static <clinit>()V
Label0:
Label2:
	ldc 10.0
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
	dup
	iconst_3
	fconst_0
	fastore
	dup
	iconst_4
	fconst_0
	fastore
	dup
	iconst_5
	fconst_0
	fastore
	dup
	bipush 6
	fconst_0
	fastore
	dup
	bipush 7
	fconst_0
	fastore
	dup
	bipush 8
	fconst_0
	fastore
	dup
	bipush 9
	fconst_0
	fastore
	putstatic ZCodeClass.fib [F
Label3:
Label1:
	return
.limit stack 4
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
.var 1 is i F from Label2 to Label3
Label2:
	getstatic ZCodeClass.fib [F
	fconst_0
	f2i
	fconst_0
	fastore
	getstatic ZCodeClass.fib [F
	fconst_1
	f2i
	fconst_1
	fastore
	fconst_2
	fstore_1
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
	getstatic ZCodeClass.fib [F
	fload_1
	f2i
	getstatic ZCodeClass.fib [F
	fload_1
	fconst_1
	fsub
	f2i
	faload
	getstatic ZCodeClass.fib [F
	fload_1
	fconst_2
	fsub
	f2i
	faload
	fadd
	fastore
Label4:
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
	getstatic ZCodeClass.fib [F
	ldc 9.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
.end method
