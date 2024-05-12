.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

.method public static <clinit>()V
Label0:
Label2:
	return
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
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc 10.0
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 123.456
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	iconst_1
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	iconst_0
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc "Hello\"World"
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
