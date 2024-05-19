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

.method public static sort_segment([FFF)V
.var 0 is arr [F from Label0 to Label1
.var 1 is segment_idx F from Label0 to Label1
.var 2 is k F from Label0 to Label1
Label0:
.var 3 is i F from Label2 to Label3
Label2:
	fload_1
	fload_2
	fadd
	fstore_3
	fload_3
Label6:
	fload_3
	ldc 10.0
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
.var 4 is tmp F from Label9 to Label10
.var 5 is j F from Label9 to Label10
Label9:
	aload_0
	fload_3
	f2i
	faload
	fstore 4
	fload_3
	fload_2
	fsub
	fstore 5
	fload 5
Label13:
	fload 5
	fload_2
	fneg
	fcmpl
	ifge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label12
Label16:
	fload 5
	fconst_0
	fcmpl
	ifge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label21
Label22:
	aload_0
	fload 5
	fload_2
	fadd
	f2i
	fload 4
	fastore
	goto Label12
Label23:
	goto Label20
Label21:
	fload 4
	aload_0
	fload 5
	f2i
	faload
	fcmpl
	iflt Label25
	iconst_1
	goto Label26
Label25:
	iconst_0
Label26:
	ifle Label24
Label28:
	aload_0
	fload 5
	fload_2
	fadd
	f2i
	fload 4
	fastore
	goto Label12
Label29:
	goto Label20
Label24:
	aload_0
	fload 5
	fload_2
	fadd
	f2i
	aload_0
	fload 5
	f2i
	faload
	fastore
Label20:
Label17:
Label11:
	fload 5
	fload_2
	fneg
	fadd
	fstore 5
	goto Label13
Label12:
	fstore 5
Label10:
Label4:
	fload_3
	fload_2
	fadd
	fstore_3
	goto Label6
Label5:
	fstore_3
Label3:
Label1:
	return
.limit stack 6
.limit locals 6
.end method

.method public static shell_sort([F[F)V
.var 0 is arr [F from Label0 to Label1
.var 1 is num_of_segment_list [F from Label0 to Label1
Label0:
.var 2 is i F from Label2 to Label3
Label2:
	fconst_2
	fstore_2
	fload_2
Label6:
	fload_2
	fconst_0
	fcmpl
	ifge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
.var 3 is segment F from Label9 to Label10
Label9:
	fconst_0
	fstore_3
	fload_3
Label13:
	fload_3
	aload_1
	fload_2
	f2i
	faload
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
	aload_1
	fload_2
	f2i
	faload
	invokestatic ZCodeClass/sort_segment([FFF)V
Label11:
	fload_3
	fconst_1
	fadd
	fstore_3
	goto Label13
Label12:
	fstore_3
Label10:
Label4:
	fload_2
	fconst_1
	fneg
	fadd
	fstore_2
	goto Label6
Label5:
	fstore_2
Label3:
Label1:
	return
.limit stack 6
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
	ldc 3.0
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
	ldc 4.0
	fastore
	invokestatic ZCodeClass/shell_sort([F[F)V
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
.limit stack 5
.limit locals 3
.end method
