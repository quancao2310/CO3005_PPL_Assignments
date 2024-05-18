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

.method public static foo()F
Label0:
	ldc 123.0
	freturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static bar(FFLjava/lang/String;)V
.var 0 is foo F from Label0 to Label1
.var 1 is bar F from Label0 to Label1
.var 2 is main Ljava/lang/String; from Label0 to Label1
Label0:
.var 3 is x F from Label2 to Label3
Label2:
	fload_1
	fload_0
	fadd
	fstore_3
	fload_3
	invokestatic io/writeNumber(F)V
	aload_2
	invokestatic io/writeString(Ljava/lang/String;)V
	invokestatic ZCodeClass/foo()F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc 321.0
	ldc 123.0
	ldc "main"
	invokestatic ZCodeClass/bar(FFLjava/lang/String;)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
