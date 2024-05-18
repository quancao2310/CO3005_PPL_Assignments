.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static x [[[F
.field static y [[F
.field static z [[F
.field static t [F
.field static u [F

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
.var 1 is w [[[[F from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	ldc 3.0
	f2i
	anewarray [[[F
	dup
	iconst_0
	getstatic ZCodeClass.x [[[F
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	anewarray [[F
	dup
	iconst_0
	getstatic ZCodeClass.y [[F
	aastore
	dup
	iconst_1
	getstatic ZCodeClass.z [[F
	aastore
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	anewarray [[F
	dup
	iconst_0
	ldc 4.0
	f2i
	anewarray [F
	dup
	iconst_0
	getstatic ZCodeClass.t [F
	aastore
	dup
	iconst_1
	getstatic ZCodeClass.t [F
	aastore
	dup
	iconst_2
	getstatic ZCodeClass.t [F
	aastore
	dup
	iconst_3
	getstatic ZCodeClass.t [F
	aastore
	aastore
	dup
	iconst_1
	ldc 4.0
	f2i
	anewarray [F
	dup
	iconst_0
	getstatic ZCodeClass.t [F
	aastore
	dup
	iconst_1
	getstatic ZCodeClass.t [F
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 100.0
	fastore
	dup
	iconst_1
	ldc 200.0
	fastore
	aastore
	dup
	iconst_3
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	getstatic ZCodeClass.u [F
	fconst_0
	f2i
	faload
	fastore
	dup
	iconst_1
	getstatic ZCodeClass.u [F
	fconst_1
	f2i
	faload
	fastore
	aastore
	aastore
	aastore
	astore_1
	aload_1
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	aaload
	fconst_0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	fconst_1
	f2i
	aaload
	fconst_1
	f2i
	aaload
	fconst_2
	f2i
	aaload
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	fconst_2
	f2i
	aaload
	fconst_1
	f2i
	aaload
	ldc 3.0
	f2i
	aaload
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 14
.limit locals 2
.end method

.method public static init()V
Label0:
Label2:
	fconst_2
	f2i
	anewarray [[F
	dup
	iconst_0
	ldc 4.0
	f2i
	anewarray [F
	dup
	iconst_0
	fconst_2
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
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 3.0
	fastore
	dup
	iconst_1
	ldc 4.0
	fastore
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 5.0
	fastore
	dup
	iconst_1
	ldc 6.0
	fastore
	aastore
	dup
	iconst_3
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 7.0
	fastore
	dup
	iconst_1
	ldc 8.0
	fastore
	aastore
	aastore
	dup
	iconst_1
	ldc 4.0
	f2i
	anewarray [F
	dup
	iconst_0
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 8.0
	fastore
	dup
	iconst_1
	ldc 7.0
	fastore
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 6.0
	fastore
	dup
	iconst_1
	ldc 5.0
	fastore
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 4.0
	fastore
	dup
	iconst_1
	ldc 3.0
	fastore
	aastore
	dup
	iconst_3
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	fconst_2
	fastore
	dup
	iconst_1
	fconst_1
	fastore
	aastore
	aastore
	putstatic ZCodeClass.x [[[F
	ldc 4.0
	f2i
	anewarray [F
	dup
	iconst_0
	fconst_2
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
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 3.0
	fastore
	dup
	iconst_1
	ldc 4.0
	fastore
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 5.0
	fastore
	dup
	iconst_1
	ldc 6.0
	fastore
	aastore
	dup
	iconst_3
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 7.0
	fastore
	dup
	iconst_1
	ldc 8.0
	fastore
	aastore
	putstatic ZCodeClass.y [[F
	ldc 4.0
	f2i
	anewarray [F
	dup
	iconst_0
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 8.0
	fastore
	dup
	iconst_1
	ldc 7.0
	fastore
	aastore
	dup
	iconst_1
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 6.0
	fastore
	dup
	iconst_1
	ldc 5.0
	fastore
	aastore
	dup
	iconst_2
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 4.0
	fastore
	dup
	iconst_1
	ldc 3.0
	fastore
	aastore
	dup
	iconst_3
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	fconst_2
	fastore
	dup
	iconst_1
	fconst_1
	fastore
	aastore
	putstatic ZCodeClass.z [[F
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 100.0
	fastore
	dup
	iconst_1
	ldc 200.0
	fastore
	putstatic ZCodeClass.t [F
	fconst_2
	f2i
	newarray float
	dup
	iconst_0
	ldc 300.0
	fastore
	dup
	iconst_1
	ldc 400.0
	fastore
	putstatic ZCodeClass.u [F
Label3:
Label1:
	return
.limit stack 10
.limit locals 0
.end method
