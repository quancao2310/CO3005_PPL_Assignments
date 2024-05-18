.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F

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
	getstatic ZCodeClass.a F
Label6:
	getstatic ZCodeClass.a F
	ldc 10.0
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
Label4:
	getstatic ZCodeClass.a F
	ldc 3.0
	fadd
	putstatic ZCodeClass.a F
	goto Label6
Label5:
	putstatic ZCodeClass.a F
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static init()V
Label0:
Label2:
	fconst_1
	putstatic ZCodeClass.a F
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
