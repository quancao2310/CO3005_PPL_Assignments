.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static d F

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

.method public static foo(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
Label2:
	fload_0
	fload_1
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	ldc 123.0
	freturn
Label6:
	invokestatic ZCodeClass/bar()F
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static bar()F
Label0:
	getstatic ZCodeClass.d F
	freturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	invokestatic ZCodeClass/init()V
	ldc 120.0
	ldc 121.0
	invokestatic ZCodeClass/foo(FF)F
	invokestatic io/writeNumber(F)V
	invokestatic ZCodeClass/bar()F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static init()V
Label0:
Label2:
	ldc 1234000.0
	putstatic ZCodeClass.d F
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
