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
Label2:
	fconst_1
	fstore_1
	fload_1
	ldc 5.0
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	fload_1
	ldc 5.0
	fadd
	fstore_1
	goto Label6
Label7:
	fload_1
	fconst_0
	fcmpl
	ifge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	fload_1
	ldc 5.0
	fsub
	fstore_1
	goto Label6
Label10:
	fload_1
	fconst_0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label6
Label13:
	fload_1
	fconst_1
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	fload_1
	fconst_2
	fadd
	fstore_1
	goto Label6
Label16:
	fload_1
	fconst_2
	fcmpl
	ifne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label6
	fload_1
	ldc 3.0
	fsub
	fstore_1
Label6:
	fload_1
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
