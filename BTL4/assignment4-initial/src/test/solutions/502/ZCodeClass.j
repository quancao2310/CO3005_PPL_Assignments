.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F
.field static b Ljava/lang/String;
.field static c Z

.method public static <clinit>()V
Label0:
Label2:
	fconst_0
	putstatic ZCodeClass.a F
	ldc ""
	putstatic ZCodeClass.b Ljava/lang/String;
	iconst_0
	putstatic ZCodeClass.c Z
	return
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LZCodeClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label2 to Label3
.var 2 is b Z from Label2 to Label3
.var 3 is c Ljava/lang/String; from Label2 to Label3
Label2:
	fconst_2
	fstore_1
	iconst_1
	istore_2
	ldc "ABC"
	astore_3
	fload_1
	invokestatic io/writeNumber(F)V
	iload_2
	invokestatic io/writeBool(Z)V
	aload_3
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 4
.end method
