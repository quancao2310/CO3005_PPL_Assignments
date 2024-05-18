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
	fconst_0
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
Label8:
	fload_1
	ldc 10.0
	fcmpl
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label13
Label14:
	ldc "a > 10"
	invokestatic io/writeString(Ljava/lang/String;)V
Label15:
	goto Label12
Label13:
	fload_1
	ldc 5.0
	fcmpl
	ifle Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	fload_1
	ldc 10.0
	fcmpl
	ifgt Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	iand
	ifle Label16
Label22:
	ldc "5 < a <= 10"
	invokestatic io/writeString(Ljava/lang/String;)V
Label23:
	goto Label12
Label16:
Label24:
	ldc "0 < a <= 5"
	invokestatic io/writeString(Ljava/lang/String;)V
Label25:
Label12:
Label9:
	goto Label6
Label7:
Label26:
	fload_1
	fconst_0
	fcmpl
	ifne Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label31
Label32:
	ldc "a = 0"
	invokestatic io/writeString(Ljava/lang/String;)V
Label33:
	goto Label30
Label31:
	ldc "a < 0"
	invokestatic io/writeString(Ljava/lang/String;)V
Label30:
Label27:
Label6:
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
