.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F

.method public static <clinit>()V
Label0:
Label2:
	ldc 100.0
	putstatic ZCodeClass.a F
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
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static a()Ljava/lang/String;
Label0:
	ldc "string"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
	invokestatic ZCodeClass/a()Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
