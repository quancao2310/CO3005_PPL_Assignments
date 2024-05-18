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

.method public static foo(FZLjava/lang/String;)V
.var 0 is a F from Label0 to Label1
.var 1 is b Z from Label0 to Label1
.var 2 is c Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fload_0
	invokestatic io/writeNumber(F)V
	iload_1
	invokestatic io/writeBool(Z)V
	aload_2
	ldc "\n"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static bar(F)F
.var 0 is num F from Label0 to Label1
Label0:
	fload_0
	fconst_2
	fdiv
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fconst_1
	iconst_1
	ldc "a random string"
	invokestatic ZCodeClass/foo(FZLjava/lang/String;)V
	ldc 10.0
	invokestatic ZCodeClass/bar(F)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
