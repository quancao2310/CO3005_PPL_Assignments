.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F

.method public static <clinit>()V
Label0:
Label2:
	ldc 6.0
	putstatic ZCodeClass.a F
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b F from Label2 to Label3
Label2:
	ldc 7.0
	fstore_1
Label4:
	ldc 8.0
	putstatic ZCodeClass.a F
Label6:
	ldc 9.0
	fstore_1
	getstatic ZCodeClass.a F
	fload_1
	fadd
	invokestatic io/writeNumber(F)V
Label7:
	getstatic ZCodeClass.a F
	fload_1
	fadd
	invokestatic io/writeNumber(F)V
Label5:
	getstatic ZCodeClass.a F
	fload_1
	fadd
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
