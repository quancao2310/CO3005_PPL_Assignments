.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static abc F

.method public static <clinit>()V
Label0:
Label2:
	ldc 12300.0
	putstatic ZCodeClass.abc F
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

.method public static foo(Ljava/lang/String;)Z
.var 0 is abc Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	ldc "abc"
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc "abc"
	invokestatic ZCodeClass/foo(Ljava/lang/String;)Z
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
