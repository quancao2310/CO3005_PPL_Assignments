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
	ldc 200000.0
	putstatic ZCodeClass.a F
	ldc " Hello "
	putstatic ZCodeClass.b Ljava/lang/String;
	iconst_0
	putstatic ZCodeClass.c Z
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.b Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
	getstatic ZCodeClass.c Z
	invokestatic io/writeBool(Z)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 0.25
	putstatic ZCodeClass.a F
	ldc " ABC "
	putstatic ZCodeClass.b Ljava/lang/String;
	iconst_1
	putstatic ZCodeClass.c Z
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.b Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
	getstatic ZCodeClass.c Z
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
