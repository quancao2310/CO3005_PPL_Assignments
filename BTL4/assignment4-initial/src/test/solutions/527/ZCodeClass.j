.source ZCodeClass.java
.class public ZCodeClass
.super java/lang/Object
.field static a Z
.field static b Z
.field static c Z
.field static d Z
.field static e Z

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
.var 1 is x1 Z from Label2 to Label3
.var 2 is x2 Z from Label2 to Label3
.var 3 is x3 Z from Label2 to Label3
Label2:
	invokestatic ZCodeClass/init()V
	getstatic ZCodeClass.a Z
	getstatic ZCodeClass.b Z
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	istore_1
	getstatic ZCodeClass.c Z
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	getstatic ZCodeClass.d Z
	ior
	istore_2
	getstatic ZCodeClass.a Z
	getstatic ZCodeClass.e Z
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	getstatic ZCodeClass.d Z
	iand
	istore_3
	iload_1
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	iload_2
	invokestatic io/writeBool(Z)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
	iload_3
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static init()V
Label0:
Label2:
	iconst_0
	putstatic ZCodeClass.a Z
	iconst_0
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
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
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	putstatic ZCodeClass.b Z
	getstatic ZCodeClass.a Z
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	putstatic ZCodeClass.c Z
	iconst_1
	putstatic ZCodeClass.d Z
	iconst_0
	putstatic ZCodeClass.e Z
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
