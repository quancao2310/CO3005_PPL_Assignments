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

.method public static partition([FFF)F
.var 0 is arr [F from Label0 to Label1
.var 1 is left F from Label0 to Label1
.var 2 is right F from Label0 to Label1
Label0:
.var 3 is pivot F from Label2 to Label3
.var 4 is i F from Label2 to Label3
.var 5 is j F from Label2 to Label3
.var 6 is saved_i F from Label2 to Label3
.var 7 is saved_j F from Label2 to Label3
Label2:
	aload_0
	fload_1
	f2i
	faload
	fstore_3
	fload_1
	fconst_1
	fadd
	fstore 4
	fload_2
	fstore 5
	fload 4
	fstore 6
	fload 5
	fstore 7
	fload 4
Label6:
	fload 4
	fload 5
	fcmpl
	ifle Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	fload 4
Label13:
	fload 4
	fload 5
	fcmpl
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	aload_0
	fload 4
	f2i
	faload
	fload_3
	fcmpl
	iflt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ior
	ifgt Label12
Label18:
	fload 4
	fconst_1
	fadd
	fstore 6
Label19:
Label11:
	fload 4
	fconst_1
	fadd
	fstore 4
	goto Label13
Label12:
	fstore 4
	fload 6
	fstore 4
	fload 5
Label22:
	fload 4
	fload 5
	fcmpl
	ifle Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	aload_0
	fload 5
	f2i
	faload
	fload_3
	fcmpl
	ifge Label25
	iconst_1
	goto Label26
Label25:
	iconst_0
Label26:
	ior
	ifgt Label21
Label27:
	fload 5
	fconst_1
	fsub
	fstore 7
Label28:
Label20:
	fload 5
	fconst_1
	fneg
	fadd
	fstore 5
	goto Label22
Label21:
	fstore 5
	fload 7
	fstore 5
	fload 4
	fload 5
	fcmpl
	ifge Label29
	iconst_1
	goto Label30
Label29:
	iconst_0
Label30:
	ifle Label31
Label32:
	aload_0
	fload 4
	fload 5
	invokestatic ZCodeClass/swap([FFF)V
	fload 4
	fconst_1
	fadd
	fstore 4
	fload 5
	fconst_1
	fsub
	fstore 5
Label33:
Label31:
Label10:
Label4:
	fload 4
	fconst_0
	fadd
	fstore 4
	goto Label6
Label5:
	fstore 4
	aload_0
	fload 5
	fload_1
	invokestatic ZCodeClass/swap([FFF)V
	fload 5
	freturn
Label3:
Label1:
.limit stack 5
.limit locals 8
.end method

.method public static quick_sort([FFF)V
.var 0 is arr [F from Label0 to Label1
.var 1 is left F from Label0 to Label1
.var 2 is right F from Label0 to Label1
Label0:
.var 3 is pos F from Label2 to Label3
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
	aload_0
	fload_1
	fload_2
	invokestatic ZCodeClass/partition([FFF)F
	fstore_3
	aload_0
	fload_1
	fload_3
	fconst_1
	fsub
	invokestatic ZCodeClass/quick_sort([FFF)V
	aload_0
	fload_3
	fconst_1
	fadd
	fload_2
	invokestatic ZCodeClass/quick_sort([FFF)V
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
	invokestatic ZCodeClass/quick_sort([FFF)V
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
