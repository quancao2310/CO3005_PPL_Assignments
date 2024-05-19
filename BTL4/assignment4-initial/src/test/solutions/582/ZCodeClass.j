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

.method public static gcd(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
Label2:
	fload_1
	fconst_0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	fload_0
	freturn
Label6:
	fload_1
	fload_0
	fload_1
	frem
	invokestatic ZCodeClass/gcd(FF)F
	freturn
Label3:
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc 6.0
	ldc 9.0
	invokestatic ZCodeClass/gcd(FF)F
	invokestatic io/writeNumber(F)V
	ldc 24.0
	ldc 16.0
	invokestatic ZCodeClass/gcd(FF)F
	invokestatic io/writeNumber(F)V
	fconst_1
	ldc 7.0
	invokestatic ZCodeClass/gcd(FF)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
