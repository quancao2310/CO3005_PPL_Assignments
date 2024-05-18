.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a F
.field static b F
.field static c F
.field static d F
.field static e Ljava/lang/String;
.field static f Ljava/lang/String;

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
.var 1 is x1 Z from Label2 to Label3
.var 2 is x2 Z from Label2 to Label3
.var 3 is x3 Z from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a F
	getstatic ZCodeClass.b F
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_1
	getstatic ZCodeClass.c F
	getstatic ZCodeClass.d F
	fcmpl
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	istore_2
	getstatic ZCodeClass.e Ljava/lang/String;
	getstatic ZCodeClass.f Ljava/lang/String;
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	istore_3
	iload_1
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	iload_2
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	iload_3
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static init()V
Label0:
Label2:
	ldc 100.0
	putstatic ZCodeClass.a F
	ldc 200.0
	putstatic ZCodeClass.b F
	ldc 100.0
	putstatic ZCodeClass.c F
	ldc 100.0
	putstatic ZCodeClass.d F
	ldc "23"
	putstatic ZCodeClass.e Ljava/lang/String;
	ldc "23"
	putstatic ZCodeClass.f Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
