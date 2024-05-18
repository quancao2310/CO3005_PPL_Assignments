.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a Z

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
	getstatic ZCodeClass.a Z
	ifle Label5
Label6:
	ldc "true"
	invokestatic io/writeString(Ljava/lang/String;)V
Label7:
	goto Label4
Label5:
Label8:
	ldc "false"
	invokestatic io/writeString(Ljava/lang/String;)V
Label9:
Label4:
	invokestatic ZCodeClass/a()Z
	ifle Label11
	ldc "true"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label10
Label11:
	ldc "false"
	invokestatic io/writeString(Ljava/lang/String;)V
Label10:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static a()Z
Label0:
	iconst_0
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static init()V
Label0:
Label2:
	iconst_1
	putstatic ZCodeClass.a Z
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
