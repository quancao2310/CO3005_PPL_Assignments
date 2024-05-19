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

.method public static lis([FF)F
.var 0 is arr [F from Label0 to Label1
.var 1 is n F from Label0 to Label1
Label0:
.var 2 is lis [F from Label2 to Label3
.var 3 is i F from Label2 to Label3
.var 4 is max F from Label2 to Label3
Label2:
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
	astore_2
	aload_2
	fconst_0
	f2i
	fconst_1
	fastore
	fconst_1
	fstore_3
	fload_3
Label6:
	fload_3
	fload_1
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
.var 4 is j F from Label9 to Label10
Label9:
	aload_2
	fload_3
	f2i
	fconst_1
	fastore
	fconst_0
	fstore 4
	fload 4
Label13:
	fload 4
	fload_3
	fcmpl
	iflt Label14
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
	fload 4
	f2i
	faload
	fcmpl
	ifle Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	aload_2
	fload 4
	f2i
	faload
	fconst_1
	fadd
	aload_2
	fload_3
	f2i
	faload
	fcmpl
	ifle Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	iand
	ifle Label20
	aload_2
	fload_3
	f2i
	aload_2
	fload 4
	f2i
	faload
	fconst_1
	fadd
	fastore
Label20:
Label11:
	fload 4
	fconst_1
	fadd
	fstore 4
	goto Label13
Label12:
	fstore 4
Label10:
Label4:
	fload_3
	fconst_1
	fadd
	fstore_3
	goto Label6
Label5:
	fstore_3
	aload_2
	fconst_0
	f2i
	faload
	fstore 4
	fload_3
Label23:
	fload_3
	fload_1
	fcmpl
	iflt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label22
	aload_2
	fload_3
	f2i
	faload
	fload 4
	fcmpl
	ifle Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label28
	aload_2
	fload_3
	f2i
	faload
	fstore 4
Label28:
Label21:
	fload_3
	fconst_1
	fadd
	fstore_3
	goto Label23
Label22:
	fstore_3
	fload 4
	freturn
Label3:
Label1:
.limit stack 6
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [F from Label2 to Label3
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
	ldc 10.0
	invokestatic ZCodeClass/lis([FF)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 2
.end method
