import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 300-304: Types
    * 305-324: Declarations
    * 325-334: Expressions
    * 335-354: Statements
    * 355-359: Mixed statements
    * 360-399: Solve algorithms/problems in ZCode
    """
    
    # Types
    def test_300(self):
        # Boolean
        input = """bool a
"""
        expect = str(Program([VarDecl(Id("a"), BoolType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_301(self):
        # Number
        input = """number a
"""
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 301))
    
    def test_302(self):
        # String
        input = """string a
"""
        expect = "Program([VarDecl(Id(a), StringType, None, None)])"
        self.assertTrue(TestAST.test(input, expect, 302))
    
    def test_303(self):
        # 1-dimensional array
        input = """number a[10]
"""
        expect = "Program([VarDecl(Id(a), ArrayType([10.0], NumberType), None, None)])"
        self.assertTrue(TestAST.test(input, expect, 303))
    
    def test_304(self):
        # Multi-dimensional array
        input = """bool a[10, 20, 30]
"""
        expect = "Program([VarDecl(Id(a), ArrayType([10.0, 20.0, 30.0], BoolType), None, None)])"
        self.assertTrue(TestAST.test(input, expect, 304))
    
    # Declarations
    def test_305(self):
        # Boolean declaration
        input = """bool a
        bool b <- true
        bool c <- false
"""
        expect = "Program([VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), BoolType, None, BooleanLit(True)), VarDecl(Id(c), BoolType, None, BooleanLit(False))])"
        self.assertTrue(TestAST.test(input, expect, 305))
    
    def test_306(self):
        # Number declaration
        input = """number a
number b <- 1
number c <- 2.5
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(c), NumberType, None, NumLit(2.5))])"
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_307(self):
        # String declaration
        input = """string a
string b <- "PPL Assignment"
string c <- "This is a string \\n"

"""
        expect = "Program([VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), StringType, None, StringLit(PPL Assignment)), VarDecl(Id(c), StringType, None, StringLit(This is a string \\n))])"
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_308(self):
        # Keyword "var" declaration
        input = """var x <- 1
var y <- true
var z <- "str"
"""
        expect = "Program([VarDecl(Id(x), None, var, NumLit(1.0)), VarDecl(Id(y), None, var, BooleanLit(True)), VarDecl(Id(z), None, var, StringLit(str))])"
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_309(self):
        # Keyword "dynamic" declaration
        input = """dynamic x <- 1
dynamic y
dynamic z <- "str"
"""
        expect = "Program([VarDecl(Id(x), None, dynamic, NumLit(1.0)), VarDecl(Id(y), None, dynamic, None), VarDecl(Id(z), None, dynamic, StringLit(str))])"
        self.assertTrue(TestAST.test(input, expect, 309))
    
    def test_310(self):
        # Array declaration
        input = """string __s[9312e1202]
number a[5] <- [2, 3, 5, 7, 11]
string sss[4] <- ["PPL", "is", "very", "hard"]
bool abc[4] <- [true, true, false, false]

number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
bool c[2, 2, 3] <- [[[true, true, false], [true, true, false]], [[true, true, false], [true, true, false]]]
"""
        expect = "Program([VarDecl(Id(__s), ArrayType([inf], StringType), None, None), VarDecl(Id(a), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(2.0), NumLit(3.0), NumLit(5.0), NumLit(7.0), NumLit(11.0))), VarDecl(Id(sss), ArrayType([4.0], StringType), None, ArrayLit(StringLit(PPL), StringLit(is), StringLit(very), StringLit(hard))), VarDecl(Id(abc), ArrayType([4.0], BoolType), None, ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False), BooleanLit(False))), VarDecl(Id(b), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))), VarDecl(Id(c), ArrayType([2.0, 2.0, 3.0], BoolType), None, ArrayLit(ArrayLit(ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False)), ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False))), ArrayLit(ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False)), ArrayLit(BooleanLit(True), BooleanLit(True), BooleanLit(False)))))])"
        self.assertTrue(TestAST.test(input, expect, 310))
    
    def test_311(self):
        # Declaration with comments
        input = """bool a
## Comment 1
bool b <- true ## Comment 2
######## Comment 3
"""
        expect = "Program([VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), BoolType, None, BooleanLit(True))])"
        self.assertTrue(TestAST.test(input, expect, 311))
    
    def test_312(self):
        # Array declaration with initializing non-array expression
        input = """number x[2] <- foo(x)
number y[2] <- x
"""
        expect = "Program([VarDecl(Id(x), ArrayType([2.0], NumberType), None, CallExpr(Id(foo), [Id(x)])), VarDecl(Id(y), ArrayType([2.0], NumberType), None, Id(x))])"
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test_313(self):
        # Invalid array declaration 1: Initialize array with wrong dimensions
        input = """number x[2.3e1] <- [1, 2, 3]
number x[3, 4] <- [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
"""
        expect = "Program([VarDecl(Id(x), ArrayType([23.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(x), ArrayType([3.0, 4.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0)), ArrayLit(NumLit(8.0), NumLit(9.0), NumLit(10.0), NumLit(11.0), NumLit(12.0))))])"
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test_314(self):
        # Invalid array declaration 2: Wrong element types
        input = """number arr[4] <- [1, true, 3, "x"]
"""
        expect = "Program([VarDecl(Id(arr), ArrayType([4.0], NumberType), None, ArrayLit(NumLit(1.0), BooleanLit(True), NumLit(3.0), StringLit(x)))])"
        self.assertTrue(TestAST.test(input, expect, 314))
    
    def test_315(self):
        # Invalid declaration: wrong type (will not give error now)
        input = """string s <- 123
"""
        expect = "Program([VarDecl(Id(s), StringType, None, NumLit(123.0))])"
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_316(self):
        # Function declaration
        input = """func main()
"""
        expect = "Program([FuncDecl(Id(main), [], None)])"
        self.assertTrue(TestAST.test(input, expect, 316))
    
    def test_317(self):
        # Function with return statement
        input = """func main() return 1
"""
        expect = "Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"
        self.assertTrue(TestAST.test(input, expect, 317))
    
    def test_318(self):
        # Function with block statement
        input = """func main() begin
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 318))
    
    def test_319(self):
        # Multiple functions
        input = """func a() return "hello\\\\"..."world\\'"*--22
func main()
begin
end
"""
        expect = "Program([FuncDecl(Id(a), [], Return(BinaryOp(..., StringLit(hello\\\\), BinaryOp(*, StringLit(world\\'), UnaryOp(-, UnaryOp(-, NumLit(22.0))))))), FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 319))
    
    def test_320(self):
        # Function with 1 parameter
        input = """
func foo(number x)
begin
    return x
end

func main() begin
end
"""
        expect = "Program([FuncDecl(Id(foo), [VarDecl(Id(x), NumberType, None, None)], Block([Return(Id(x))])), FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test_321(self):
        # Function with many parameters
        input = """func foo(number x, number y, string s[9])
begin
    s[5] <- "Awesome'""
    return x + y
end

func main() begin
    foo(1, 2, "xyz")
    return
end
"""
        expect = "Program([FuncDecl(Id(foo), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), NumberType, None, None), VarDecl(Id(s), ArrayType([9.0], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(s), [NumLit(5.0)]), StringLit(Awesome'\")), Return(BinaryOp(+, Id(x), Id(y)))])), FuncDecl(Id(main), [], Block([CallStmt(Id(foo), [NumLit(1.0), NumLit(2.0), StringLit(xyz)]), Return()]))])"
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def test_322(self):
        # Function with local variables
        input = """func main()
begin

number a
string b <- "x"
var c <- false

end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, StringLit(x)), VarDecl(Id(c), None, var, BooleanLit(False))]))])"
        self.assertTrue(TestAST.test(input, expect, 322))
    
    def test_323(self):
        # Function with declaration and implementation parts
        input = """func bar(number x)
func main() begin
    number a <- bar(2024)
    string b <- bar("John")
    writeNumber(a)
end
func bar(number x)
begin
    return x + 1
end
"""
        expect = "Program([FuncDecl(Id(bar), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, CallExpr(Id(bar), [NumLit(2024.0)])), VarDecl(Id(b), StringType, None, CallExpr(Id(bar), [StringLit(John)])), CallStmt(Id(writeNumber), [Id(a)])])), FuncDecl(Id(bar), [VarDecl(Id(x), NumberType, None, None)], Block([Return(BinaryOp(+, Id(x), NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 323))
    
    def test_324(self):
        # Function with global variables
        input = """number MOD <- 1e9 + 7
number _val1 <- 1000
number _val2 <- 20.24
func main()
begin
    writeNumber(_val1 % MOD)
    writeNumber(_val2 % MOD)
end
"""
        expect = "Program([VarDecl(Id(MOD), NumberType, None, BinaryOp(+, NumLit(1000000000.0), NumLit(7.0))), VarDecl(Id(_val1), NumberType, None, NumLit(1000.0)), VarDecl(Id(_val2), NumberType, None, NumLit(20.24)), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [BinaryOp(%, Id(_val1), Id(MOD))]), CallStmt(Id(writeNumber), [BinaryOp(%, Id(_val2), Id(MOD))])]))])"
        self.assertTrue(TestAST.test(input, expect, 324))
    
    # Expressions
    def test_325(self):
        # Number expressions
        input = """
number a <- x + y
number a <- x - y
number a <- x * y
number a <- x / y
number a <- x % y
number a <- -x
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, BinaryOp(+, Id(x), Id(y))), VarDecl(Id(a), NumberType, None, BinaryOp(-, Id(x), Id(y))), VarDecl(Id(a), NumberType, None, BinaryOp(*, Id(x), Id(y))), VarDecl(Id(a), NumberType, None, BinaryOp(/, Id(x), Id(y))), VarDecl(Id(a), NumberType, None, BinaryOp(%, Id(x), Id(y))), VarDecl(Id(a), NumberType, None, UnaryOp(-, Id(x)))])"
        self.assertTrue(TestAST.test(input, expect, 325))
    
    def test_326(self):
        # Boolean and relational expressions
        input = """
bool a <- x and y
bool a <- x or y
bool a <- not y

bool a <- x = y
bool a <- x != y
bool a <- x < y
bool a <- x <= y
bool a <- x > y
bool a <- x >= y
bool a <- x == y
"""
        expect = "Program([VarDecl(Id(a), BoolType, None, BinaryOp(and, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(or, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, UnaryOp(not, Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(=, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(!=, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(<, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(<=, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(>, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(>=, Id(x), Id(y))), VarDecl(Id(a), BoolType, None, BinaryOp(==, Id(x), Id(y)))])"
        self.assertTrue(TestAST.test(input, expect, 326))
    
    def test_327(self):
        # String and indexing expressions
        input = """
string a <- x...y

var x <- arr[1, 2, 3]

func main() begin
    a[3 + foo(2), x, y] <- a[b[2, 3]] + 4
end
"""
        expect = "Program([VarDecl(Id(a), StringType, None, BinaryOp(..., Id(x), Id(y))), VarDecl(Id(x), None, var, ArrayCell(Id(arr), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])), FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [BinaryOp(+, NumLit(3.0), CallExpr(Id(foo), [NumLit(2.0)])), Id(x), Id(y)]), BinaryOp(+, ArrayCell(Id(a), [ArrayCell(Id(b), [NumLit(2.0), NumLit(3.0)])]), NumLit(4.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 327))
    
    def test_328(self):
        # Function call expression and sub-expression
        input = """
dynamic a <- foo(213)
dynamic a <- bar(foo("x" + 4.213))
dynamic a <- (foo() + 2) * "adsad"
dynamic a <- -(x + x)*(x-x) ... foo(x, y, z)
"""
        expect = "Program([VarDecl(Id(a), None, dynamic, CallExpr(Id(foo), [NumLit(213.0)])), VarDecl(Id(a), None, dynamic, CallExpr(Id(bar), [CallExpr(Id(foo), [BinaryOp(+, StringLit(x), NumLit(4.213))])])), VarDecl(Id(a), None, dynamic, BinaryOp(*, BinaryOp(+, CallExpr(Id(foo), []), NumLit(2.0)), StringLit(adsad))), VarDecl(Id(a), None, dynamic, BinaryOp(..., BinaryOp(*, UnaryOp(-, BinaryOp(+, Id(x), Id(x))), BinaryOp(-, Id(x), Id(x))), CallExpr(Id(foo), [Id(x), Id(y), Id(z)])))])"
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test_329(self):
        # Unary operators
        input = """func main()
begin
    var x <- -1
    var x <- --1
    var x <- ---1
    var x <- ----1
    var x <- -----1
    var x <--------1
    
    var y <- not x
    var y <- not not x
    var y <- not not not x
    var y <- not not not not not not x
    
    var z <- a[1]
    var z <- a[1, 2, a[3]]
    var z <- a[1, "a", "B"]
    var z <- a[[true, false]]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), None, var, UnaryOp(-, NumLit(1.0))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, NumLit(1.0)))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0)))))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))))))), VarDecl(Id(y), None, var, UnaryOp(not, Id(x))), VarDecl(Id(y), None, var, UnaryOp(not, UnaryOp(not, Id(x)))), VarDecl(Id(y), None, var, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(x))))), VarDecl(Id(y), None, var, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(not, UnaryOp(not, Id(x)))))))), VarDecl(Id(z), None, var, ArrayCell(Id(a), [NumLit(1.0)])), VarDecl(Id(z), None, var, ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), ArrayCell(Id(a), [NumLit(3.0)])])), VarDecl(Id(z), None, var, ArrayCell(Id(a), [NumLit(1.0), StringLit(a), StringLit(B)])), VarDecl(Id(z), None, var, ArrayCell(Id(a), [ArrayLit(BooleanLit(True), BooleanLit(False))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test_330(self):
        # Complex expressions 1
        input = """
number a <- ((a + b - c) * (d / e)) + ((f % g) - ((h % i) + (j / k) * (l + m) / (n - o))) + (p * q)
number b <- ((a1 + a2) * a3) / (a1 - a2) % (a1 != a2) and (not (a3 < a2) or (a1 <= a3 and (a2 >= a1 or (a3 == a2 and (a1 != a2))))) or (a1 + a2) * (a3 > a2) / (a1 <= a3)
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, BinaryOp(+, BinaryOp(+, BinaryOp(*, BinaryOp(-, BinaryOp(+, Id(a), Id(b)), Id(c)), BinaryOp(/, Id(d), Id(e))), BinaryOp(-, BinaryOp(%, Id(f), Id(g)), BinaryOp(+, BinaryOp(%, Id(h), Id(i)), BinaryOp(/, BinaryOp(*, BinaryOp(/, Id(j), Id(k)), BinaryOp(+, Id(l), Id(m))), BinaryOp(-, Id(n), Id(o)))))), BinaryOp(*, Id(p), Id(q)))), VarDecl(Id(b), NumberType, None, BinaryOp(or, BinaryOp(and, BinaryOp(%, BinaryOp(/, BinaryOp(*, BinaryOp(+, Id(a1), Id(a2)), Id(a3)), BinaryOp(-, Id(a1), Id(a2))), BinaryOp(!=, Id(a1), Id(a2))), BinaryOp(or, UnaryOp(not, BinaryOp(<, Id(a3), Id(a2))), BinaryOp(<=, Id(a1), BinaryOp(and, Id(a3), BinaryOp(>=, Id(a2), BinaryOp(or, Id(a1), BinaryOp(==, Id(a3), BinaryOp(and, Id(a2), BinaryOp(!=, Id(a1), Id(a2)))))))))), BinaryOp(/, BinaryOp(*, BinaryOp(+, Id(a1), Id(a2)), BinaryOp(>, Id(a3), Id(a2))), BinaryOp(<=, Id(a1), Id(a3)))))])"
        self.assertTrue(TestAST.test(input, expect, 330))
    
    def test_331(self):
        # Complex expressions 2
        input = """func __aaa__() begin
    number arr[0, 0, 0] <- [[1, 2, 3], ["a\\'" ... "b\\'", foo()["index\\\\"]], [(a and not c) = d]]
end
"""
        expect = "Program([FuncDecl(Id(__aaa__), [], Block([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(..., StringLit(a\\'), StringLit(b\\')), ArrayCell(CallExpr(Id(foo), []), [StringLit(index\\\\)])), ArrayLit(BinaryOp(=, BinaryOp(and, Id(a), UnaryOp(not, Id(c))), Id(d)))))]))])"
        self.assertTrue(TestAST.test(input, expect, 331))
    
    def test_332(self):
        # Complex expressions 3
        input = """func x() begin 
hello()
kkap(kk(yeah(ha(idk(2,4,[2,4,[[[[[[[[[[[2]]]]]]]]]]],45],4)))))
end
"""
        expect = "Program([FuncDecl(Id(x), [], Block([CallStmt(Id(hello), []), CallStmt(Id(kkap), [CallExpr(Id(kk), [CallExpr(Id(yeah), [CallExpr(Id(ha), [CallExpr(Id(idk), [NumLit(2.0), NumLit(4.0), ArrayLit(NumLit(2.0), NumLit(4.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(2.0)))))))))))), NumLit(45.0)), NumLit(4.0)])])])])])]))])"
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_333(self):
        # Complex expressions 4
        input = """ func calculateSthComplicated(number a, number b, number c)
begin
    number result
    result <- -a * b + (c % 3) - 5 / (a + 1) and not (b > c) or (a == b) * (c >= 0)
    string finalText <- "Result: " ... result
    writeString(finalText)
end
func main() begin
    number a <- 26
    number b <- 2
    number c <- 2024
    calculateSthComplicated(a, b, c)
end
"""
        expect = "Program([FuncDecl(Id(calculateSthComplicated), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Block([VarDecl(Id(result), NumberType, None, None), AssignStmt(Id(result), BinaryOp(or, BinaryOp(and, BinaryOp(-, BinaryOp(+, BinaryOp(*, UnaryOp(-, Id(a)), Id(b)), BinaryOp(%, Id(c), NumLit(3.0))), BinaryOp(/, NumLit(5.0), BinaryOp(+, Id(a), NumLit(1.0)))), UnaryOp(not, BinaryOp(>, Id(b), Id(c)))), BinaryOp(*, BinaryOp(==, Id(a), Id(b)), BinaryOp(>=, Id(c), NumLit(0.0))))), VarDecl(Id(finalText), StringType, None, BinaryOp(..., StringLit(Result: ), Id(result))), CallStmt(Id(writeString), [Id(finalText)])])), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(26.0)), VarDecl(Id(b), NumberType, None, NumLit(2.0)), VarDecl(Id(c), NumberType, None, NumLit(2024.0)), CallStmt(Id(calculateSthComplicated), [Id(a), Id(b), Id(c)])]))])"
        self.assertTrue(TestAST.test(input, expect, 333))
    
    def test_334(self):
        # Complex expressions 5
        input = """func kfpd3omas(string __odsa_321, bool MA02masS32[24.913, 8e32], number aksdasd[5, 5, 3.217]) return
## osfod32;/['[fgpkodfmae;f,mqn3t4in]
string _09132lmasad <- "F$\\''"\\t\\b'"\\'"
## {ASKDAD{S:DAP:DASF>GAGDGAL#%{Q#{:F}}}{"{}"}"+:+"{P:+_}}}}
string _AsaBKOS0eqwe <- "{ASKDAD{S:DAP:DASF>GAGDGAL#%{Q#{:F}}}{'"{'"}'"+:+'"'{P:+_}}}}"
"""
        expect = """Program([FuncDecl(Id(kfpd3omas), [VarDecl(Id(__odsa_321), StringType, None, None), VarDecl(Id(MA02masS32), ArrayType([24.913, 8e+32], BoolType), None, None), VarDecl(Id(aksdasd), ArrayType([5.0, 5.0, 3.217], NumberType), None, None)], Return()), VarDecl(Id(_09132lmasad), StringType, None, StringLit(F$\\''"\\t\\b'"\\')), VarDecl(Id(_AsaBKOS0eqwe), StringType, None, StringLit({ASKDAD{S:DAP:DASF>GAGDGAL#%{Q#{:F}}}{'"{'"}'"+:+'"'{P:+_}}}}))])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    
    # Statements
    def test_335(self):
        # Scalar variable assignment
        input = """func main() begin
a <- 100
b <- "oifj'"safjms'"fp"
c <- true and true
d <- 0.13E-1
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(100.0)), AssignStmt(Id(b), StringLit(oifj'"safjms'"fp)), AssignStmt(Id(c), BinaryOp(and, BooleanLit(True), BooleanLit(True))), AssignStmt(Id(d), NumLit(0.013))]))])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    
    def test_336(self):
        # Index assignment
        input = """func main() begin
l[3] <- value * aPi
foo[x, y, z + 1] <- abc[231.e+9]
rec[rec[rec[rec[rec[rec[rec[rec[rec[rec[rec["infinitely"]]]]]]]]]]] <- "stack"..."overflow"
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(l), [NumLit(3.0)]), BinaryOp(*, Id(value), Id(aPi))), AssignStmt(ArrayCell(Id(foo), [Id(x), Id(y), BinaryOp(+, Id(z), NumLit(1.0))]), ArrayCell(Id(abc), [NumLit(231000000000.0)])), AssignStmt(ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [ArrayCell(Id(rec), [StringLit(infinitely)])])])])])])])])])])]), BinaryOp(..., StringLit(stack), StringLit(overflow)))]))])"
        self.assertTrue(TestAST.test(input, expect, 336))
    
    def test_337(self):
        # Block statement
        input = """func main() begin
    begin
        number r
        number s
        r <- 2.0
    end
    begin
        
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end

end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, None), AssignStmt(Id(r), NumLit(2.0))]), Block([VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), ArrayType([5.0], NumberType), None, None), AssignStmt(Id(s), BinaryOp(*, BinaryOp(*, Id(r), Id(r)), NumLit(3.14))), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), Id(s))])]))])"
        self.assertTrue(TestAST.test(input, expect, 337))
    
    def test_338(self):
        # Nested blocks 1
        input = """func main() begin
    begin
        number r
        number s <- 3
        r <- 2.0
        begin
            s <- r * r - r
            writeNumber(s)
        end
        writeNumber(s)
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, NumLit(3.0)), AssignStmt(Id(r), NumLit(2.0)), Block([AssignStmt(Id(s), BinaryOp(-, BinaryOp(*, Id(r), Id(r)), Id(r))), CallStmt(Id(writeNumber), [Id(s)])]), CallStmt(Id(writeNumber), [Id(s)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 338))
    
    def test_339(self):
        # Nested blocks 2
        input = """func a()
begin
    begin
        begin
            begin
                begin
                    begin
                    begin
                    begin
                    end
                    end
                    end
                end
            end
        end
    end
end
"""
        expect = "Program([FuncDecl(Id(a), [], Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])]))])"
        self.assertTrue(TestAST.test(input, expect, 339))
    
    def test_340(self):
        # If statement: 1 line
        input = """func main() begin
    if (a = 1) writeBool(true)
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(a), NumLit(1.0)), CallStmt(Id(writeBool), [BooleanLit(True)])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 340))
    
    def test_341(self):
        # If statement: block statement
        input = """func main() begin
    if (a = 1)
    
    begin
        bool x <- true
        writeBool(x)
        x <- x ... a + 2
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(a), NumLit(1.0)), Block([VarDecl(Id(x), BoolType, None, BooleanLit(True)), CallStmt(Id(writeBool), [Id(x)]), AssignStmt(Id(x), BinaryOp(..., Id(x), BinaryOp(+, Id(a), NumLit(2.0))))])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 341))
    
    def test_342(self):
        # If statement: nested if
        input = """func main() begin
    if (a = 1)
        if (b = 1) begin
            string s <- readString()
            writeString(s)
        end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(a), NumLit(1.0)), If((BinaryOp(=, Id(b), NumLit(1.0)), Block([VarDecl(Id(s), StringType, None, CallExpr(Id(readString), [])), CallStmt(Id(writeString), [Id(s)])])), [], None)), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 342))
    
    def test_343(self):
        # If-else statement
        input = """func main() begin
    if (PPL_is_easy()) begin
        writeString("u are lying")
    end
    else begin
        writeString("coi SCORM di em")
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(PPL_is_easy), []), Block([CallStmt(Id(writeString), [StringLit(u are lying)])])), [], Block([CallStmt(Id(writeString), [StringLit(coi SCORM di em)])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 343))
    
    def test_344(self):
        # If-elif-else statement
        input = """number status <- 404

func main()
begin
    string msg
    if (status = 200)
        msg <- "OK"
    elif (status = 400)
        msg <- "Bad Request"
    elif (status = 401) msg <- "Unauthorized"
    elif (status = 404)
        
        msg <- "Not Found"
    elif (status = 500)
        msg <- "Internal Server Error"
    else msg <- "Other messages"
    printString(msg)
end
"""
        expect = "Program([VarDecl(Id(status), NumberType, None, NumLit(404.0)), FuncDecl(Id(main), [], Block([VarDecl(Id(msg), StringType, None, None), If((BinaryOp(=, Id(status), NumLit(200.0)), AssignStmt(Id(msg), StringLit(OK))), [(BinaryOp(=, Id(status), NumLit(400.0)), AssignStmt(Id(msg), StringLit(Bad Request))), (BinaryOp(=, Id(status), NumLit(401.0)), AssignStmt(Id(msg), StringLit(Unauthorized))), (BinaryOp(=, Id(status), NumLit(404.0)), AssignStmt(Id(msg), StringLit(Not Found))), (BinaryOp(=, Id(status), NumLit(500.0)), AssignStmt(Id(msg), StringLit(Internal Server Error)))], AssignStmt(Id(msg), StringLit(Other messages))), CallStmt(Id(printString), [Id(msg)])]))])"
        self.assertTrue(TestAST.test(input, expect, 344))
    
    def test_345(self):
        # Mixed if-elif-else statement
        input = """func main() begin
if ("adk\\rasd")
if (sdad)
if (true and false)
foo(1)
elif (adm2 or fs)
foo(2)
else foo(3)
elif (_13kacs)
if (akdsd)
foo(4)
else foo(5)
else foo(6)
elif ("\\''"ashduau23/fik")
foo(7)
else foo(8)
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((StringLit(adk\\rasd), If((Id(sdad), If((BinaryOp(and, BooleanLit(True), BooleanLit(False)), CallStmt(Id(foo), [NumLit(1.0)])), [(BinaryOp(or, Id(adm2), Id(fs)), CallStmt(Id(foo), [NumLit(2.0)]))], CallStmt(Id(foo), [NumLit(3.0)]))), [(Id(_13kacs), If((Id(akdsd), CallStmt(Id(foo), [NumLit(4.0)])), [], CallStmt(Id(foo), [NumLit(5.0)])))], CallStmt(Id(foo), [NumLit(6.0)]))), [(StringLit(\\''"ashduau23/fik), CallStmt(Id(foo), [NumLit(7.0)]))], CallStmt(Id(foo), [NumLit(8.0)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    
    def test_346(self):
        # For statement
        input = """func main() begin
var i <- 0
for i until i >= 10 by 1
writeNumber(i)
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), NumLit(1.0), CallStmt(Id(writeNumber), [Id(i)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test_347(self):
        # For statement: block statement
        input = """func main() begin
number arr[20, 10]
var i <- 0
var j <- 0

for i until i >= 20 by 1
begin
    var tmp_10i <- 10*i
    for j until j >= 10 by 1 begin
        arr[i, j] <- tmp_10i + j
        writeNumber(arr[i, j])
    end
end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([20.0, 10.0], NumberType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(20.0)), NumLit(1.0), Block([VarDecl(Id(tmp_10i), None, var, BinaryOp(*, NumLit(10.0), Id(i))), For(Id(j), BinaryOp(>=, Id(j), NumLit(10.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(arr), [Id(i), Id(j)]), BinaryOp(+, Id(tmp_10i), Id(j))), CallStmt(Id(writeNumber), [ArrayCell(Id(arr), [Id(i), Id(j)])])]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 347))
    
    def test_348(self):
        # For statement: nested for
        input = """func main() begin
number arr[20, 10]
var i <- 0
var j <- 0
for i until i >= 20 by 1
    for j until j >= 10 by 1
        arr[i, j] <- readNumber()
writeNumber(i)
writeNumber(j)
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([20.0, 10.0], NumberType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(20.0)), NumLit(1.0), For(Id(j), BinaryOp(>=, Id(j), NumLit(10.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(arr), [Id(i), Id(j)]), CallExpr(Id(readNumber), [])))), CallStmt(Id(writeNumber), [Id(i)]), CallStmt(Id(writeNumber), [Id(j)])]))])"
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test_349(self):
        # For statement: break statement
        input = """func main() begin
number i <- 1
for i until i = 20 by 1
begin
    writeBool(true)
    if (i = 10) break
end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(20.0)), NumLit(1.0), Block([CallStmt(Id(writeBool), [BooleanLit(True)]), If((BinaryOp(=, Id(i), NumLit(10.0)), Break), [], None)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 349))
    
    def test_350(self):
        # For statement: continue statement
        input = """func main() begin
number i <- 20
for i until i = 0 by -1
begin
    if (i >= 10)
        continue
    writeString("less than 10")
end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), NumberType, None, NumLit(20.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), Block([If((BinaryOp(>=, Id(i), NumLit(10.0)), Continue), [], None), CallStmt(Id(writeString), [StringLit(less than 10)])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def test_351(self):
        # Return statement: return only
        input = """func main() begin
    return
end

func foo(number x) begin
    if (x > 1) return
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Return()])), FuncDecl(Id(foo), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(>, Id(x), NumLit(1.0)), Return()), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test_352(self):
        # Return statement: return expression 1
        input = """
func pow(number x, number n) begin
    ## Calculate x^n (n >= 0)
    if (n = 0) return 1
    
    var tmp <- pow(x, round(n/2))
    if (n % 2 = 1) return tmp*tmp*x
    return tmp*tmp
end

func round(number n)
begin
    return n - n % 1
end
"""
        expect = "Program([FuncDecl(Id(pow), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(1.0))), [], None), VarDecl(Id(tmp), None, var, CallExpr(Id(pow), [Id(x), CallExpr(Id(round), [BinaryOp(/, Id(n), NumLit(2.0))])])), If((BinaryOp(=, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(1.0)), Return(BinaryOp(*, BinaryOp(*, Id(tmp), Id(tmp)), Id(x)))), [], None), Return(BinaryOp(*, Id(tmp), Id(tmp)))])), FuncDecl(Id(round), [VarDecl(Id(n), NumberType, None, None)], Block([Return(BinaryOp(-, Id(n), BinaryOp(%, Id(n), NumLit(1.0))))]))])"
        self.assertTrue(TestAST.test(input, expect, 352))
    
    def test_353(self):
        # Return statement: return expression 2 (array)
        input = """func main() begin
number x[50] <- createArray(50)
return [1, 2, 3]
end

func createArray(number n)
begin
    if (n > 100) n <- 100
    
    number res[100]
    var i <- 0
    for i until i = n by 1
        res[i] <- 0
    i <- n
    for i until i = 100 by 1
        res[i] <- -1
    return res
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), ArrayType([50.0], NumberType), None, CallExpr(Id(createArray), [NumLit(50.0)])), Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])), FuncDecl(Id(createArray), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(>, Id(n), NumLit(100.0)), AssignStmt(Id(n), NumLit(100.0))), [], None), VarDecl(Id(res), ArrayType([100.0], NumberType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), Id(n)), NumLit(1.0), AssignStmt(ArrayCell(Id(res), [Id(i)]), NumLit(0.0))), AssignStmt(Id(i), Id(n)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(res), [Id(i)]), UnaryOp(-, NumLit(1.0)))), Return(Id(res))]))])"
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test_354(self):
        # Function call statement
        input = """func main() begin
    foo()
    pow(2, 3)
    pow(0, 4)
    pow(pow(2, 3), pow(4, 2))
    pow(arr[2, 3], 4 - 2 + 6 * round(7/3))
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(foo), []), CallStmt(Id(pow), [NumLit(2.0), NumLit(3.0)]), CallStmt(Id(pow), [NumLit(0.0), NumLit(4.0)]), CallStmt(Id(pow), [CallExpr(Id(pow), [NumLit(2.0), NumLit(3.0)]), CallExpr(Id(pow), [NumLit(4.0), NumLit(2.0)])]), CallStmt(Id(pow), [ArrayCell(Id(arr), [NumLit(2.0), NumLit(3.0)]), BinaryOp(+, BinaryOp(-, NumLit(4.0), NumLit(2.0)), BinaryOp(*, NumLit(6.0), CallExpr(Id(round), [BinaryOp(/, NumLit(7.0), NumLit(3.0))])))])]))])"
        self.assertTrue(TestAST.test(input, expect, 354))
    
    # Mixed statements
    def test_355(self):
        # If with for statement 1
        input = """func main() begin
    if (1)
        for i until i > 3 by 1
            if (2) LOOP_COUNT<- LOOP_COUNT ----1
            elif (3)
                for i until i > 3 by 1
                    if (4) a <--a
    for i until i = 4 by 1
        if (5)
            for j until j = 6 by -1.4
                if (6) break
                elif (7) continue
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.0), For(Id('i'), BinaryOp('>', Id('i'), NumberLiteral(3.0)), NumberLiteral(1.0), If(NumberLiteral(2.0), Assign(Id('LOOP_COUNT'), BinaryOp('-', Id('LOOP_COUNT'), UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.0)))))), [(NumberLiteral(3.0), For(Id('i'), BinaryOp('>', Id('i'), NumberLiteral(3.0)), NumberLiteral(1.0), If(NumberLiteral(4.0), Assign(Id('a'), UnaryOp('-', Id('a'))))))]))), For(Id('i'), BinaryOp('=', Id('i'), NumberLiteral(4.0)), NumberLiteral(1.0), If(NumberLiteral(5.0), For(Id('j'), BinaryOp('=', Id('j'), NumberLiteral(6.0)), UnaryOp('-', NumberLiteral(1.4)), If(NumberLiteral(6.0), Break(), [(NumberLiteral(7.0), Continue())]))))]))]))
        self.assertTrue(TestAST.test(input, expect, 355))
    
    def test_356(self):
        # If with for statement 2
        input = """func main() begin
    if (1)
        for i until i > 3 by 1
            if (2) break
            else continue
    for i until i = 4 by 1
        if (5)
            for j until j = 6 by -1.4 LOOP_COUNT <- LOOP_COUNT --1
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.0), For(Id('i'), BinaryOp('>', Id('i'), NumberLiteral(3.0)), NumberLiteral(1.0), If(NumberLiteral(2.0), Break(), [], Continue()))), For(Id('i'), BinaryOp('=', Id('i'), NumberLiteral(4.0)), NumberLiteral(1.0), If(NumberLiteral(5.0), For(Id('j'), BinaryOp('=', Id('j'), NumberLiteral(6.0)), UnaryOp('-', NumberLiteral(1.4)), Assign(Id('LOOP_COUNT'), BinaryOp('-', Id('LOOP_COUNT'), UnaryOp('-', NumberLiteral(1.0)))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 356))
    
    def test_357(self):
        # Mixed statements program 1
        input = """func main() begin
## cond stmt
if (a > 1)
    a <- 1
elif (a < 1) begin
    a <- 0
end
else begin
    a <- 0.5
end
## iter stmt
for i until a >= 0 by 0 begin
    a <- a*0.4
    print(a)
    if (a > 5E-1) continue
    if (a < 1) break
end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(>, Id(a), NumLit(1.0)), AssignStmt(Id(a), NumLit(1.0))), [(BinaryOp(<, Id(a), NumLit(1.0)), Block([AssignStmt(Id(a), NumLit(0.0))]))], Block([AssignStmt(Id(a), NumLit(0.5))])), For(Id(i), BinaryOp(>=, Id(a), NumLit(0.0)), NumLit(0.0), Block([AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(0.4))), CallStmt(Id(print), [Id(a)]), If((BinaryOp(>, Id(a), NumLit(0.5)), Continue), [], None), If((BinaryOp(<, Id(a), NumLit(1.0)), Break), [], None)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 357))
    
    def test_358(self):
        # Mixed statements program 2
        input = """func main () begin
number a <- 10
if (a > 0)
    for a until a <= 0 by -1
        if (a > 5) writeString("a > 5")
        else continue
return a
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(10.0)), If((BinaryOp(>, Id(a), NumLit(0.0)), For(Id(a), BinaryOp(<=, Id(a), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), If((BinaryOp(>, Id(a), NumLit(5.0)), CallStmt(Id(writeString), [StringLit(a > 5)])), [], Continue))), [], None), Return(Id(a))]))])"
        self.assertTrue(TestAST.test(input, expect, 358))
    
    def test_359(self):
        # Mixed statements program 3
        input = """func main() begin 
    number a[4,6,7,8]
    a[3,true,1,ahahaha(4)] <- 1
    if (a[31,32.1,3E+1,huhu((0))]) doNothing()
    else for x until 3600 + s == 1 + h by 1e9+7 alsoDoNothing()
    begin
        x <- 234
        begin
            y <- 567
            begin
                print(x+y)
            end
        end
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([4.0, 6.0, 7.0, 8.0], NumberType), None, None), AssignStmt(ArrayCell(Id(a), [NumLit(3.0), BooleanLit(True), NumLit(1.0), CallExpr(Id(ahahaha), [NumLit(4.0)])]), NumLit(1.0)), If((ArrayCell(Id(a), [NumLit(31.0), NumLit(32.1), NumLit(30.0), CallExpr(Id(huhu), [NumLit(0.0)])]), CallStmt(Id(doNothing), [])), [], For(Id(x), BinaryOp(==, BinaryOp(+, NumLit(3600.0), Id(s)), BinaryOp(+, NumLit(1.0), Id(h))), BinaryOp(+, NumLit(1000000000.0), NumLit(7.0)), CallStmt(Id(alsoDoNothing), []))), Block([AssignStmt(Id(x), NumLit(234.0)), Block([AssignStmt(Id(y), NumLit(567.0)), Block([CallStmt(Id(print), [BinaryOp(+, Id(x), Id(y))])])])])]))])"
        self.assertTrue(TestAST.test(input, expect, 359))
    
    # Solve algorithms/problems in ZCode
    def test_360(self):
        # Factorial
        input = """func fact(number n) begin
if (n = 1) return 1
return n * fact(n - 1)
end
"""
        expect = "Program([FuncDecl(Id(fact), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(1.0)), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, Id(n), CallExpr(Id(fact), [BinaryOp(-, Id(n), NumLit(1.0))])))]))])"
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test_361(self):
        # XOR function
        input = """func xor(bool a, bool b) return (a and not b) or (not a and b)
"""
        expect = "Program([FuncDecl(Id(xor), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), BoolType, None, None)], Return(BinaryOp(or, BinaryOp(and, Id(a), UnaryOp(not, Id(b))), BinaryOp(and, UnaryOp(not, Id(a)), Id(b)))))])"
        self.assertTrue(TestAST.test(input, expect, 361))
    
    def test_362(self):
        # Count digits of a number
        input = """func main() begin
var num <- readNumber()
number count <- 1
number core <- 10
for core until false by 0
    if (num < core) break
    else core <- 10*core
    count<-count+1
writeNumber(num)
writeString(" has ")
writeNumber(count)
writeString(" digits.")
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(num), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(count), NumberType, None, NumLit(1.0)), VarDecl(Id(core), NumberType, None, NumLit(10.0)), For(Id(core), BooleanLit(False), NumLit(0.0), If((BinaryOp(<, Id(num), Id(core)), Break), [], AssignStmt(Id(core), BinaryOp(*, NumLit(10.0), Id(core))))), AssignStmt(Id(count), BinaryOp(+, Id(count), NumLit(1.0))), CallStmt(Id(writeNumber), [Id(num)]), CallStmt(Id(writeString), [StringLit( has )]), CallStmt(Id(writeNumber), [Id(count)]), CallStmt(Id(writeString), [StringLit( digits.)])]))])"
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test_363(self):
        # Check leap year
        input = """func is_leap(number year)
return (year % 4 = 0) and ((year % 100 != 0) or (year % 400 = 0))
func main()
begin
    number year <- 2024
    writeNumber(year)
    if (is_leap(year))
        writeString(" is a leap year")
    else writeString(" is not a leap year")
end
"""
        expect = "Program([FuncDecl(Id(is_leap), [VarDecl(Id(year), NumberType, None, None)], Return(BinaryOp(and, BinaryOp(=, BinaryOp(%, Id(year), NumLit(4.0)), NumLit(0.0)), BinaryOp(or, BinaryOp(!=, BinaryOp(%, Id(year), NumLit(100.0)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(year), NumLit(400.0)), NumLit(0.0)))))), FuncDecl(Id(main), [], Block([VarDecl(Id(year), NumberType, None, NumLit(2024.0)), CallStmt(Id(writeNumber), [Id(year)]), If((CallExpr(Id(is_leap), [Id(year)]), CallStmt(Id(writeString), [StringLit( is a leap year)])), [], CallStmt(Id(writeString), [StringLit( is not a leap year)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 363))
    
    def test_364(self):
        # Find divisors of a number
        input = """func find_divisors(number n) begin
number res[100]
number i <- 0
number x <- 1
for x until x > n by 1
    if (x = n) res[i] <- -1
    elif (n % x = 0) begin
        res[i] <- x
        i <- i + 1
    end
return res
end
"""
        expect = "Program([FuncDecl(Id(find_divisors), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(res), ArrayType([100.0], NumberType), None, None), VarDecl(Id(i), NumberType, None, NumLit(0.0)), VarDecl(Id(x), NumberType, None, NumLit(1.0)), For(Id(x), BinaryOp(>, Id(x), Id(n)), NumLit(1.0), If((BinaryOp(=, Id(x), Id(n)), AssignStmt(ArrayCell(Id(res), [Id(i)]), UnaryOp(-, NumLit(1.0)))), [(BinaryOp(=, BinaryOp(%, Id(n), Id(x)), NumLit(0.0)), Block([AssignStmt(ArrayCell(Id(res), [Id(i)]), Id(x)), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))]))], None)), Return(Id(res))]))])"
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test_365(self):
        # Find average of array
        input = """func avg(number a[100], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum / length
end
"""
        expect = "Program([FuncDecl(Id(avg), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(sum), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(BinaryOp(/, Id(sum), Id(length)))]))])"
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test_366(self):
        # Convert Celsius to Fahrenheit
        input = """func C_to_F(number celsius) return (celsius * 1.8) + 32
"""
        expect = "Program([FuncDecl(Id(C_to_F), [VarDecl(Id(celsius), NumberType, None, None)], Return(BinaryOp(+, BinaryOp(*, Id(celsius), NumLit(1.8)), NumLit(32.0))))])"
        self.assertTrue(TestAST.test(input, expect, 366))
    
    def test_367(self):
        # Check even number
        input = """func isEven(number n) return (n % 2) = 0
"""
        expect = "Program([FuncDecl(Id(isEven), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(=, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0))))])"
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test_368(self):
        # Binary Search Tree (BST)
        input = """func initTree(number tree[100,3]) begin 
    var i<-0 
    for i until i=100 by 1
        begin 
            tree[i,0] <- -1
            tree[i,1] <- -1
            tree[i,2] <- -1
        end
end

func appendNode(number val,number head,number tree[100,3],bool freeNode[100])
begin 
number node <- 0 
for node until node=100 by 1
    if (freeNode[node]) break 
freeNode[node] <- false 
tree[node,0] <- val 
if (head = -1) return node 
var i <- 0 
number currNode <- 0
for i until i=100 by 1 
begin 
if (tree[node,0] < tree[currNode,0])
    begin 
        if (tree[currNode,1]!=-1) currNode <- tree[currNode,1]
        else tree[currNode,1] <- node 
    end
else begin
    if (tree[currNode,2]!=-1) currNode <- tree[currNode,2]
    else tree[currNode,2] <- node
end
end 
return head
end 

func main() begin 
number tree[100,3]
bool freeNode[100]
number head <- -1
initTree(tree)
var i<-0 
for i until i=100 by 1
    freeNode[i] <- true
i<-0 
for i until i=100 by 1
    begin 
        number val <- readNumber()
        head <- appendNode(val,head,tree, freeNode)
    end
end
"""
        expect = "Program([FuncDecl(Id(initTree), [VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(0.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(ArrayCell(Id(tree), [Id(i), NumLit(2.0)]), UnaryOp(-, NumLit(1.0)))]))])), FuncDecl(Id(appendNode), [VarDecl(Id(val), NumberType, None, None), VarDecl(Id(head), NumberType, None, None), VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None)], Block([VarDecl(Id(node), NumberType, None, NumLit(0.0)), For(Id(node), BinaryOp(=, Id(node), NumLit(100.0)), NumLit(1.0), If((ArrayCell(Id(freeNode), [Id(node)]), Break), [], None)), AssignStmt(ArrayCell(Id(freeNode), [Id(node)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), Id(val)), If((BinaryOp(=, Id(head), UnaryOp(-, NumLit(1.0))), Return(Id(node))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(currNode), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([If((BinaryOp(<, ArrayCell(Id(tree), [Id(node), NumLit(0.0)]), ArrayCell(Id(tree), [Id(currNode), NumLit(0.0)])), Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(1.0)]), Id(node)))])), [], Block([If((BinaryOp(!=, ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), UnaryOp(-, NumLit(1.0))), AssignStmt(Id(currNode), ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]))), [], AssignStmt(ArrayCell(Id(tree), [Id(currNode), NumLit(2.0)]), Id(node)))]))])), Return(Id(head))])), FuncDecl(Id(main), [], Block([VarDecl(Id(tree), ArrayType([100.0, 3.0], NumberType), None, None), VarDecl(Id(freeNode), ArrayType([100.0], BoolType), None, None), VarDecl(Id(head), NumberType, None, UnaryOp(-, NumLit(1.0))), CallStmt(Id(initTree), [Id(tree)]), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(freeNode), [Id(i)]), BooleanLit(True))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), Block([VarDecl(Id(val), NumberType, None, CallExpr(Id(readNumber), [])), AssignStmt(Id(head), CallExpr(Id(appendNode), [Id(val), Id(head), Id(tree), Id(freeNode)]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test_369(self):
        # Breadth First Search (BFS)
        input = """number QUEUE[100] <- [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
number HEAD <- 0
number TAIL <- 0
func push(number item) begin 
    QUEUE[TAIL] <- item 
    TAIL <- (TAIL + 1)%100
end 
func pop() begin 
    number item <- QUEUE[HEAD]
    HEAD <- (HEAD + 1)%100
    return item
end
func main() begin
bool graph[10,10] 
var i<-0
for i until i=10 by 1
begin
    var j<-0
    for j until j=10 by 1
        dynamic num <- readNumber()
        if (num=1) graph[i,j] <- true
        else graph[i,j] <- false 
end
dynamic start <- readNumber()
dynamic des <- readNumber()
bool visit[10]
i<-0
for i until i=10 by 1 visit[i] <- false
push(start)
for i until (HEAD = TAIL) by 0
begin
var top <- pop()
visit[top] <- true 
if (top = des) break 
i<-0 
for i until i=10 by 1
    if (not visit[i]) push(i)
end
end
"""
        expect = "Program([VarDecl(Id(QUEUE), ArrayType([100.0], NumberType), None, ArrayLit(NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0), NumLit(0.0))), VarDecl(Id(HEAD), NumberType, None, NumLit(0.0)), VarDecl(Id(TAIL), NumberType, None, NumLit(0.0)), FuncDecl(Id(push), [VarDecl(Id(item), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(QUEUE), [Id(TAIL)]), Id(item)), AssignStmt(Id(TAIL), BinaryOp(%, BinaryOp(+, Id(TAIL), NumLit(1.0)), NumLit(100.0)))])), FuncDecl(Id(pop), [], Block([VarDecl(Id(item), NumberType, None, ArrayCell(Id(QUEUE), [Id(HEAD)])), AssignStmt(Id(HEAD), BinaryOp(%, BinaryOp(+, Id(HEAD), NumLit(1.0)), NumLit(100.0))), Return(Id(item))])), FuncDecl(Id(main), [], Block([VarDecl(Id(graph), ArrayType([10.0, 10.0], BoolType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(j), BinaryOp(=, Id(j), NumLit(10.0)), NumLit(1.0), VarDecl(Id(num), None, dynamic, CallExpr(Id(readNumber), []))), If((BinaryOp(=, Id(num), NumLit(1.0)), AssignStmt(ArrayCell(Id(graph), [Id(i), Id(j)]), BooleanLit(True))), [], AssignStmt(ArrayCell(Id(graph), [Id(i), Id(j)]), BooleanLit(False)))])), VarDecl(Id(start), None, dynamic, CallExpr(Id(readNumber), [])), VarDecl(Id(des), None, dynamic, CallExpr(Id(readNumber), [])), VarDecl(Id(visit), ArrayType([10.0], BoolType), None, None), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(visit), [Id(i)]), BooleanLit(False))), CallStmt(Id(push), [Id(start)]), For(Id(i), BinaryOp(=, Id(HEAD), Id(TAIL)), NumLit(0.0), Block([VarDecl(Id(top), None, var, CallExpr(Id(pop), [])), AssignStmt(ArrayCell(Id(visit), [Id(top)]), BooleanLit(True)), If((BinaryOp(=, Id(top), Id(des)), Break), [], None), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(10.0)), NumLit(1.0), If((UnaryOp(not, ArrayCell(Id(visit), [Id(i)])), CallStmt(Id(push), [Id(i)])), [], None))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 369))
    
    def test_370(self):
        # Find sum of array
        input = """func sum(number a[100], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum
end

func main() begin
    writeNumber(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(sum([2, 0, 2, 4], 4))
end
"""
        expect = "Program([FuncDecl(Id(sum), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(sum), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(Id(sum))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0), NumLit(8.0), NumLit(9.0), NumLit(10.0)), NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(sum), [ArrayLit(NumLit(2.0), NumLit(0.0), NumLit(2.0), NumLit(4.0)), NumLit(4.0)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 370))
    
    def test_371(self):
        # Print array - Iterative approach
        input = """func printArr(number a[100], number length)
begin
    var i <- 0
    for i until i >= length by 1 begin
        writeNumber(a[i])
        writeString(" ")
    end
    writeString("\\n")
end
"""
        expect = "Program([FuncDecl(Id(printArr), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), Block([CallStmt(Id(writeNumber), [ArrayCell(Id(a), [Id(i)])]), CallStmt(Id(writeString), [StringLit( )])])), CallStmt(Id(writeString), [StringLit(\\n)])]))])"
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test_372(self):
        # Print array - Recursive approach
        input = """func printArr(number a[100], number length)
begin
    if (length < 0)
        return
    printArr(a, length - 1)
    writeNumber(a[length - 1])
    writeString(" ")
end
"""
        expect = "Program([FuncDecl(Id(printArr), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<, Id(length), NumLit(0.0)), Return()), [], None), CallStmt(Id(printArr), [Id(a), BinaryOp(-, Id(length), NumLit(1.0))]), CallStmt(Id(writeNumber), [ArrayCell(Id(a), [BinaryOp(-, Id(length), NumLit(1.0))])]), CallStmt(Id(writeString), [StringLit( )])]))])"
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test_373(self):
        # Find maximum in array
        input = """func max(number a[100], number length)
begin
    if (length <= 0)
        return -1e9 ## Represent negative infinity
    var max <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] > max) max <- a[i]
    return max
end
"""
        expect = "Program([FuncDecl(Id(max), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<=, Id(length), NumLit(0.0)), Return(UnaryOp(-, NumLit(1000000000.0)))), [], None), VarDecl(Id(max), None, var, ArrayCell(Id(a), [NumLit(0.0)])), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), If((BinaryOp(>, ArrayCell(Id(a), [Id(i)]), Id(max)), AssignStmt(Id(max), ArrayCell(Id(a), [Id(i)]))), [], None)), Return(Id(max))]))])"
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test_374(self):
        # Find minimum in array
        input = """func min(number a[100], number length)
begin
    if (length <= 0)
        return 1E+9 ## Represent possitive infinity
    var min <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] < min) min <- a[i]
    return min
end
"""
        expect = "Program([FuncDecl(Id(min), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<=, Id(length), NumLit(0.0)), Return(NumLit(1000000000.0))), [], None), VarDecl(Id(min), None, var, ArrayCell(Id(a), [NumLit(0.0)])), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), If((BinaryOp(<, ArrayCell(Id(a), [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(Id(a), [Id(i)]))), [], None)), Return(Id(min))]))])"
        self.assertTrue(TestAST.test(input, expect, 374))
    
    def test_375(self):
        # Decimal to binary representation
        input = """func round(number n)

func dec_to_bin(number n) begin
    if (n < 0) return "not implemented"
    if (n = 0) return "0"
    
    var res <- ""
    var i <- 0
    for i until n <= 0 by 0 begin
        if (n % 2 == 0) res <- "0" ... res
        else res <- "1" ... res
        n <- round(n/2)
    end
    
    return res
end

func round(number n) return n - n % 1

func main() begin
    writeNumber(dec_to_bin(10))
    writeNumber(dec_to_bin(100))
    writeNumber(dec_to_bin(1000))
end
"""
        expect = "Program([FuncDecl(Id(round), [VarDecl(Id(n), NumberType, None, None)], None), FuncDecl(Id(dec_to_bin), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<, Id(n), NumLit(0.0)), Return(StringLit(not implemented))), [], None), If((BinaryOp(=, Id(n), NumLit(0.0)), Return(StringLit(0))), [], None), VarDecl(Id(res), None, var, StringLit()), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(n), NumLit(0.0)), NumLit(0.0), Block([If((BinaryOp(==, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)), AssignStmt(Id(res), BinaryOp(..., StringLit(0), Id(res)))), [], AssignStmt(Id(res), BinaryOp(..., StringLit(1), Id(res)))), AssignStmt(Id(n), CallExpr(Id(round), [BinaryOp(/, Id(n), NumLit(2.0))]))])), Return(Id(res))])), FuncDecl(Id(round), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(-, Id(n), BinaryOp(%, Id(n), NumLit(1.0))))), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(dec_to_bin), [NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(dec_to_bin), [NumLit(100.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(dec_to_bin), [NumLit(1000.0)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 375))
    
    def test_376(self):
        # Greatest Common Divisor (GCD)
        input = """func gcd(number a, number b)
begin
    if (b = 0) return a
    return gcd(b, a % b)
end

func main() begin
    writeNumber(gcd(6, 9))
    writeNumber(gcd(24, 16))
    writeNumber(gcd(1, 7))
end
"""
        expect = "Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(=, Id(b), NumLit(0.0)), Return(Id(a))), [], None), Return(CallExpr(Id(gcd), [Id(b), BinaryOp(%, Id(a), Id(b))]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(6.0), NumLit(9.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(24.0), NumLit(16.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(gcd), [NumLit(1.0), NumLit(7.0)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test_377(self):
        # Palindrome string
        input = """func isPalindrome(string s[100], number left, number right)
begin
    ## Because ZCode string cannot be indexed, cut, etc...
    ## We assume that s is an array of 1-length strings, aka characters
    ## And we will check whether characters from left to right (inclusively) can make a palindrome string
    
    if (left > right + 1) return false
    if ((left = right) or (left = right + 1)) return true
    return (s[left] == s[right]) and isPalindrome(s, left + 1, right - 1)
end

func main()
begin
    isPalindrome(["m", "o", "m"], 0, 2)
    isPalindrome(["d", "o", "g", "e", "e", "s", "e", "s", "e", "e", "g", "o", "d"], 0, 12)
end
"""
        expect = "Program([FuncDecl(Id(isPalindrome), [VarDecl(Id(s), ArrayType([100.0], StringType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(>, Id(left), BinaryOp(+, Id(right), NumLit(1.0))), Return(BooleanLit(False))), [], None), If((BinaryOp(or, BinaryOp(=, Id(left), Id(right)), BinaryOp(=, Id(left), BinaryOp(+, Id(right), NumLit(1.0)))), Return(BooleanLit(True))), [], None), Return(BinaryOp(and, BinaryOp(==, ArrayCell(Id(s), [Id(left)]), ArrayCell(Id(s), [Id(right)])), CallExpr(Id(isPalindrome), [Id(s), BinaryOp(+, Id(left), NumLit(1.0)), BinaryOp(-, Id(right), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(isPalindrome), [ArrayLit(StringLit(m), StringLit(o), StringLit(m)), NumLit(0.0), NumLit(2.0)]), CallStmt(Id(isPalindrome), [ArrayLit(StringLit(d), StringLit(o), StringLit(g), StringLit(e), StringLit(e), StringLit(s), StringLit(e), StringLit(s), StringLit(e), StringLit(e), StringLit(g), StringLit(o), StringLit(d)), NumLit(0.0), NumLit(12.0)])]))])"
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test_378(self):
        # Fibonacci sequence
        input = """number res[100]

func fib(number n)
begin
    if (res[n] != -1) return res[n]
    res[n] <- fib(n - 1) + fib(n - 2)
    return res[n]
end

func main() begin
    res[0] <- 0
    res[1] <- 1
    
    var i <- 2
    for i until i = 100 by 1 res[i] <- -1
    
    writeNumber(fib(5))
    writeNumber(fib(10))
    writeNumber(fib(50))
end
"""
        expect = "Program([VarDecl(Id(res), ArrayType([100.0], NumberType), None, None), FuncDecl(Id(fib), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(!=, ArrayCell(Id(res), [Id(n)]), UnaryOp(-, NumLit(1.0))), Return(ArrayCell(Id(res), [Id(n)]))), [], None), AssignStmt(ArrayCell(Id(res), [Id(n)]), BinaryOp(+, CallExpr(Id(fib), [BinaryOp(-, Id(n), NumLit(1.0))]), CallExpr(Id(fib), [BinaryOp(-, Id(n), NumLit(2.0))]))), Return(ArrayCell(Id(res), [Id(n)]))])), FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(res), [NumLit(0.0)]), NumLit(0.0)), AssignStmt(ArrayCell(Id(res), [NumLit(1.0)]), NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(=, Id(i), NumLit(100.0)), NumLit(1.0), AssignStmt(ArrayCell(Id(res), [Id(i)]), UnaryOp(-, NumLit(1.0)))), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(5.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(10.0)])]), CallStmt(Id(writeNumber), [CallExpr(Id(fib), [NumLit(50.0)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test_379(self):
        # Check whether one number is divisible the other (Example 1 in spec)
        input = """func areDivisors(number num1, number num2)
    return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
    end
"""
        expect = "Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 379))
    
    def test_380(self):
        # Check prime number (Example 2 in spec)
        input = """func isPrime(number x)

func main()
    begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
    end

func isPrime(number x)
    begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        return true
    end
"""
        expect = "Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))])), FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"
        self.assertTrue(TestAST.test(input, expect, 380))
    
    def test_381(self):
        # Tower of Hanoi
        input = """func print(string src, string dst, string aux)

func tower_of_hanoi(number n, string src, string dst, string aux)
begin
    if (n = 1) print(src, dst)
    else begin
        tower_of_hanoi(n - 1, src, aux, dst)
        tower_of_hanoi(1, src, dst, aux)
        tower_of_hanoi(n - 1, aux, dst, src)
    end
end

func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    output <- output ... "\\n"
    writeString(output)
end
"""
        expect = "Program([FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None), VarDecl(Id(aux), StringType, None, None)], None), FuncDecl(Id(tower_of_hanoi), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None), VarDecl(Id(aux), StringType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(1.0)), CallStmt(Id(print), [Id(src), Id(dst)])), [], Block([CallStmt(Id(tower_of_hanoi), [BinaryOp(-, Id(n), NumLit(1.0)), Id(src), Id(aux), Id(dst)]), CallStmt(Id(tower_of_hanoi), [NumLit(1.0), Id(src), Id(dst), Id(aux)]), CallStmt(Id(tower_of_hanoi), [BinaryOp(-, Id(n), NumLit(1.0)), Id(aux), Id(dst), Id(src)])]))])), FuncDecl(Id(print), [VarDecl(Id(src), StringType, None, None), VarDecl(Id(dst), StringType, None, None)], Block([AssignStmt(Id(output), StringLit(Move 1 disk from tower )), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(src))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit( to tower ))), AssignStmt(Id(output), BinaryOp(..., Id(output), Id(des))), AssignStmt(Id(output), BinaryOp(..., Id(output), StringLit(\\n))), CallStmt(Id(writeString), [Id(output)])]))])"
        self.assertTrue(TestAST.test(input, expect, 381))
    
    def test_382(self):
        # N-queens problem
        # Print one solution of N-queens problem
        input = """func printSolution(number board[100, 100], number n)
begin
    var i <- 0
    var j <- 0
	for i until i >= n by 1 begin
		for j until j >= n by 1
            if (board[i, j]) writeString("Q ")
		    else writeString(". ")
		printf("\\n")
	end
end

func isSafe(number board[100, 100], number n, number row, number col) begin
	var i <- 0
    var j <- 0
	for i until i >= col by 1
		if (board[row, i])
			return false
    
    i <- row
    j <- col
	for i until ((i < 0) or (j < 0)) by -1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
    
    i <- row
    j <- col
	for i until ((i >= n) or (j < 0)) by 1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
	
    return true
end

func solverec(number board[100, 100], number col, number n) begin
    if (col >= n) return true
    
    var i <- 0
    for i until i >= n by 1 begin
		if (isSafe(board, n, i, col)) begin
			board[i, col] <- 1
			if (solverec(board, col + 1, n)) return true
			board[i, col] <- 0
		end
	end
	
    return false
end

func solve(number n)
begin
    number board[100, 100]
    var i <- 0
    var j <- 0
    for i until i >= n by 1
        for j until j >= n by 1
            board[i, j] <- 0
    
    if (not solverec(board, 0, n)) writeString("No solution")
    else printSolution(board, n)
end
"""
        expect = "Program([FuncDecl(Id(printSolution), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), If((ArrayCell(Id(board), [Id(i), Id(j)]), CallStmt(Id(writeString), [StringLit(Q )])), [], CallStmt(Id(writeString), [StringLit(. )]))), CallStmt(Id(printf), [StringLit(\\n)])]))])), FuncDecl(Id(isSafe), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(row), NumberType, None, None), VarDecl(Id(col), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(col)), NumLit(1.0), If((ArrayCell(Id(board), [Id(row), Id(i)]), Return(BooleanLit(False))), [], None)), AssignStmt(Id(i), Id(row)), AssignStmt(Id(j), Id(col)), For(Id(i), BinaryOp(or, BinaryOp(<, Id(i), NumLit(0.0)), BinaryOp(<, Id(j), NumLit(0.0))), UnaryOp(-, NumLit(1.0)), Block([If((ArrayCell(Id(board), [Id(i), Id(j)]), Return(BooleanLit(False))), [], None), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), AssignStmt(Id(i), Id(row)), AssignStmt(Id(j), Id(col)), For(Id(i), BinaryOp(or, BinaryOp(>=, Id(i), Id(n)), BinaryOp(<, Id(j), NumLit(0.0))), NumLit(1.0), Block([If((ArrayCell(Id(board), [Id(i), Id(j)]), Return(BooleanLit(False))), [], None), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), Return(BooleanLit(True))])), FuncDecl(Id(solverec), [VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(col), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(>=, Id(col), Id(n)), Return(BooleanLit(True))), [], None), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([If((CallExpr(Id(isSafe), [Id(board), Id(n), Id(i), Id(col)]), Block([AssignStmt(ArrayCell(Id(board), [Id(i), Id(col)]), NumLit(1.0)), If((CallExpr(Id(solverec), [Id(board), BinaryOp(+, Id(col), NumLit(1.0)), Id(n)]), Return(BooleanLit(True))), [], None), AssignStmt(ArrayCell(Id(board), [Id(i), Id(col)]), NumLit(0.0))])), [], None)])), Return(BooleanLit(False))])), FuncDecl(Id(solve), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(board), ArrayType([100.0, 100.0], NumberType), None, None), VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), AssignStmt(ArrayCell(Id(board), [Id(i), Id(j)]), NumLit(0.0)))), If((UnaryOp(not, CallExpr(Id(solverec), [Id(board), NumLit(0.0), Id(n)])), CallStmt(Id(writeString), [StringLit(No solution)])), [], CallStmt(Id(printSolution), [Id(board), Id(n)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 382))
    
    def test_383(self):
        # Knight's tour problem
        input = """number sol[10, 10]
number xMove[8] <- [ 2, 1, -1, -2, -2, -1,  1,  2 ]
number yMove[8] <- [ 1, 2,  2,  1, -1, -2, -2, -1 ]

func chkCell(number x, number y, number n)
    return (x >= 0) and (x < n) and (y >= 0) and (y < n) and (sol[x, y] == -1)

func solverec(number x, number y, number move_ith, number n) begin
    if (move_ith == n*n) return true
    number k <- 0
    number xNext
    number yNext
    for k until k = 8 by 1 begin
        xNext <- x + xMove[k]
        yNext <- y + yMove[k]
        if (chkCell(xNext, yNext, n)) begin
            sol[xNext, yNext] <- move_ith
            move_ith <- move_ith + 1
            if (solverec(xNext, yNext, move_ith, n)) return true
            move_ith <- move_ith - 1
            sol[xNext, yNext] <- -1
        end
    end
    return false
end

func solve(number n) begin
    var i <- 0
    var j <- 0
    for i until i >= n by 1
        for j until j >= n by 1
            sol[i, j] <- -1
    sol[0, 0] <- 0
    
    return solverec(0, 0, 1, n) = 1
end
"""
        expect = "Program([VarDecl(Id(sol), ArrayType([10.0, 10.0], NumberType), None, None), VarDecl(Id(xMove), ArrayType([8.0], NumberType), None, ArrayLit(NumLit(2.0), NumLit(1.0), UnaryOp(-, NumLit(1.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(1.0)), NumLit(1.0), NumLit(2.0))), VarDecl(Id(yMove), ArrayType([8.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(2.0), NumLit(1.0), UnaryOp(-, NumLit(1.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(1.0)))), FuncDecl(Id(chkCell), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(and, BinaryOp(and, BinaryOp(and, BinaryOp(and, BinaryOp(>=, Id(x), NumLit(0.0)), BinaryOp(<, Id(x), Id(n))), BinaryOp(>=, Id(y), NumLit(0.0))), BinaryOp(<, Id(y), Id(n))), BinaryOp(==, ArrayCell(Id(sol), [Id(x), Id(y)]), UnaryOp(-, NumLit(1.0)))))), FuncDecl(Id(solverec), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), NumberType, None, None), VarDecl(Id(move_ith), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(move_ith), BinaryOp(*, Id(n), Id(n))), Return(BooleanLit(True))), [], None), VarDecl(Id(k), NumberType, None, NumLit(0.0)), VarDecl(Id(xNext), NumberType, None, None), VarDecl(Id(yNext), NumberType, None, None), For(Id(k), BinaryOp(=, Id(k), NumLit(8.0)), NumLit(1.0), Block([AssignStmt(Id(xNext), BinaryOp(+, Id(x), ArrayCell(Id(xMove), [Id(k)]))), AssignStmt(Id(yNext), BinaryOp(+, Id(y), ArrayCell(Id(yMove), [Id(k)]))), If((CallExpr(Id(chkCell), [Id(xNext), Id(yNext), Id(n)]), Block([AssignStmt(ArrayCell(Id(sol), [Id(xNext), Id(yNext)]), Id(move_ith)), AssignStmt(Id(move_ith), BinaryOp(+, Id(move_ith), NumLit(1.0))), If((CallExpr(Id(solverec), [Id(xNext), Id(yNext), Id(move_ith), Id(n)]), Return(BooleanLit(True))), [], None), AssignStmt(Id(move_ith), BinaryOp(-, Id(move_ith), NumLit(1.0))), AssignStmt(ArrayCell(Id(sol), [Id(xNext), Id(yNext)]), UnaryOp(-, NumLit(1.0)))])), [], None)])), Return(BooleanLit(False))])), FuncDecl(Id(solve), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), AssignStmt(ArrayCell(Id(sol), [Id(i), Id(j)]), UnaryOp(-, NumLit(1.0))))), AssignStmt(ArrayCell(Id(sol), [NumLit(0.0), NumLit(0.0)]), NumLit(0.0)), Return(BinaryOp(=, CallExpr(Id(solverec), [NumLit(0.0), NumLit(0.0), NumLit(1.0), Id(n)]), NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 383))
    
    def test_384(self):
        # Linear search
        input = """func find(number arr[100], number length, number element)
begin
    var i <- 0
    for i until i >= length by 1
        if (arr[i] = element) return i
    return -1
end
"""
        expect = "Program([FuncDecl(Id(find), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(element), NumberType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), If((BinaryOp(=, ArrayCell(Id(arr), [Id(i)]), Id(element)), Return(Id(i))), [], None)), Return(UnaryOp(-, NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 384))
    
    def test_385(self):
        # Binary search
        input = """func find(number arr[100], number length, number element)
begin
    var left <- 0
    var right <- length - 1
    number mid
    for _ until left > right by 0 begin
        mid <- (left + right) / 2
        if (element = arr[mid]) return mid
        elif (element > arr[mid]) left <- mid + 1
        else right <- mid - 1
    end
    return -1
end
"""
        expect = "Program([FuncDecl(Id(find), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(element), NumberType, None, None)], Block([VarDecl(Id(left), None, var, NumLit(0.0)), VarDecl(Id(right), None, var, BinaryOp(-, Id(length), NumLit(1.0))), VarDecl(Id(mid), NumberType, None, None), For(Id(_), BinaryOp(>, Id(left), Id(right)), NumLit(0.0), Block([AssignStmt(Id(mid), BinaryOp(/, BinaryOp(+, Id(left), Id(right)), NumLit(2.0))), If((BinaryOp(=, Id(element), ArrayCell(Id(arr), [Id(mid)])), Return(Id(mid))), [(BinaryOp(>, Id(element), ArrayCell(Id(arr), [Id(mid)])), AssignStmt(Id(left), BinaryOp(+, Id(mid), NumLit(1.0))))], AssignStmt(Id(right), BinaryOp(-, Id(mid), NumLit(1.0))))])), Return(UnaryOp(-, NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 385))
    
    def test_386(self):
        # Interpolation search
        input = """func interpolationSearch(number arr[100], number element, number left, number right)
begin
    if ((left > right) or (element < arr[left]) or (element > arr[right])) return -1
    number pos <- left + (right - left)*(element - arr[left])/(arr[right] - arr[left])
    if (element = arr[pos]) return pos
    else if (element < arr[pos]) return interpolationSearch(arr, element, left, pos-1)
    return interpolationSearch(arr, element, pos+1, right)
end
"""
        expect = "Program([FuncDecl(Id(interpolationSearch), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(element), NumberType, None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(or, BinaryOp(>, Id(left), Id(right)), BinaryOp(<, Id(element), ArrayCell(Id(arr), [Id(left)]))), BinaryOp(>, Id(element), ArrayCell(Id(arr), [Id(right)]))), Return(UnaryOp(-, NumLit(1.0)))), [], None), VarDecl(Id(pos), NumberType, None, BinaryOp(+, Id(left), BinaryOp(/, BinaryOp(*, BinaryOp(-, Id(right), Id(left)), BinaryOp(-, Id(element), ArrayCell(Id(arr), [Id(left)]))), BinaryOp(-, ArrayCell(Id(arr), [Id(right)]), ArrayCell(Id(arr), [Id(left)]))))), If((BinaryOp(=, Id(element), ArrayCell(Id(arr), [Id(pos)])), Return(Id(pos))), [], If((BinaryOp(<, Id(element), ArrayCell(Id(arr), [Id(pos)])), Return(CallExpr(Id(interpolationSearch), [Id(arr), Id(element), Id(left), BinaryOp(-, Id(pos), NumLit(1.0))]))), [], None)), Return(CallExpr(Id(interpolationSearch), [Id(arr), Id(element), BinaryOp(+, Id(pos), NumLit(1.0)), Id(right)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 386))
    
    def test_387(self):
        # Jump search
        input = """func jumpSearch(number arr[100], number n, number element)
begin
    number m <- sqrt(n)
    number k <- 0
    for k until k*m >= n by 1 begin
        if (element = arr[k*m]) return k*m
        if (element < arr[k*m]) break
    end
    k <- k - 1
    number i <- k*m + 1
    for i until i >= (k+1)*m by 1 begin
        if ((i >= n) or (element < arr[i])) break
        if (element = arr[i]) return i
    end
    return -1
end
"""
        expect = "Program([FuncDecl(Id(jumpSearch), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(element), NumberType, None, None)], Block([VarDecl(Id(m), NumberType, None, CallExpr(Id(sqrt), [Id(n)])), VarDecl(Id(k), NumberType, None, NumLit(0.0)), For(Id(k), BinaryOp(>=, BinaryOp(*, Id(k), Id(m)), Id(n)), NumLit(1.0), Block([If((BinaryOp(=, Id(element), ArrayCell(Id(arr), [BinaryOp(*, Id(k), Id(m))])), Return(BinaryOp(*, Id(k), Id(m)))), [], None), If((BinaryOp(<, Id(element), ArrayCell(Id(arr), [BinaryOp(*, Id(k), Id(m))])), Break), [], None)])), AssignStmt(Id(k), BinaryOp(-, Id(k), NumLit(1.0))), VarDecl(Id(i), NumberType, None, BinaryOp(+, BinaryOp(*, Id(k), Id(m)), NumLit(1.0))), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(*, BinaryOp(+, Id(k), NumLit(1.0)), Id(m))), NumLit(1.0), Block([If((BinaryOp(or, BinaryOp(>=, Id(i), Id(n)), BinaryOp(<, Id(element), ArrayCell(Id(arr), [Id(i)]))), Break), [], None), If((BinaryOp(=, Id(element), ArrayCell(Id(arr), [Id(i)])), Return(Id(i))), [], None)])), Return(UnaryOp(-, NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 387))
    
    def test_388(self):
        # Bubble sort
        input = """func bubbleSort(number arr[100], number length)
begin
    number i <- 1
    for i until i >= length by 1 begin
        number j <- length - 1
        for j until j < i by -1
            if (arr[j] < arr[j - 1]) swap(arr, j, j - 1)
    end
end

func swap(number arr[100], number i, number j) begin
    var tmp <- arr[i]
    arr[i] <- arr[j]
    arr[j] <- tmp
end
"""
        expect = "Program([FuncDecl(Id(bubbleSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), Block([VarDecl(Id(j), NumberType, None, BinaryOp(-, Id(length), NumLit(1.0))), For(Id(j), BinaryOp(<, Id(j), Id(i)), UnaryOp(-, NumLit(1.0)), If((BinaryOp(<, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(-, Id(j), NumLit(1.0))])), CallStmt(Id(swap), [Id(arr), Id(j), BinaryOp(-, Id(j), NumLit(1.0))])), [], None))]))])), FuncDecl(Id(swap), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None)], Block([VarDecl(Id(tmp), None, var, ArrayCell(Id(arr), [Id(i)])), AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), AssignStmt(ArrayCell(Id(arr), [Id(j)]), Id(tmp))]))])"
        self.assertTrue(TestAST.test(input, expect, 388))
    
    def test_389(self):
        # Selection sort
        input = """func selectionSort(number arr[100], number length)
begin
    number i <- 0
    for i until i >= length-1 by 1 begin
        number min_idx <- i
        number j <- i + 1
        for j until j >= length by 1
            if (arr[j] < arr[min_idx]) min_idx <- j
        swap(arr, i, min_idx)
    end
end
"""
        expect = "Program([FuncDecl(Id(selectionSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(length), NumLit(1.0))), NumLit(1.0), Block([VarDecl(Id(min_idx), NumberType, None, Id(i)), VarDecl(Id(j), NumberType, None, BinaryOp(+, Id(i), NumLit(1.0))), For(Id(j), BinaryOp(>=, Id(j), Id(length)), NumLit(1.0), If((BinaryOp(<, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [Id(min_idx)])), AssignStmt(Id(min_idx), Id(j))), [], None)), CallStmt(Id(swap), [Id(arr), Id(i), Id(min_idx)])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 389))
    
    def test_390(self):
        # Insertion sort
        input = """func insertionSort(number arr[100], number length)
begin
    number i <- 1
    for i until i >= length by 1 begin
        number tmp <- arr[i]
        number j <- i-1
        for j until ((j < 0) or (tmp >= arr[j])) by -1
            arr[j+1] <- arr[j]
        arr[j+1] <- tmp
    end
end
"""
        expect = "Program([FuncDecl(Id(insertionSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), Block([VarDecl(Id(tmp), NumberType, None, ArrayCell(Id(arr), [Id(i)])), VarDecl(Id(j), NumberType, None, BinaryOp(-, Id(i), NumLit(1.0))), For(Id(j), BinaryOp(or, BinaryOp(<, Id(j), NumLit(0.0)), BinaryOp(>=, Id(tmp), ArrayCell(Id(arr), [Id(j)]))), UnaryOp(-, NumLit(1.0)), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))]), ArrayCell(Id(arr), [Id(j)]))), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))]), Id(tmp))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test_391(self):
        # Shell sort
        input = """func sortSegment(number arr[100], number length, number segment_idx, number k)
begin
    number i <- segment_idx + k
    for i until i >= length by k begin
        number tmp <- arr[i]
        number j <- i-k
        for j until ((j < 0) or (tmp >= arr[j])) by -k
            arr[j+k] <- arr[j]
        arr[j+k] <- tmp
    end
end

func shellSort(number arr[100], number length, number num_of_segment_list[10], number num_phases) begin
    number i <- num_phases-1
    for i until i < 0 by -1 begin
        number segment <- 0
        for segment until segment > num_of_segment_list[i] by 1
            sortSegment(arr, length, segment, num_of_segment_list[i])
    end
end
"""
        expect = "Program([FuncDecl(Id(sortSegment), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(segment_idx), NumberType, None, None), VarDecl(Id(k), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, BinaryOp(+, Id(segment_idx), Id(k))), For(Id(i), BinaryOp(>=, Id(i), Id(length)), Id(k), Block([VarDecl(Id(tmp), NumberType, None, ArrayCell(Id(arr), [Id(i)])), VarDecl(Id(j), NumberType, None, BinaryOp(-, Id(i), Id(k))), For(Id(j), BinaryOp(or, BinaryOp(<, Id(j), NumLit(0.0)), BinaryOp(>=, Id(tmp), ArrayCell(Id(arr), [Id(j)]))), UnaryOp(-, Id(k)), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), Id(k))]), ArrayCell(Id(arr), [Id(j)]))), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), Id(k))]), Id(tmp))]))])), FuncDecl(Id(shellSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(num_of_segment_list), ArrayType([10.0], NumberType), None, None), VarDecl(Id(num_phases), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, BinaryOp(-, Id(num_phases), NumLit(1.0))), For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), Block([VarDecl(Id(segment), NumberType, None, NumLit(0.0)), For(Id(segment), BinaryOp(>, Id(segment), ArrayCell(Id(num_of_segment_list), [Id(i)])), NumLit(1.0), CallStmt(Id(sortSegment), [Id(arr), Id(length), Id(segment), ArrayCell(Id(num_of_segment_list), [Id(i)])]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 391))
    
    def test_392(self):
        # Merge sort
        input = """func round(number n) return n - n % 1
func merge(number arr[100], number left, number right, number mid) begin
    number left_length <- mid - left + 1
    number right_length <- right - mid
    number arr_left[50]
    number arr_right[50]
    
    number i <- 0
    number j <- 0
    
    for i until i >= left_length by 1
        arr_left[i] <- arr[left + i]
    for j until j >= right_length by 1
        arr_right[j] <- arr[mid + 1 + j]
    
    number k <- left
    for k until k > right by 1 begin
        if ((i < left_length) and ((j >= right_length) or (arr_left[i] <= arr_right[j]))) begin
            arr[k] <- arr_left[i]
            i <- i + 1
        end
        else begin
            arr[k] <- arr_right[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right) begin
    if (left >= right) return
    number mid <- round((left + right) / 2)
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, right, mid)
end
"""
        expect = "Program([FuncDecl(Id(round), [VarDecl(Id(n), NumberType, None, None)], Return(BinaryOp(-, Id(n), BinaryOp(%, Id(n), NumLit(1.0))))), FuncDecl(Id(merge), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None), VarDecl(Id(mid), NumberType, None, None)], Block([VarDecl(Id(left_length), NumberType, None, BinaryOp(+, BinaryOp(-, Id(mid), Id(left)), NumLit(1.0))), VarDecl(Id(right_length), NumberType, None, BinaryOp(-, Id(right), Id(mid))), VarDecl(Id(arr_left), ArrayType([50.0], NumberType), None, None), VarDecl(Id(arr_right), ArrayType([50.0], NumberType), None, None), VarDecl(Id(i), NumberType, None, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(left_length)), NumLit(1.0), AssignStmt(ArrayCell(Id(arr_left), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(left), Id(i))]))), For(Id(j), BinaryOp(>=, Id(j), Id(right_length)), NumLit(1.0), AssignStmt(ArrayCell(Id(arr_right), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, BinaryOp(+, Id(mid), NumLit(1.0)), Id(j))]))), VarDecl(Id(k), NumberType, None, Id(left)), For(Id(k), BinaryOp(>, Id(k), Id(right)), NumLit(1.0), Block([If((BinaryOp(and, BinaryOp(<, Id(i), Id(left_length)), BinaryOp(or, BinaryOp(>=, Id(j), Id(right_length)), BinaryOp(<=, ArrayCell(Id(arr_left), [Id(i)]), ArrayCell(Id(arr_right), [Id(j)])))), Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(arr_left), [Id(i)])), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), [], Block([AssignStmt(ArrayCell(Id(arr), [Id(k)]), ArrayCell(Id(arr_right), [Id(j)])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0)))]))]))])), FuncDecl(Id(mergeSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(>=, Id(left), Id(right)), Return()), [], None), VarDecl(Id(mid), NumberType, None, CallExpr(Id(round), [BinaryOp(/, BinaryOp(+, Id(left), Id(right)), NumLit(2.0))])), CallStmt(Id(mergeSort), [Id(arr), Id(left), Id(mid)]), CallStmt(Id(mergeSort), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(right)]), CallStmt(Id(merge), [Id(arr), Id(left), Id(right), Id(mid)])]))])"
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test_393(self):
        # Quick sort
        input = """func swap(number arr[100], number i, number j)
func partition(number arr[100], number left, number right) begin
    number pivot <- arr[left]
    number i <- left + 1
    number j <- right
    
    for i until i > j by 0 begin
        for i until ((i > j) or (arr[i] >= pivot)) by 1 begin
        end
        for j until ((i > j) or (arr[j] < pivot)) by -1 begin
        end
        if (i < j) begin
            swap(arr, i, j)
            i <- i + 1
            j <- j - 1
        end
    end
    swap(arr, j, left)
    return j
end

func quickSort(number arr[100], number left, number right) begin
    if (left >= right) return
    number pos <- partition(arr, left, right)
    quickSort(arr, left, pos - 1)
    quickSort(arr, pos + 1, right)
end
"""
        expect = "Program([FuncDecl(Id(swap), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None)], None), FuncDecl(Id(partition), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([VarDecl(Id(pivot), NumberType, None, ArrayCell(Id(arr), [Id(left)])), VarDecl(Id(i), NumberType, None, BinaryOp(+, Id(left), NumLit(1.0))), VarDecl(Id(j), NumberType, None, Id(right)), For(Id(i), BinaryOp(>, Id(i), Id(j)), NumLit(0.0), Block([For(Id(i), BinaryOp(or, BinaryOp(>, Id(i), Id(j)), BinaryOp(>=, ArrayCell(Id(arr), [Id(i)]), Id(pivot))), NumLit(1.0), Block([])), For(Id(j), BinaryOp(or, BinaryOp(>, Id(i), Id(j)), BinaryOp(<, ArrayCell(Id(arr), [Id(j)]), Id(pivot))), UnaryOp(-, NumLit(1.0)), Block([])), If((BinaryOp(<, Id(i), Id(j)), Block([CallStmt(Id(swap), [Id(arr), Id(i), Id(j)]), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0))), AssignStmt(Id(j), BinaryOp(-, Id(j), NumLit(1.0)))])), [], None)])), CallStmt(Id(swap), [Id(arr), Id(j), Id(left)]), Return(Id(j))])), FuncDecl(Id(quickSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(left), NumberType, None, None), VarDecl(Id(right), NumberType, None, None)], Block([If((BinaryOp(>=, Id(left), Id(right)), Return()), [], None), VarDecl(Id(pos), NumberType, None, CallExpr(Id(partition), [Id(arr), Id(left), Id(right)])), CallStmt(Id(quickSort), [Id(arr), Id(left), BinaryOp(-, Id(pos), NumLit(1.0))]), CallStmt(Id(quickSort), [Id(arr), BinaryOp(+, Id(pos), NumLit(1.0)), Id(right)])]))])"
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test_394(self):
        # Heap sort
        input = """func heapSort(number arr[100], number length)
begin
    buildHeap(arr, length) ## Build heap algorithm in next testcase
    
    var i <- length - 1
    for i until i < 0 by -1 begin
        swap(arr, 0, i)
        reHeapDown(arr, i, 0)
    end
end
"""
        expect = "Program([FuncDecl(Id(heapSort), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([CallStmt(Id(buildHeap), [Id(arr), Id(length)]), VarDecl(Id(i), None, var, BinaryOp(-, Id(length), NumLit(1.0))), For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), Block([CallStmt(Id(swap), [Id(arr), NumLit(0.0), Id(i)]), CallStmt(Id(reHeapDown), [Id(arr), Id(i), NumLit(0.0)])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 394))
    
    def test_395(self):
        # Build heap
        input = """func reHeapDown(number arr[100], number length, number index) begin
    number l <- 2*index + 1
    number r <- 2*index + 2
    number largest <- index
    if ((l < length) and (arr[l] > arr[largest])) largest <- l
    if ((r < length) and (arr[r] > arr[largest])) largest <- r
    if (largest != index) begin
        swap(arr, index, largest)
        reHeapDown(arr, length, largest)
    end
end

func buildHeap(number arr[100], number length) begin
    number internal <- round(length/2) - 1
    for internal until internal < 0 by -1
        reHeapDown(arr, length, internal)
end
"""
        expect = "Program([FuncDecl(Id(reHeapDown), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(index), NumberType, None, None)], Block([VarDecl(Id(l), NumberType, None, BinaryOp(+, BinaryOp(*, NumLit(2.0), Id(index)), NumLit(1.0))), VarDecl(Id(r), NumberType, None, BinaryOp(+, BinaryOp(*, NumLit(2.0), Id(index)), NumLit(2.0))), VarDecl(Id(largest), NumberType, None, Id(index)), If((BinaryOp(and, BinaryOp(<, Id(l), Id(length)), BinaryOp(>, ArrayCell(Id(arr), [Id(l)]), ArrayCell(Id(arr), [Id(largest)]))), AssignStmt(Id(largest), Id(l))), [], None), If((BinaryOp(and, BinaryOp(<, Id(r), Id(length)), BinaryOp(>, ArrayCell(Id(arr), [Id(r)]), ArrayCell(Id(arr), [Id(largest)]))), AssignStmt(Id(largest), Id(r))), [], None), If((BinaryOp(!=, Id(largest), Id(index)), Block([CallStmt(Id(swap), [Id(arr), Id(index), Id(largest)]), CallStmt(Id(reHeapDown), [Id(arr), Id(length), Id(largest)])])), [], None)])), FuncDecl(Id(buildHeap), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([VarDecl(Id(internal), NumberType, None, BinaryOp(-, CallExpr(Id(round), [BinaryOp(/, Id(length), NumLit(2.0))]), NumLit(1.0))), For(Id(internal), BinaryOp(<, Id(internal), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), CallStmt(Id(reHeapDown), [Id(arr), Id(length), Id(internal)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 395))
    
    def test_396(self):
        # Insert an element into a heap
        input = """func reHeapUp(number arr[100], number length, number index) begin
    if (index = 0) return
    number parent <- round((index - 1)/2)
    if (arr[index] > arr[parent]) begin
        swap(arr, index, parent)
        reHeapUp(arr, length, parent)
    end
end

func insertHeap(number arr[100], number length, number element)
begin
    arr[length] <- element
    length <- length + 1
    reHeapUp(arr, length, length - 1)
    return length
end
"""
        expect = "Program([FuncDecl(Id(reHeapUp), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(index), NumberType, None, None)], Block([If((BinaryOp(=, Id(index), NumLit(0.0)), Return()), [], None), VarDecl(Id(parent), NumberType, None, CallExpr(Id(round), [BinaryOp(/, BinaryOp(-, Id(index), NumLit(1.0)), NumLit(2.0))])), If((BinaryOp(>, ArrayCell(Id(arr), [Id(index)]), ArrayCell(Id(arr), [Id(parent)])), Block([CallStmt(Id(swap), [Id(arr), Id(index), Id(parent)]), CallStmt(Id(reHeapUp), [Id(arr), Id(length), Id(parent)])])), [], None)])), FuncDecl(Id(insertHeap), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None), VarDecl(Id(element), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(arr), [Id(length)]), Id(element)), AssignStmt(Id(length), BinaryOp(+, Id(length), NumLit(1.0))), CallStmt(Id(reHeapUp), [Id(arr), Id(length), BinaryOp(-, Id(length), NumLit(1.0))]), Return(Id(length))]))])"
        self.assertTrue(TestAST.test(input, expect, 396))
    
    def test_397(self):
        # Delete an element from a heap
        input = """func removeHeap(number arr[100], number length)
begin
    if (length <= 0) return
    var deleted <- arr[0]
    arr[0] <- arr[length - 1]
    length <- length - 1
    reHeapDown(arr, length, 0)
    return deleted
end
"""
        expect = "Program([FuncDecl(Id(removeHeap), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(length), NumberType, None, None)], Block([If((BinaryOp(<=, Id(length), NumLit(0.0)), Return()), [], None), VarDecl(Id(deleted), None, var, ArrayCell(Id(arr), [NumLit(0.0)])), AssignStmt(ArrayCell(Id(arr), [NumLit(0.0)]), ArrayCell(Id(arr), [BinaryOp(-, Id(length), NumLit(1.0))])), AssignStmt(Id(length), BinaryOp(-, Id(length), NumLit(1.0))), CallStmt(Id(reHeapDown), [Id(arr), Id(length), NumLit(0.0)]), Return(Id(deleted))]))])"
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test_398(self):
        # Longest Increasing Subsequence (LIS)
        # Print the length of the longest increasing subsequence of array
        input = """func lis(number arr[100], number n) begin
    number lis[100]
    lis[0] <- 1
    
    number i <- 1
    for i until i >= n by 1 begin
        lis[i] <- 1
        
        number j <- 0
        for j until j >= i by 1
            if ((arr[i] > arr[j]) and (lis[j] + 1 > lis[i]))
                lis[i] <- lis[j] + 1
    end
    return max(lis, n)
end
"""
        expect = "Program([FuncDecl(Id(lis), [VarDecl(Id(arr), ArrayType([100.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(lis), ArrayType([100.0], NumberType), None, None), AssignStmt(ArrayCell(Id(lis), [NumLit(0.0)]), NumLit(1.0)), VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(lis), [Id(i)]), NumLit(1.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(j), BinaryOp(>=, Id(j), Id(i)), NumLit(1.0), If((BinaryOp(and, BinaryOp(>, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), BinaryOp(>, BinaryOp(+, ArrayCell(Id(lis), [Id(j)]), NumLit(1.0)), ArrayCell(Id(lis), [Id(i)]))), AssignStmt(ArrayCell(Id(lis), [Id(i)]), BinaryOp(+, ArrayCell(Id(lis), [Id(j)]), NumLit(1.0)))), [], None))])), Return(CallExpr(Id(max), [Id(lis), Id(n)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_399(self):
        # Longest Common Subsequence (LCS)
        # Print the length of the longest common subsequence of array (or strings)
        input = """func lcs(number arr1[100], number arr2[100], number m, number n) begin
    if ((m = 0) or (n = 0)) return 0
    if (arr1[m - 1] = arr2[n - 1]) return 1 + lcs(arr1, arr2, m - 1, n - 1)
    return max(lcs(arr1, arr2, m - 1, n), lcs(arr1, arr2, m, n - 1))
end
"""
        expect = "Program([FuncDecl(Id(lcs), [VarDecl(Id(arr1), ArrayType([100.0], NumberType), None, None), VarDecl(Id(arr2), ArrayType([100.0], NumberType), None, None), VarDecl(Id(m), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(=, Id(m), NumLit(0.0)), BinaryOp(=, Id(n), NumLit(0.0))), Return(NumLit(0.0))), [], None), If((BinaryOp(=, ArrayCell(Id(arr1), [BinaryOp(-, Id(m), NumLit(1.0))]), ArrayCell(Id(arr2), [BinaryOp(-, Id(n), NumLit(1.0))])), Return(BinaryOp(+, NumLit(1.0), CallExpr(Id(lcs), [Id(arr1), Id(arr2), BinaryOp(-, Id(m), NumLit(1.0)), BinaryOp(-, Id(n), NumLit(1.0))])))), [], None), Return(CallExpr(Id(max), [CallExpr(Id(lcs), [Id(arr1), Id(arr2), BinaryOp(-, Id(m), NumLit(1.0)), Id(n)]), CallExpr(Id(lcs), [Id(arr1), Id(arr2), Id(m), BinaryOp(-, Id(n), NumLit(1.0))])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 399))
