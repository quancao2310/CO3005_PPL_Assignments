.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

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

.method public static foo(FZ)V
.var 0 is x F from Label0 to Label1
.var 1 is y Z from Label0 to Label1
Label0:
.var 2 is x Ljava/lang/String; from Label2 to Label3
.var 3 is y Z from Label2 to Label3
Label2:
	ldc "str "
	astore_2
	iconst_1
	istore_3
	aload_2
	invokestatic io/writeString(Ljava/lang/String;)V
	iload_3
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fconst_1
	iconst_0
	invokestatic ZCodeClass/foo(FZ)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
