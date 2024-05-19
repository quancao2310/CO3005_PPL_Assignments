.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

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

.method public static swap([FFF)V
.var 0 is arr [F from Label0 to Label1
.var 1 is i F from Label0 to Label1
.var 2 is j F from Label0 to Label1
Label0:
.var 3 is tmp F from Label2 to Label3
Label2:
	fload_1
	fconst_0
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	fload_1
	ldc 10.0
	fcmpl
	iflt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	fload_2
	fconst_0
	fcmpl
	ifge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	fload_2
	ldc 10.0
	fcmpl
	iflt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	fload_1
	fload_2
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ior
	ifle Label14
	return
Label14:
	aload_0
	fload_1
	f2i
	faload
	fstore_3
	aload_0
	fload_1
	f2i
	aload_0
	fload_2
	f2i
	faload
	fastore
	aload_0
	fload_2
	f2i
	fload_3
	fastore
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public static selection_sort([F)V
.var 0 is arr [F from Label0 to Label1
Label0:
.var 1 is i F from Label2 to Label3
Label2:
	fconst_0
	fstore_1
	fload_1
Label6:
	fload_1
	ldc 9.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
.var 2 is min_idx F from Label9 to Label10
.var 3 is j F from Label9 to Label10
Label9:
	fload_1
	fstore_2
	fload_1
	fconst_1
	fadd
	fstore_3
	fload_3
Label13:
	fload_3
	ldc 10.0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label12
	aload_0
	fload_3
	f2i
	faload
	aload_0
	fload_2
	f2i
	faload
	fcmpl
	ifge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	fload_3
	fstore_2
Label18:
Label11:
	fload_3
	fconst_1
	fadd
	fstore_3
	goto Label13
Label12:
	fstore_3
	aload_0
	fload_1
	fload_2
	invokestatic ZCodeClass/swap([FFF)V
Label10:
Label4:
	fload_1
	fconst_1
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
Label3:
Label1:
	return
.limit stack 5
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [F from Label2 to Label3
.var 2 is i F from Label2 to Label3
Label2:
	ldc 10.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 5.71
	fastore
	dup
	iconst_1
	ldc 1.69
	fastore
	dup
	iconst_2
	ldc 3.49
	fastore
	dup
	iconst_3
	ldc 2.65
	fastore
	dup
	iconst_4
	ldc 4.28
	fastore
	dup
	iconst_5
	ldc 7.84
	fastore
	dup
	bipush 6
	ldc 1.49
	fastore
	dup
	bipush 7
	ldc 5.52
	fastore
	dup
	bipush 8
	ldc 2.48
	fastore
	dup
	bipush 9
	ldc 7.87
	fastore
	astore_1
	aload_1
	invokestatic ZCodeClass/selection_sort([F)V
	aload_1
	fconst_0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	fconst_1
	fstore_2
	fload_2
Label6:
	fload_2
	ldc 10.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	aload_1
	fload_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label10:
Label4:
	fload_2
	fconst_1
	fadd
	fstore_2
	goto Label6
Label5:
	fstore_2
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method
