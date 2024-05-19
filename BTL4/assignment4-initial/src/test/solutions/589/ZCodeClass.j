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

.method public static binary_search([FF)F
.var 0 is arr [F from Label0 to Label1
.var 1 is element F from Label0 to Label1
Label0:
.var 2 is left F from Label2 to Label3
.var 3 is right F from Label2 to Label3
.var 4 is mid F from Label2 to Label3
.var 5 is _ F from Label2 to Label3
Label2:
	fconst_0
	fstore_2
	ldc 9.0
	fstore_3
	fconst_0
	fstore 4
	fconst_0
	fstore 5
	fload 5
Label6:
	fload_2
	fload_3
	fcmpl
	ifle Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	fload_2
	fload_3
	fadd
	fconst_2
	fdiv
	invokestatic ZCodeClass/round(F)F
	fstore 4
	fload_1
	aload_0
	fload 4
	f2i
	faload
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label14
	fload 4
	freturn
	goto Label13
Label14:
	fload_1
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
	ifle Label15
	fload 4
	fconst_1
	fadd
	fstore_2
	goto Label13
Label15:
	fload 4
	fconst_1
	fsub
	fstore_3
Label13:
Label10:
Label4:
	fload 5
	fconst_0
	fadd
	fstore 5
	goto Label6
Label5:
	fstore 5
	fconst_1
	fneg
	freturn
Label3:
Label1:
.limit stack 4
.limit locals 6
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [F from Label2 to Label3
.var 2 is element F from Label2 to Label3
.var 3 is pos F from Label2 to Label3
Label2:
	ldc 10.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 1.49
	fastore
	dup
	iconst_1
	ldc 1.69
	fastore
	dup
	iconst_2
	ldc 2.48
	fastore
	dup
	iconst_3
	ldc 2.65
	fastore
	dup
	iconst_4
	ldc 3.49
	fastore
	dup
	iconst_5
	ldc 4.28
	fastore
	dup
	bipush 6
	ldc 5.52
	fastore
	dup
	bipush 7
	ldc 5.71
	fastore
	dup
	bipush 8
	ldc 7.84
	fastore
	dup
	bipush 9
	ldc 7.87
	fastore
	astore_1
	ldc 4.28
	fstore_2
	aload_1
	fload_2
	invokestatic ZCodeClass/binary_search([FF)F
	fstore_3
	fload_3
	fconst_1
	fneg
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	ldc "Not found"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label6
Label7:
	fload_3
	invokestatic io/writeNumber(F)V
Label6:
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
.end method
