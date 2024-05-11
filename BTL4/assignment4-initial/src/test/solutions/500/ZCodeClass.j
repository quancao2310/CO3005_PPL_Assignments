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
	ldc 5.0
	putstatic ZCodeClass.a F
	ldc "hello"
	putstatic ZCodeClass.b Ljava/lang/String;
	iconst_1
	putstatic ZCodeClass.c Z
	getstatic ZCodeClass.a F
	putstatic ZCodeClass.d F
	return
Label1:
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
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic ZCodeClass.d F
	putstatic ZCodeClass.e F
	getstatic ZCodeClass.e F
	invokestatic io/writeNumber(F)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
