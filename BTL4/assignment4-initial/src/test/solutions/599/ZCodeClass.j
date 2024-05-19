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

.method public static max(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
Label2:
	fload_0
	fload_1
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	fload_0
	freturn
Label6:
	fload_1
	freturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static lcs([Ljava/lang/String;[Ljava/lang/String;FF)F
.var 0 is s1 [Ljava/lang/String; from Label0 to Label1
.var 1 is s2 [Ljava/lang/String; from Label0 to Label1
.var 2 is m F from Label0 to Label1
.var 3 is n F from Label0 to Label1
Label0:
Label2:
	fload_2
	fconst_0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	fload_3
	fconst_0
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	ifle Label8
	fconst_0
	freturn
Label8:
	aload_0
	fload_2
	fconst_1
	fsub
	f2i
	aaload
	aload_1
	fload_3
	fconst_1
	fsub
	f2i
	aaload
	invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
	ifle Label11
	fconst_1
	aload_0
	aload_1
	fload_2
	fconst_1
	fsub
	fload_3
	fconst_1
	fsub
	invokestatic ZCodeClass/lcs([Ljava/lang/String;[Ljava/lang/String;FF)F
	fadd
	freturn
Label11:
	aload_0
	aload_1
	fload_2
	fconst_1
	fsub
	fload_3
	invokestatic ZCodeClass/lcs([Ljava/lang/String;[Ljava/lang/String;FF)F
	aload_0
	aload_1
	fload_2
	fload_3
	fconst_1
	fsub
	invokestatic ZCodeClass/lcs([Ljava/lang/String;[Ljava/lang/String;FF)F
	invokestatic ZCodeClass/max(FF)F
	freturn
Label3:
Label1:
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is s1 [Ljava/lang/String; from Label2 to Label3
.var 2 is s2 [Ljava/lang/String; from Label2 to Label3
Label2:
	ldc 10.0
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "A"
	aastore
	dup
	iconst_1
	ldc "G"
	aastore
	dup
	iconst_2
	ldc "G"
	aastore
	dup
	iconst_3
	ldc "T"
	aastore
	dup
	iconst_4
	ldc "A"
	aastore
	dup
	iconst_5
	ldc "B"
	aastore
	dup
	bipush 6
	ldc ""
	aastore
	dup
	bipush 7
	ldc ""
	aastore
	dup
	bipush 8
	ldc ""
	aastore
	dup
	bipush 9
	ldc ""
	aastore
	astore_1
	ldc 10.0
	f2i
	anewarray java/lang/String
	dup
	iconst_0
	ldc "G"
	aastore
	dup
	iconst_1
	ldc "X"
	aastore
	dup
	iconst_2
	ldc "T"
	aastore
	dup
	iconst_3
	ldc "X"
	aastore
	dup
	iconst_4
	ldc "A"
	aastore
	dup
	iconst_5
	ldc "Y"
	aastore
	dup
	bipush 6
	ldc "B"
	aastore
	dup
	bipush 7
	ldc ""
	aastore
	dup
	bipush 8
	ldc ""
	aastore
	dup
	bipush 9
	ldc ""
	aastore
	astore_2
	aload_1
	aload_2
	ldc 6.0
	ldc 7.0
	invokestatic ZCodeClass/lcs([Ljava/lang/String;[Ljava/lang/String;FF)F
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method
