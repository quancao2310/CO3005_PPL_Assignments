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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label2 to Label3
.var 2 is b F from Label2 to Label3
.var 3 is c F from Label2 to Label3
.var 4 is d F from Label2 to Label3
.var 5 is e F from Label2 to Label3
.var 6 is f F from Label2 to Label3
.var 7 is g F from Label2 to Label3
.var 8 is h F from Label2 to Label3
Label2:
	ldc 47.25
	fstore_1
	ldc 10.5
	fstore_2
	fload_1
	fload_2
	fadd
	fstore_3
	fload_1
	fload_2
	fsub
	fstore 4
	fload_1
	fneg
	fload_2
	fadd
	fstore 5
	fload_1
	fneg
	fload_2
	fneg
	fmul
	fstore 6
	fload_1
	fload_2
	fdiv
	fstore 7
	fload_1
	fload_2
	frem
	fstore 8
	fload_3
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload 4
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload 5
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload 6
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload 7
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload 8
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 9
.end method
