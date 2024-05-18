.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F
.field static b Z
.field static c Ljava/lang/String;
.field static d F

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

.method public static foo(FZLjava/lang/String;F)V
.var 0 is a F from Label0 to Label1
.var 1 is b Z from Label0 to Label1
.var 2 is c Ljava/lang/String; from Label0 to Label1
.var 3 is d F from Label0 to Label1
Label0:
Label2:
	fload_0
	fload_3
	fsub
	invokestatic io/writeNumber(F)V
	iload_1
	aload_2
	ldc "abc"
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	iand
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static inc(F)F
.var 0 is a F from Label0 to Label1
Label0:
	fload_0
	fconst_1
	fadd
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a F
	getstatic ZCodeClass.b Z
	getstatic ZCodeClass.c Ljava/lang/String;
	getstatic ZCodeClass.d F
	invokestatic ZCodeClass/inc(F)F
	invokestatic ZCodeClass/foo(FZLjava/lang/String;F)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static init()V
Label0:
Label2:
	fconst_1
	putstatic ZCodeClass.a F
	iconst_1
	putstatic ZCodeClass.b Z
	ldc "abc"
	putstatic ZCodeClass.c Ljava/lang/String;
	ldc 10.0
	putstatic ZCodeClass.d F
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
