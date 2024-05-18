.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F

.method public static <clinit>()V
Label0:
Label2:
	ldc 10.0
	putstatic ZCodeClass.a F
Label3:
Label1:
	return
.limit stack 1
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

.method public static foo()F
Label0:
Label2:
	getstatic ZCodeClass.a F
	fconst_1
	fsub
	putstatic ZCodeClass.a F
	getstatic ZCodeClass.a F
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b F from Label2 to Label3
Label2:
	fconst_0
	fstore_1
	fload_1
	fconst_0
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	invokestatic ZCodeClass/foo()F
	fstore_1
	goto Label6
Label7:
	fload_1
	fconst_0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	invokestatic ZCodeClass/foo()F
	fconst_1
	fadd
	fstore_1
	goto Label6
Label11:
	invokestatic ZCodeClass/foo()F
	ldc 7.0
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label8
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label6
Label8:
	fload_1
	fconst_2
	fadd
	fstore_1
Label6:
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
	fload_1
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
