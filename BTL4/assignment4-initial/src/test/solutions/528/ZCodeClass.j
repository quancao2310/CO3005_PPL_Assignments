.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a Ljava/lang/String;
.field static b Ljava/lang/String;
.field static c Ljava/lang/String;

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
.var 1 is x1 Ljava/lang/String; from Label2 to Label3
.var 2 is x2 Ljava/lang/String; from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a Ljava/lang/String;
	ldc " str"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_1
	getstatic ZCodeClass.b Ljava/lang/String;
	getstatic ZCodeClass.c Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
	aload_1
	invokestatic io/writeString(Ljava/lang/String;)V
	ldc "\n"
	invokestatic io/writeString(Ljava/lang/String;)V
	aload_2
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static init()V
Label0:
Label2:
	ldc "abc"
	putstatic ZCodeClass.a Ljava/lang/String;
	ldc "fed"
	putstatic ZCodeClass.b Ljava/lang/String;
	ldc "ghi"
	putstatic ZCodeClass.c Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
