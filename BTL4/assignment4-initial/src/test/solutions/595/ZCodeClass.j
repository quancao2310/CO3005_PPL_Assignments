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

.method public static round(F)F
.var 0 is n F from Label0 to Label1
Label0:
	fload_0
	fload_0
	fconst_1
	frem
	fsub
	freturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static merge([FFFF)V
.var 0 is arr [F from Label0 to Label1
.var 1 is left F from Label0 to Label1
.var 2 is right F from Label0 to Label1
.var 3 is mid F from Label0 to Label1
Label0:
.var 4 is left_length F from Label2 to Label3
.var 5 is right_length F from Label2 to Label3
.var 6 is arr_left [F from Label2 to Label3
.var 7 is arr_right [F from Label2 to Label3
.var 8 is i F from Label2 to Label3
.var 9 is j F from Label2 to Label3
.var 10 is k F from Label2 to Label3
Label2:
	fload_3
	fload_1
	fsub
	fconst_1
	fadd
	fstore 4
	fload_2
	fload_3
	fsub
	fstore 5
	ldc 10.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	dup
	iconst_4
	fconst_0
	fastore
	dup
	iconst_5
	fconst_0
	fastore
	dup
	bipush 6
	fconst_0
	fastore
	dup
	bipush 7
	fconst_0
	fastore
	dup
	bipush 8
	fconst_0
	fastore
	dup
	bipush 9
	fconst_0
	fastore
	astore 6
	ldc 10.0
	f2i
	newarray float
	dup
	iconst_0
	fconst_0
	fastore
	dup
	iconst_1
	fconst_0
	fastore
	dup
	iconst_2
	fconst_0
	fastore
	dup
	iconst_3
	fconst_0
	fastore
	dup
	iconst_4
	fconst_0
	fastore
	dup
	iconst_5
	fconst_0
	fastore
	dup
	bipush 6
	fconst_0
	fastore
	dup
	bipush 7
	fconst_0
	fastore
	dup
	bipush 8
	fconst_0
	fastore
	dup
	bipush 9
	fconst_0
	fastore
	astore 7
	fconst_0
	fstore 8
	fconst_0
	fstore 9
	fload 8
Label6:
	fload 8
	fload 4
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
	aload 6
	fload 8
	f2i
	aload_0
	fload_1
	fload 8
	fadd
	f2i
	faload
	fastore
Label4:
	fload 8
	fconst_1
	fadd
	fstore 8
	goto Label6
Label5:
	fstore 8
	fload 9
Label11:
	fload 9
	fload 5
	fcmpl
	iflt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label10
	aload 7
	fload 9
	f2i
	aload_0
	fload_3
	fconst_1
	fadd
	fload 9
	fadd
	f2i
	faload
	fastore
Label9:
	fload 9
	fconst_1
	fadd
	fstore 9
	goto Label11
Label10:
	fstore 9
	fload_1
	fstore 10
	fload 10
Label16:
	fload 10
	fload_2
	fcmpl
	ifle Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifgt Label15
Label19:
	fload 8
	fload 4
	fcmpl
	ifge Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	fload 9
	fload 5
	fcmpl
	iflt Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	aload 6
	fload 8
	f2i
	faload
	aload 7
	fload 9
	f2i
	faload
	fcmpl
	ifgt Label25
	iconst_1
	goto Label26
Label25:
	iconst_0
Label26:
	ior
	iand
	ifle Label28
Label29:
	aload_0
	fload 10
	f2i
	aload 6
	fload 8
	f2i
	faload
	fastore
	fload 8
	fconst_1
	fadd
	fstore 8
Label30:
	goto Label27
Label28:
Label31:
	aload_0
	fload 10
	f2i
	aload 7
	fload 9
	f2i
	faload
	fastore
	fload 9
	fconst_1
	fadd
	fstore 9
Label32:
Label27:
Label20:
Label14:
	fload 10
	fconst_1
	fadd
	fstore 10
	goto Label16
Label15:
	fstore 10
Label3:
Label1:
	return
.limit stack 6
.limit locals 11
.end method

.method public static merge_sort([FFF)V
.var 0 is arr [F from Label0 to Label1
.var 1 is left F from Label0 to Label1
.var 2 is right F from Label0 to Label1
Label0:
.var 3 is mid F from Label2 to Label3
Label2:
	fload_1
	fload_2
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	return
Label6:
	fload_1
	fload_2
	fadd
	fconst_2
	fdiv
	invokestatic ZCodeClass/round(F)F
	fstore_3
	aload_0
	fload_1
	fload_3
	invokestatic ZCodeClass/merge_sort([FFF)V
	aload_0
	fload_3
	fconst_1
	fadd
	fload_2
	invokestatic ZCodeClass/merge_sort([FFF)V
	aload_0
	fload_1
	fload_2
	fload_3
	invokestatic ZCodeClass/merge([FFFF)V
Label3:
Label1:
	return
.limit stack 4
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
	fconst_0
	ldc 9.0
	invokestatic ZCodeClass/merge_sort([FFF)V
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
