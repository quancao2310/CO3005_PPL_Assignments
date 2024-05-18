.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a [[Z

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
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a [[Z
	fconst_1
	f2i
	aaload
	fconst_2
	f2i
	baload
	ifle Label5
	ldc "true"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label4
Label5:
	ldc "false"
	invokestatic io/writeString(Ljava/lang/String;)V
Label4:
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static init()V
Label0:
Label2:
	ldc 3.0
	f2i
	anewarray [Z
	dup
	iconst_0
	ldc 3.0
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	dup
	iconst_1
	ldc 3.0
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	aastore
	dup
	iconst_2
	ldc 3.0
	f2i
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	aastore
	putstatic ZCodeClass.a [[Z
Label3:
Label1:
	return
.limit stack 7
.limit locals 0
.end method
