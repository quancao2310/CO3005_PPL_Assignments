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

.method public static foo()Ljava/lang/String;
Label0:
	ldc "Hello"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static bar()V
Label0:
.var 0 is a F from Label2 to Label3
.var 1 is b F from Label2 to Label3
Label2:
	fconst_1
	fstore_0
Label3:
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic ZCodeClass/bar()V
	invokestatic ZCodeClass/foo()Ljava/lang/String;
	astore_1
	aload_1
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 2
.end method
