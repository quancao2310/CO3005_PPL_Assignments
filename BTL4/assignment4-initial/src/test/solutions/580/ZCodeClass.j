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

.method public static is_leap(F)Z
.var 0 is year F from Label0 to Label1
Label0:
	fload_0
	ldc 400.0
	frem
	fconst_0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_0
	ldc 4.0
	frem
	fconst_0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	fload_0
	ldc 100.0
	frem
	fconst_0
	fcmpl
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ior
	ireturn
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is years [F from Label2 to Label3
.var 2 is i F from Label2 to Label3
Label2:
	ldc 4.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 2001.0
	fastore
	dup
	iconst_1
	ldc 2004.0
	fastore
	dup
	iconst_2
	ldc 1900.0
	fastore
	dup
	iconst_3
	ldc 2000.0
	fastore
	astore_1
	fconst_0
	fstore_2
	fload_2
Label6:
	fload_2
	ldc 4.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	aload_1
	fload_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	fload_2
	f2i
	faload
	invokestatic ZCodeClass/is_leap(F)Z
	ifle Label12
	ldc " is a leap year\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label11
Label12:
	ldc " is not a leap year\n"
	invokestatic io/writeString(Ljava/lang/String;)V
Label11:
Label10:
Label4:
	fload_2
	fconst_1
	fadd
	fstore_2
	goto Label6
Label5:
	fstore_2
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method
