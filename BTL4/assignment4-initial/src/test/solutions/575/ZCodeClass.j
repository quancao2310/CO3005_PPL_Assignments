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

.method public static fact(F)F
.var 0 is n F from Label0 to Label1
Label0:
Label2:
	fload_0
	fconst_1
	fcmpl
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	fconst_1
	freturn
Label6:
	fload_0
	fload_0
	fconst_1
	fsub
	invokestatic ZCodeClass/fact(F)F
	fmul
	freturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fconst_1
	invokestatic ZCodeClass/fact(F)F
	invokestatic io/writeNumber(F)V
	fconst_2
	invokestatic ZCodeClass/fact(F)F
	invokestatic io/writeNumber(F)V
	ldc 3.0
	invokestatic ZCodeClass/fact(F)F
	invokestatic io/writeNumber(F)V
	ldc 4.0
	invokestatic ZCodeClass/fact(F)F
	invokestatic io/writeNumber(F)V
	ldc 5.0
	invokestatic ZCodeClass/fact(F)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
