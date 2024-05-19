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

.method public static areDivisors(FF)Z
.var 0 is num1 F from Label0 to Label1
.var 1 is num2 F from Label0 to Label1
Label0:
	fload_0
	fload_1
	frem
	fconst_0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_1
	fload_0
	frem
	fconst_0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is num1 F from Label2 to Label3
.var 2 is num2 F from Label2 to Label3
Label2:
	ldc 2024.0
	fstore_1
	ldc 8.0
	fstore_2
	fload_1
	fload_2
	invokestatic ZCodeClass/areDivisors(FF)Z
	ifle Label5
	ldc "Yes"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label4
Label5:
	ldc "No"
	invokestatic io/writeString(Ljava/lang/String;)V
Label4:
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method
