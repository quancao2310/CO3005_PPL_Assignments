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
.var 1 is a F from Label2 to Label3
.var 2 is b Ljava/lang/String; from Label2 to Label3
Label2:
	ldc 100.0
	fstore_1
.var 2 is a F from Label4 to Label5
Label4:
	ldc 200.0
	fstore_2
	fload_2
	invokestatic io/writeNumber(F)V
Label5:
	ldc " false"
	astore_2
	fload_1
	invokestatic io/writeNumber(F)V
	aload_2
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 3
.end method
