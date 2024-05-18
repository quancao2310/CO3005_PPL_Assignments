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
	ldc 4.0
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
	ifge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	fload_1
	ldc 5.0
	fsub
	fstore_1
	goto Label6
Label11:
	fload_1
	fconst_0
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label6
Label14:
	fload_1
	fconst_1
	fcmpl
	ifne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	fload_1
	fconst_2
	fadd
	fstore_1
	goto Label6
Label17:
	fload_1
	fconst_2
	fcmpl
	ifne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label8
	fload_1
	ldc 3.0
	fadd
	fstore_1
	goto Label6
Label8:
	fload_1
	ldc 5.0
	fmul
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
