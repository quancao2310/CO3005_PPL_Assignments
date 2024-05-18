.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static arr [F

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

.method public static pushIndices()V
Label0:
Label2:
	getstatic ZCodeClass.arr [F
	fconst_1
	fconst_2
	ldc 3.0
	ldc 4.0
	ldc 5.0
	ldc 6.0
	ldc 7.0
	ldc 8.0
	ldc 9.0
	invokestatic ZCodeClass/bar(FFFFFFFFF)F
	f2i
	ldc 10.0
	ldc 10.0
	fmul
	fastore
Label3:
Label1:
	return
.limit stack 10
.limit locals 0
.end method

.method public static pushRhs()V
Label0:
Label2:
	getstatic ZCodeClass.arr [F
	ldc 9.0
	f2i
	getstatic ZCodeClass.arr [F
	fconst_1
	fconst_2
	ldc 3.0
	ldc 4.0
	ldc 5.0
	ldc 6.0
	ldc 7.0
	ldc 8.0
	ldc 9.0
	invokestatic ZCodeClass/bar(FFFFFFFFF)F
	f2i
	faload
	ldc 10.0
	fsub
	fastore
Label3:
Label1:
	return
.limit stack 12
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc 10.0
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
	dup
	iconst_5
	ldc 6.0
	fastore
	dup
	bipush 6
	ldc 7.0
	fastore
	dup
	bipush 7
	ldc 8.0
	fastore
	dup
	bipush 8
	ldc 9.0
	fastore
	dup
	bipush 9
	ldc 10.0
	fastore
	putstatic ZCodeClass.arr [F
	invokestatic ZCodeClass/pushIndices()V
	invokestatic ZCodeClass/pushRhs()V
	getstatic ZCodeClass.arr [F
	fconst_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.arr [F
	ldc 9.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static bar(FFFFFFFFF)F
.var 0 is x1 F from Label0 to Label1
.var 1 is x2 F from Label0 to Label1
.var 2 is x3 F from Label0 to Label1
.var 3 is x4 F from Label0 to Label1
.var 4 is x5 F from Label0 to Label1
.var 5 is x6 F from Label0 to Label1
.var 6 is x7 F from Label0 to Label1
.var 7 is x8 F from Label0 to Label1
.var 8 is x9 F from Label0 to Label1
Label0:
	fconst_1
	freturn
Label1:
.limit stack 1
.limit locals 9
.end method
