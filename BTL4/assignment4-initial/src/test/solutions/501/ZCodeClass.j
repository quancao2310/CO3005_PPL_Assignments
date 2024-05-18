.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F
.field static b Z
.field static c Ljava/lang/String;
.field static d F
.field static e Ljava/lang/String;
.field static f Z

.method public static <clinit>()V
Label0:
Label2:
	fconst_1
	putstatic ZCodeClass.a F
	iconst_1
	putstatic ZCodeClass.b Z
	ldc "ABC"
	putstatic ZCodeClass.c Ljava/lang/String;
	fconst_0
	putstatic ZCodeClass.d F
	ldc ""
	putstatic ZCodeClass.e Ljava/lang/String;
	iconst_0
	putstatic ZCodeClass.f Z
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.b Z
	invokestatic io/writeBool(Z)V
	getstatic ZCodeClass.c Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
