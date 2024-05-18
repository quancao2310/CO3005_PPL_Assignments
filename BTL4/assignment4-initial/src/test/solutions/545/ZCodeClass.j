.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a [F
.field static b [[Z
.field static c [[Ljava/lang/String;
.field static i F
.field static j F
.field static k F

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
.var 2 is x2 Z from Label2 to Label3
.var 3 is x3 Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a [F
	getstatic ZCodeClass.i F
	f2i
	faload
	fstore_1
	getstatic ZCodeClass.b [[Z
	getstatic ZCodeClass.i F
	f2i
	aaload
	getstatic ZCodeClass.j F
	f2i
	baload
	istore_2
	getstatic ZCodeClass.c [[Ljava/lang/String;
	getstatic ZCodeClass.j F
	f2i
	aaload
	getstatic ZCodeClass.i F
	f2i
	aaload
	astore_3
	fload_1
	invokestatic io/writeNumber(F)V
	iload_2
	invokestatic io/writeBool(Z)V
	aload_3
	invokestatic io/writeString(Ljava/lang/String;)V
	getstatic ZCodeClass.a [F
	getstatic ZCodeClass.k F
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static init()V
Label0:
Label2:
	ldc 5.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 5.0
	fastore
	dup
	iconst_1
	ldc 4.0
	fastore
	dup
	iconst_2
	ldc 3.0
	fastore
	dup
	iconst_3
	fconst_2
	fastore
	dup
	iconst_4
	fconst_1
	fastore
	putstatic ZCodeClass.a [F
	fconst_2
	f2i
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	fconst_2
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "PPL"
	aastore
	dup
	iconst_1
	ldc "is"
	aastore
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "very"
	aastore
	dup
	iconst_1
	ldc "hard"
	aastore
	aastore
	putstatic ZCodeClass.c [[Ljava/lang/String;
	ldc 3.0
	f2i
	anewarray [Z
	dup
	iconst_0
	fconst_2
	f2i
	newarray boolean
	dup
	iconst_0
	getstatic ZCodeClass.a [F
	fconst_0
	f2i
	faload
	getstatic ZCodeClass.a [F
	fconst_1
	f2i
	faload
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	bastore
	dup
	iconst_1
	getstatic ZCodeClass.c [[Ljava/lang/String;
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	ldc "PPL"
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	bastore
	aastore
	dup
	iconst_1
	fconst_2
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
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray boolean
	dup
	iconst_0
	fconst_2
	fconst_2
	fcmpl
	ifne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	bastore
	dup
	iconst_1
	fconst_1
	ldc 3.0
	fcmpl
	ifeq Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	bastore
	aastore
	putstatic ZCodeClass.b [[Z
	fconst_0
	putstatic ZCodeClass.i F
	fconst_1
	putstatic ZCodeClass.j F
	fconst_2
	putstatic ZCodeClass.k F
Label3:
Label1:
	return
.limit stack 9
.limit locals 0
.end method
