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
.var 1 is x F from Label2 to Label3
Label2:
	ldc 23.0
	fstore_1
	fload_1
	invokestatic ZCodeClass/isPrime(F)Z
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
.limit stack 1
.limit locals 2
.end method

.method public static isPrime(F)Z
.var 0 is x F from Label0 to Label1
Label0:
.var 1 is i F from Label2 to Label3
Label2:
	fload_0
	fconst_1
	fcmpl
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	iconst_0
	ireturn
Label6:
	fconst_2
	fstore_1
	fload_1
Label9:
	fload_1
	fload_0
	fconst_2
	fdiv
	fcmpl
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label8
Label12:
	fload_0
	fload_1
	frem
	fconst_0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	iconst_0
	ireturn
Label16:
Label13:
Label7:
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label9
Label8:
	fstore_1
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 2
.end method
