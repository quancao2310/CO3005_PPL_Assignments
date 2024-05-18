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
	ldc 7.0
	fstore_1
Label4:
	fload_1
	ldc 10.0
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
Label10:
	ldc "a > 10;"
	invokestatic io/writeString(Ljava/lang/String;)V
Label12:
	fload_1
	fconst_2
	fmul
	fstore_1
Label13:
Label11:
	goto Label8
Label9:
	fload_1
	ldc 10.0
	fcmpl
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	fload_1
	ldc 5.0
	fcmpl
	iflt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iand
	ifle Label19
Label20:
Label22:
	fload_1
	fconst_1
	fadd
	fstore_1
	ldc "5 <= a <= 10;"
	invokestatic io/writeString(Ljava/lang/String;)V
Label23:
	fload_1
	fconst_1
	fadd
	fstore_1
Label21:
	goto Label18
Label19:
Label24:
Label26:
	fload_1
	ldc 6.0
	fsub
	fstore_1
Label27:
	ldc "a < 5;"
	invokestatic io/writeString(Ljava/lang/String;)V
Label25:
Label18:
Label8:
	fload_1
	fconst_1
	fsub
	fstore_1
Label5:
	fload_1
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
