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

.method public static print(Ljava/lang/String;Ljava/lang/String;)V
.var 0 is src Ljava/lang/String; from Label0 to Label1
.var 1 is dst Ljava/lang/String; from Label0 to Label1
Label0:
.var 2 is output Ljava/lang/String; from Label2 to Label3
Label2:
	ldc "Move 1 disk from "
	astore_2
	aload_2
	aload_0
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
	aload_2
	ldc " to "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
	aload_2
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
	aload_2
	ldc "\n"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
	aload_2
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static tower_of_hanoi(FLjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
.var 0 is n F from Label0 to Label1
.var 1 is src Ljava/lang/String; from Label0 to Label1
.var 2 is dst Ljava/lang/String; from Label0 to Label1
.var 3 is aux Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	fload_0
	fconst_1
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label7
	aload_1
	aload_2
	invokestatic ZCodeClass/print(Ljava/lang/String;Ljava/lang/String;)V
	goto Label6
Label7:
Label8:
	fload_0
	fconst_1
	fsub
	aload_1
	aload_3
	aload_2
	invokestatic ZCodeClass/tower_of_hanoi(FLjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
	fconst_1
	aload_1
	aload_2
	aload_3
	invokestatic ZCodeClass/tower_of_hanoi(FLjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
	fload_0
	fconst_1
	fsub
	aload_3
	aload_2
	aload_1
	invokestatic ZCodeClass/tower_of_hanoi(FLjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
Label9:
Label6:
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	ldc 3.0
	ldc "A"
	ldc "C"
	ldc "B"
	invokestatic ZCodeClass/tower_of_hanoi(FLjava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method
