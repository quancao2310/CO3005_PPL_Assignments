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

.method public static pow(FF)F
.var 0 is base F from Label0 to Label1
.var 1 is exp F from Label0 to Label1
Label0:
.var 2 is res F from Label2 to Label3
.var 3 is i F from Label2 to Label3
Label2:
	fconst_1
	fstore_2
	fconst_0
	fstore_3
	fload_3
Label6:
	fload_3
	fload_1
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	fload_2
	fload_0
	fmul
	fstore_2
Label10:
Label4:
	fload_3
	fconst_1
	fadd
	fstore_3
	goto Label6
Label5:
	fstore_3
	fload_2
	freturn
Label3:
Label1:
.limit stack 3
.limit locals 4
.end method

.method public static round(FF)F
.var 0 is n F from Label0 to Label1
.var 1 is decimal_points F from Label0 to Label1
Label0:
.var 2 is factor F from Label2 to Label3
Label2:
	ldc 10.0
	fload_1
	invokestatic ZCodeClass/pow(FF)F
	fstore_2
	fload_0
	fload_2
	fmul
	fload_0
	fload_2
	fmul
	fconst_1
	frem
	fsub
	fload_2
	fdiv
	freturn
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static sqrt(FF)F
.var 0 is n F from Label0 to Label1
.var 1 is decimal_points F from Label0 to Label1
Label0:
.var 2 is left F from Label2 to Label3
.var 3 is right F from Label2 to Label3
.var 4 is mid F from Label2 to Label3
.var 5 is _ F from Label2 to Label3
Label2:
	fload_0
	fconst_0
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	fconst_1
	fneg
	freturn
Label6:
	fconst_0
	fstore_2
	fload_0
	fstore_3
	fconst_0
	fstore 4
	fconst_0
	fstore 5
	fload 5
Label9:
	fload_3
	fload_2
	fsub
	ldc 0.1
	fload_1
	invokestatic ZCodeClass/pow(FF)F
	fcmpl
	ifge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label8
Label12:
	fload_2
	fload_3
	fadd
	fconst_2
	fdiv
	fstore 4
	fload 4
	fload 4
	fmul
	fload_0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label17
	fload 4
	freturn
	goto Label16
Label17:
	fload 4
	fload 4
	fmul
	fload_0
	fcmpl
	ifge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label18
	fload 4
	fstore_2
	goto Label16
Label18:
	fload 4
	fstore_3
Label16:
Label13:
Label7:
	fload 5
	fconst_0
	fadd
	fstore 5
	goto Label9
Label8:
	fstore 5
	fload_2
	fload_3
	fadd
	fconst_2
	fdiv
	fload_1
	invokestatic ZCodeClass/round(FF)F
	freturn
Label3:
Label1:
.limit stack 4
.limit locals 6
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fconst_0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 25.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 81.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 100.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 9.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 12.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 13.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 14.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 15.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 16.0
	fconst_2
	invokestatic ZCodeClass/sqrt(FF)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
