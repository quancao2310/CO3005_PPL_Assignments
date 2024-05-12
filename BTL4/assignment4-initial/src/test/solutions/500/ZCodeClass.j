.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F
.field static b Ljava/lang/String;
.field static c Z
.field static d F
.field static e F

.method public static <clinit>()V
Label0:
Label2:
	ldc 16.0
	putstatic ZCodeClass.a F
	ldc "hello"
	putstatic ZCodeClass.b Ljava/lang/String;
	iconst_1
	putstatic ZCodeClass.c Z
	getstatic ZCodeClass.a F
	putstatic ZCodeClass.d F
	return
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
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(ZLjava/lang/String;F)F
.var 0 is g Z from Label0 to Label1
.var 1 is a Ljava/lang/String; from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
.var 3 is f Z from Label2 to Label3
.var 4 is e F from Label2 to Label3
Label2:
	iconst_0
	istore_3
	getstatic ZCodeClass.d F
	freturn
Label3:
Label1:
.limit stack 1
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is g F from Label2 to Label3
Label2:
.var 1 is b F from Label4 to Label5
.var 2 is c F from Label4 to Label5
Label4:
	fconst_0
	fstore_1
	fconst_0
	fstore_2
Label5:
	getstatic ZCodeClass.d F
	putstatic ZCodeClass.e F
	getstatic ZCodeClass.e F
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 3
.end method
