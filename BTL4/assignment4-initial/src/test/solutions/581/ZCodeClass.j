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

.method public static dec_to_bin(F)Ljava/lang/String;
.var 0 is n F from Label0 to Label1
Label0:
.var 1 is res Ljava/lang/String; from Label2 to Label3
.var 2 is i F from Label2 to Label3
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
	ldc "not implemented\n"
	areturn
Label6:
	fload_0
	fconst_0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	ldc "0\n"
	areturn
Label9:
	ldc "\n"
	astore_1
	fconst_0
	fstore_2
	fload_2
Label12:
	fload_0
	fconst_0
	fcmpl
	ifgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label11
Label15:
	fload_0
	fconst_2
	frem
	fconst_0
	fcmpl
	ifne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label20
	ldc "0"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_1
	goto Label19
Label20:
	ldc "1"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_1
Label19:
	fload_0
	fconst_2
	fdiv
	invokestatic ZCodeClass/round(F)F
	fstore_0
Label16:
Label10:
	fload_2
	fconst_0
	fadd
	fstore_2
	goto Label12
Label11:
	aload_1
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 3
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc 4.0
	invokestatic ZCodeClass/dec_to_bin(F)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 10.0
	invokestatic ZCodeClass/dec_to_bin(F)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 100.0
	invokestatic ZCodeClass/dec_to_bin(F)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc 1000.0
	invokestatic ZCodeClass/dec_to_bin(F)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
