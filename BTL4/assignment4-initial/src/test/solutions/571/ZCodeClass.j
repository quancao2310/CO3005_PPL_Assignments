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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [[F from Label2 to Label3
.var 2 is i F from Label2 to Label3
.var 3 is j F from Label2 to Label3
.var 4 is chk10 Z from Label2 to Label3
Label2:
	ldc 3.0
	f2i
	anewarray [F
	dup
	iconst_0
	ldc 5.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 10.0
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
	aastore
	dup
	iconst_1
	ldc 5.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 6.0
	fastore
	dup
	iconst_1
	ldc 7.0
	fastore
	dup
	iconst_2
	ldc 8.0
	fastore
	dup
	iconst_3
	ldc 9.0
	fastore
	dup
	iconst_4
	ldc 10.0
	fastore
	aastore
	dup
	iconst_2
	ldc 5.0
	f2i
	newarray float
	dup
	iconst_0
	ldc 11.0
	fastore
	dup
	iconst_1
	ldc 12.0
	fastore
	dup
	iconst_2
	ldc 13.0
	fastore
	dup
	iconst_3
	ldc 14.0
	fastore
	dup
	iconst_4
	ldc 10.0
	fastore
	aastore
	astore_1
	fconst_0
	fstore_2
	fconst_0
	fstore_3
	iconst_0
	istore 4
	fload_2
Label6:
	fload_2
	ldc 3.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	fload_3
Label13:
	fload_3
	ldc 5.0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label12
Label16:
	fload_3
	fconst_0
	fcmpl
	ifne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	goto Label11
Label20:
	aload_1
	fload_2
	f2i
	aaload
	fload_3
	f2i
	faload
	ldc 10.0
	fcmpl
	ifne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
Label24:
	iconst_1
	istore 4
	fload_2
	invokestatic io/writeNumber(F)V
	fload_3
	invokestatic io/writeNumber(F)V
	goto Label12
Label25:
Label23:
Label17:
Label11:
	fload_3
	fconst_1
	fadd
	fstore_3
	goto Label13
Label12:
	fstore_3
	ldc "End of inner loop "
	invokestatic io/writeString(Ljava/lang/String;)V
	iload 4
	ifle Label26
	goto Label5
Label26:
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
.limit stack 7
.limit locals 5
.end method
