.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F
.field static b F
.field static c F
.field static d F
.field static e F
.field static f F

.method public static <clinit>()V
Label0:
Label2:
	return
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
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x1 F from Label2 to Label3
.var 2 is x2 F from Label2 to Label3
.var 3 is x3 F from Label2 to Label3
.var 4 is x4 F from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a F
	fneg
	fstore_1
	getstatic ZCodeClass.b F
	fneg
	fneg
	fstore_2
	getstatic ZCodeClass.c F
	fneg
	getstatic ZCodeClass.d F
	fadd
	fstore_3
	getstatic ZCodeClass.e F
	fneg
	getstatic ZCodeClass.f F
	fmul
	fstore 4
	fload_1
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload_2
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload_3
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	fload 4
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 5
.end method

.method public static init()V
Label0:
Label2:
	ldc 100.0
	putstatic ZCodeClass.a F
	fconst_1
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	putstatic ZCodeClass.b F
	getstatic ZCodeClass.a F
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	fneg
	putstatic ZCodeClass.c F
	fconst_1
	putstatic ZCodeClass.d F
	fconst_2
	putstatic ZCodeClass.e F
	ldc 3.0
	putstatic ZCodeClass.f F
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method