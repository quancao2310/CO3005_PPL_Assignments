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
Label2:
	ldc 10.0
	ldc 20.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/writeBool(Z)V
	ldc 20.0
	ldc 20.0
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/writeBool(Z)V
	ldc 10.0
	ldc 20.0
	fcmpl
	ifeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/writeBool(Z)V
	ldc 20.0
	ldc 20.0
	fcmpl
	ifeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 10.0
	ldc 20.0
	fcmpl
	ifge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/writeBool(Z)V
	ldc 10.0
	ldc 20.0
	fcmpl
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/writeBool(Z)V
	ldc 20.0
	ldc 20.0
	fcmpl
	ifle Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	invokestatic io/writeBool(Z)V
	ldc 10.0
	ldc 20.0
	fcmpl
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	invokestatic io/writeBool(Z)V
	ldc 20.0
	ldc 20.0
	fcmpl
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	invokestatic io/writeBool(Z)V
	ldc 10.0
	ldc 20.0
	fcmpl
	iflt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/writeBool(Z)V
	ldc 20.0
	ldc 20.0
	fcmpl
	iflt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc ""
	ldc ""
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	invokestatic io/writeBool(Z)V
	ldc "abc"
	ldc "abc"
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	invokestatic io/writeBool(Z)V
	ldc "abc"
	ldc "abd"
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	invokestatic io/writeBool(Z)V
	ldc "123\'456"
	ldc "123'456"
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
