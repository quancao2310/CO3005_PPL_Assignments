.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object

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
.var 1 is a F from Label2 to Label3
.var 2 is b F from Label2 to Label3
.var 3 is c Z from Label2 to Label3
.var 4 is x F from Label2 to Label3
.var 5 is y Z from Label2 to Label3
Label2:
	fconst_1
	fstore_1
	fconst_2
	fstore_2
	fload_1
	fload_2
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_3
	fload_1
	fload_1
	fadd
	fload_2
	fsub
	fload_1
	fload_2
	fdiv
	fmul
	fload_1
	fload_2
	frem
	fload_2
	fload_1
	frem
	fload_2
	fload_1
	fdiv
	fload_1
	fload_1
	fadd
	fmul
	fload_2
	fload_1
	fsub
	fdiv
	fadd
	fsub
	fadd
	fload_1
	fload_1
	fmul
	fadd
	fstore 4
	fload_1
	fload_1
	fload_1
	fmul
	fadd
	fload_1
	fload_2
	fsub
	fdiv
	fload_1
	fload_1
	fadd
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_3
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	fload_1
	fload_1
	fadd
	fload_1
	fcmpl
	iflt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	istore 5
	iload 5
	fload_1
	fload_1
	fcmpl
	ifge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	fload_1
	fload_1
	fcmpl
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	fload_1
	fload_1
	fcmpl
	iflt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	fload_1
	fload_1
	fcmpl
	ifne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	fload_1
	fload_1
	fcmpl
	ifeq Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	iand
	ior
	iand
	ior
	iand
	istore 5
	fload 4
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	iload 5
	invokestatic io/writeBool(Z)V
	ldc " This "
	ldc "is "
	ldc "a "
	ldc "string "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	ldc "concatenation"
	ldc "!"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 6
.end method
