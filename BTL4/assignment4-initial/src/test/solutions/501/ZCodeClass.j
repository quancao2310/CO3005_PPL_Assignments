.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a [F
.field static b [F
.field static c F

.method public static <clinit>()V
Label0:
Label2:
	ldc 5.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_1
	fastore
	dup
	iconst_1
	fconst_2
	fastore
	dup
	iconst_2
	ldc 3.0
	fastore
	dup
	iconst_3
	ldc 4.0
	fastore
	dup
	iconst_4
	ldc 5.0
	fastore
	putstatic ZCodeClass.a [F
	getstatic ZCodeClass.a [F
	putstatic ZCodeClass.b [F
	return
Label3:
Label1:
	return
.limit stack 9
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
Label2:
	invokestatic io/readNumber()F
	putstatic ZCodeClass.c F
	getstatic ZCodeClass.c F
	fconst_0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	getstatic ZCodeClass.a [F
	fconst_0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	goto Label6
Label7:
	getstatic ZCodeClass.c F
	fconst_1
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	getstatic ZCodeClass.a [F
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	goto Label6
Label11:
	getstatic ZCodeClass.c F
	fconst_2
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label8
	getstatic ZCodeClass.a [F
	fconst_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
	goto Label6
Label8:
	getstatic ZCodeClass.a [F
	ldc 3.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label6:
Label3:
Label1:
	return
.limit stack 6
.limit locals 1
.end method
