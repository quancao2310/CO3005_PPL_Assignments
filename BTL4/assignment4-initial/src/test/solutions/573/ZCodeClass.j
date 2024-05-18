.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a Z

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
.var 1 is i F from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	fconst_0
	fstore_1
	fload_1
Label6:
	getstatic ZCodeClass.a Z
	ifgt Label5
Label7:
	fload_1
	invokestatic io/writeNumber(F)V
	fload_1
	ldc 10.0
	fcmpl
	ifle Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	putstatic ZCodeClass.a Z
Label8:
Label4:
	fload_1
	fconst_2
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static init()V
Label0:
Label2:
	iconst_0
	putstatic ZCodeClass.a Z
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
