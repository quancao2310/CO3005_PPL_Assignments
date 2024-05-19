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

.method public static xor(ZZ)Z
.var 0 is a Z from Label0 to Label1
.var 1 is b Z from Label0 to Label1
Label0:
	iload_0
	iload_1
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iand
	iload_0
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_1
	iand
	ior
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_1
	iconst_1
	invokestatic ZCodeClass/xor(ZZ)Z
	invokestatic io/writeBool(Z)V
	iconst_1
	iconst_0
	invokestatic ZCodeClass/xor(ZZ)Z
	invokestatic io/writeBool(Z)V
	iconst_0
	iconst_1
	invokestatic ZCodeClass/xor(ZZ)Z
	invokestatic io/writeBool(Z)V
	iconst_0
	iconst_0
	invokestatic ZCodeClass/xor(ZZ)Z
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
