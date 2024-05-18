import unittest
import unittest.mock
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 500: Built-in function calls
    * 501-505: Variable Declarations + Assignment Statement
    * 506-519: Function Declarations + Function calls (Statement + Expression) + Return Statement + Block Statement
    * 520-529: Binary/Unary expressions
    * 530-549: Array expressions + Index operator
    * 550-574: Other Statements (If, For, Break, Continue)
    * 575-599: Solve algorithms/problems in ZCode (simplified due to lack of features)
    """
    
    # Built-in function calls
    def test_500(self):
        # Built-in function calls (Read is not tested due to no automation set up)
        input = """func main() begin
    writeNumber(10)
    writeString(" ")
    writeNumber(123.456)
    writeString(" ")
    writeBool(true)
    writeString(" ")
    writeBool(false)
    writeString(" ")
    writeString("Hello'"World")
end
"""
        expect = "10.0 123.456 true false Hello\"World"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    # Variable Declarations + Assignment Statement
    def test_501(self):
        # Variables: Global declarations
        input = """number a <- 1
bool b <- true
string c <- "ABC"
number d
string e
bool f

func main() begin
    writeNumber(a)
    writeBool(b)
    writeString(c)
end
"""
        expect = "1.0trueABC"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test_502(self):
        # Variables: Local declarations
        input = """number a
string b
bool c

func main() begin
    number a <- 2
    bool b <- true
    string c <- "ABC"
    
    writeNumber(a)
    writeBool(b)
    writeString(c)
end
"""
        expect = "2.0trueABC"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test_503(self):
        # Assignments
        input = """number a
string b
bool c

func main() begin
    a <- 20e4
    b <- " Hello "
    c <- false
    
    writeNumber(a)
    writeString(b)
    writeBool(c)
    writeString("\\n")
    
    a <- 2.5e-1
    b <- " ABC "
    c <- true
    
    writeNumber(a)
    writeString(b)
    writeBool(c)
end
"""
        expect = "200000.0 Hello false\n0.25 ABC true"
        self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    def test_504(self):
        # Local variables shadowing global variables
        input = """number a <- 100
func main() begin
    writeNumber(a)
    number a <- 200
    writeNumber(a)
end
"""
        expect = "100.0200.0"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    def test_505(self):
        # Variables: Type inference
        input = """var a <- 1
dynamic b <- "an inferred string "
dynamic c
dynamic d <- a

func main() begin
    c <- false
    writeNumber(a)
    writeString(b)
    writeBool(c)
    writeNumber(d)
end
"""
        expect = "1.0an inferred string false1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
    
    # Function Declarations + Function calls (Statement + Expression) + Return Statement + Block Statement
    def test_506(self):
        # Functions: Normal functions
        input = """func foo() return "Hello"
func bar() begin
    number a <- 1
    dynamic b
end

func main() begin
    bar()
    var x <- foo()
    writeString(x)
end
"""
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 506))
    
    def test_507(self):
        # Functions: Declaration-only first and Implementation later (Function call Type inference)
        input = """func foo()
func main() begin
    number a <- foo()
    writeNumber(a)
end

func foo() return 1.5
"""
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 507))
    
    def test_508(self):
        # Functions: Type inference
        input = """func init()
func foo() return false
dynamic a

func main() begin
    init()
    number b <- a ## Infer rhs
    dynamic c <- foo() ## Infer lhs
    writeNumber(b)
    writeBool(c)
end

func init() begin
    a <- 1.23
end
"""
        expect = "1.23false"
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test_509(self):
        # Functions: With parameters
        input = """func foo(number a, bool b, string c) begin
    writeNumber(a)
    writeBool(b)
    writeString(c ... "\\n")
end
func bar(number num) return num/2

func main() begin
    foo(1, true, "a random string")
    writeNumber(bar(10))
end
"""
        expect = "1.0truea random string\n5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))
    
    def test_510(self):
        # Functions: Redeclared Parameter in declaration-only part
        input = """func foo(number a, bool a, bool a)

func foo(number x, bool y, bool z) return
func main() begin
    foo(1, true, false)
end
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test_511(self):
        # Declare Variable with the same name as Parameter (No error - Due to function scope being different from block scope)
        input = """func foo(number x, bool y) begin
    string x <- "str "
    bool y <- true
    writeString(x)
    writeBool(y)
end
func main() begin
    foo(1, false)
end
"""
        expect = "str true"
        self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    def test_512(self):
        # Declare Parameter with the same name as Function (No error)
        input = """func foo() return 123

func bar(number foo, number bar, string main) begin
    number x <- bar + foo
    writeNumber(x)
    writeString(main)
    writeNumber(foo())
end

func main() begin
    bar(321, 123, "main")
end
"""
        expect = "444.0main123.0"
        self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    def test_513(self):
        # Declare Function with the same name as global Variable (No error)
        input = """number a <- 100.

func a() return "string"

func main() begin
    writeNumber(a)
    writeString(a())
end
"""
        expect = "100.0string"
        self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    def test_514(self):
        # Functions: Parameter shadowing global variable
        input = """number abc <- 12.3e3

func foo(string abc) return abc == "abc"

func main() begin
    writeBool(foo("abc"))
end
"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    def test_515(self):
        # Functions: Parameter Type inference
        input = """func init()
dynamic a
dynamic b
dynamic c
dynamic d

func foo(number a, bool b, string c, number d) begin
    writeNumber(a - d)
    writeBool(b and (c == "abc"))
end

func inc(number a) return a + 1

func main() begin
    init()
    foo(a, b, c, inc(d))
end

func init() begin
    a <- 1
    b <- true
    c <- "abc"
    d <- 10
end
"""
        expect = "-10.0true"
        self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    def test_516(self):
        # Functions: Return Statement Type inference
        input = """func init()
func bar()
dynamic d

func foo(number a, number b) begin
    if (a = b) return 123 ## Return value infers function type
    return bar() ## Function type infers another function
end

func bar() return d ## Function type infers the returned variable

func main() begin
    init()
    writeNumber(foo(120, 121))
    writeNumber(bar())
end

func init() begin
    d <- 12.34e5
end
"""
        expect = "1234000.01234000.0"
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_517(self):
        # Declarations in block scope 1
        input = """func main() begin
    number a <- 100
    begin
        number a <- 200
        writeNumber(a)
    end
    string b <- " false"
    writeNumber(a)
    writeString(b)
end
"""
        expect = "200.0100.0 false"
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_518(self):
        # Declarations in block scope 2
        input = """number a <- 6
func main() begin
    dynamic b <- 7
    begin
        dynamic a <- 8
        begin
            dynamic b <- 9
            writeNumber(a + b) ## 8 + 9 = 17
        end
        writeNumber(a + b) ## 8 + 7 = 15
    end
    writeNumber(a + b) ## 6 + 7 = 13
end
"""
        expect = "17.015.013.0"
        self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    def test_519(self):
        # Declarations in block scope 3
        input = """number a <- 6
func main() begin
    dynamic b <- 7
    begin
        a <- 8
        begin
            b <- 9
            writeNumber(a + b) ## 8 + 9 = 17
        end
        writeNumber(a + b) ## 8 + 9 = 17
    end
    writeNumber(a + b) ## 8 + 9 = 17
end
"""
        expect = "17.017.017.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    # Binary/Unary expressions
    def test_520(self):
        # Arithmetic operators
        input = """func main() begin
    number a <- 47.25
    number b <- 10.5
    var c <- a + b
    var d <- a - b
    var e <- -a + b
    var f <- -a * -b
    var g <- a / b
    var h <- a % b
    
    writeNumber(c)
    writeString(" ")
    writeNumber(d)
    writeString(" ")
    writeNumber(e)
    writeString(" ")
    writeNumber(f)
    writeString(" ")
    writeNumber(g)
    writeString(" ")
    writeNumber(h)
end
"""
        expect = "57.75 36.75 -36.75 496.125 4.5 5.25"
        self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    def test_521(self):
        # Logic operators
        input = """func main() begin
    writeBool(true and true)
    writeBool(true and false)
    writeBool(false and true)
    writeBool(false and false)
    
    writeBool(true or true)
    writeBool(true or false)
    writeBool(false or true)
    writeBool(false or false)
    
    writeBool(not true)
    writeBool(not false)
end
"""
        expect = "truefalsefalsefalsetruetruetruefalsefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    def test_522(self):
        # String operators
        input = """func main() begin
    string a <- "Hello"
    string b <- " World"
    dynamic c <- a ... b
    writeString(("\\t" ... c) ..."\\n")
end
"""
        expect = "\tHello World\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    def test_523(self):
        # Relational operators
        input = """func main() begin
    writeBool(10 = 20)
    writeBool(20 = 20)
    writeBool(10 != 20)
    writeBool(20 != 20)
    
    writeString(" ")
    
    writeBool(10 < 20)
    writeBool(10 > 20)
    writeBool(20 > 20)
    writeBool(10 <= 20)
    writeBool(20 <= 20)
    writeBool(10 >= 20)
    writeBool(20 >= 20)
    
    writeString(" ")
    
    writeBool("" == "")
    writeBool("abc" == "abc")
    writeBool("abc" == "abd")
    writeBool("123\\'456" == "123'456")
end
"""
        expect = "falsetruetruefalse truefalsefalsetruetruefalsetrue truetruefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    def test_524(self):
        # Mixed operators
        input = """func main() begin
    number a <- 1
    number b <- 2
    bool c <- a >= b
    number x <- ((a + a - b) * (a / b)) + ((a % b) - ((b % a) + (b / a) * (a + a) / (b - a))) + (a * a)
    bool y <- ((a + a * a) / (a - b) < a + a) and not c or (a + a >= a)
    y <- y and (not (a < a) or ((a <= a) and ((a >= a) or ((a = a) and (a != a)))))
    
    writeNumber(x)
    writeString("\\n")
    writeBool(y)
    writeString(" This " ... (("is " ... ("a " ... "string ")) ... ("concatenation" ... "!")))
end
"""
        expect = "-2.0\ntrue This is a string concatenation!"
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test_525(self):
        # Arithmetic binary operators: Type inference
        input = """func init()
dynamic a
dynamic b
dynamic c
dynamic d
dynamic e
dynamic f

func main() begin
    init()
    var x1 <- a + b - 1
    var x2 <- 3 * c - d
    var x3 <- e / 2
    var x4 <- f % 5
    
    writeNumber(x1)
    writeString(" ")
    writeNumber(x2)
    writeString(" ")
    writeNumber(x3)
    writeString(" ")
    writeNumber(x4)
end

func init() begin
    a <- 100
    b <- 10.18
    c <- a - 10
    d <- b + 0.82
    e <- a / 2
    f <- 57
end
"""
        expect = "109.18 259.0 25.0 2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    def test_526(self):
        # Arithmetic unary operators: Type inference
        input = """func init()
dynamic a
dynamic b
dynamic c
dynamic d
dynamic e
dynamic f

func main() begin
    init()
    dynamic x1 <- -a
    dynamic x2 <- --b
    dynamic x3 <- -c + d
    dynamic x4 <- -e * f
    
    writeNumber(x1)
    writeString(" ")
    writeNumber(x2)
    writeString(" ")
    writeNumber(x3)
    writeString(" ")
    writeNumber(x4)
end

func init() begin
    a <- 100
    b <- -----------1 ## -1
    c <- ----------a ## 100
    d <- 1
    e <- 2
    f <- 3
end
"""
        expect = "-100.0 -1.0 -99.0 -6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    def test_527(self):
        # Logic operators: Type inference
        input = """func init()
dynamic a
dynamic b
dynamic c
dynamic d
dynamic e

func main() begin
    init()
    dynamic x1 <- a and not b
    dynamic x2 <- not not c or d
    dynamic x3 <- a or not e and d
    
    writeBool(x1)
    writeString(" ")
    writeBool(x2)
    writeString(" ")
    writeBool(x3)
end

func init() begin
    a <- false
    b <- not not not not not not not false ## true
    c <- not not not not not not a ## false
    d <- true
    e <- false
end
"""
        expect = "false true true"
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    def test_528(self):
        # String operators: Type inference
        input = """func init()
dynamic a
dynamic b
dynamic c

func main() begin
    init()
    dynamic x1 <- a ... " str"
    dynamic x2 <- b ... c
    
    writeString(x1)
    writeString("\\n")
    writeString(x2)
end

func init() begin
    a <- "abc"
    b <- "fed"
    c <- "ghi"
end
"""
        expect = "abc str\nfedghi"
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test_529(self):
        # Relational operators: Type inference
        input = """func init()
dynamic a
dynamic b
dynamic c
dynamic d
dynamic e
dynamic f

func main() begin
    init()
    dynamic x1 <- a > b
    dynamic x2 <- c != d
    dynamic x3 <- e == f
    
    writeBool(x1)
    writeString(" ")
    writeBool(x2)
    writeString(" ")
    writeBool(x3)
end

func init() begin
    a <- 100
    b <- 200
    c <- 100.0
    d <- 100.00
    e <- "23"
    f <- "23"
end
"""
        expect = "false false true"
        self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    # Array expressions + Index operator
    def test_530(self):
        # Array Literal: 1-dimensional array
        input = """func main() begin
    number a[10] <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bool b[5] <- [true, false, true, false, true]
    string c[4] <- ["PPL", "is", "very", "hard"]
    
    writeNumber(a[5])
    writeBool(b[3])
    writeString(c[0])
end
"""
        expect = "6.0falsePPL"
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    def test_531(self):
        # Array Literal: Multi-dimensional array
        input = """func main() begin
    number a[1, 2, 3]
    number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    bool c[2, 2, 3] <- [[[true, true, false], [true, true, false]], [[true, true, false], [true, true, false]]]
    string d[2, 2] <- [["PPL", "is"], ["very", "hard"]]
    
    writeNumber(b[1, 0])
    writeBool(c[1, 1, 1])
    writeString(d[0, 0])
end
"""
        expect = "4.0truePPL"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test_532(self):
        # Array Literal: With other expressions
        input = """func main() begin
    number a[2, 3] <- [[1 + 2, 2 * 3, 3 / 4], [4 - 5, 5 % 2, 6 / 3]]
    bool b[3] <- [true or true, false and false, not true]
    string c[2] <- ["PPL " ... "is ", "very " ... "hard"]
    
    writeNumber(a[0, 2])
    writeBool(b[1])
    writeString(c[1])
end
"""
        expect = "0.75falsevery hard"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    def test_533(self):
        # Index operator: Array access from variable
        input = """func main() begin
    number a[2, 3] <- [[1 + 2, 2 * 3, 3 / 4], [4 - 5, 5 % 2, 6 / 3]]
    number b <- a[1, 2]
    number c <- 1 + a[1, 1]
    number d <- a[0, 2] * 2
    
    writeNumber(b)
    writeNumber(c)
    writeNumber(d)
end
"""
        expect = "2.02.01.5"
        self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    def test_534(self):
        # Index operator: Array write
        input = """func main() begin
    number a[2, 3]
    a[0, 0] <- 1
    a[0, 1] <- 2
    a[0, 2] <- 3 + 4
    a[1, 0] <- 5 * 6
    a[1, 1] <- 7 - 8
    a[1, 2] <- 9 / 10
    
    writeNumber(a[0, 0])
    writeNumber(a[0, 1])
    writeNumber(a[0, 2])
    writeNumber(a[1, 0] + a[1, 1] + a[1, 2])
end
"""
        expect = "1.02.07.029.9"
        self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    def test_535(self):
        # Index operator: Read-write array
        input = """func foo(number x) return x + 1

func main() begin
    number a[15] <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    number b[3, 4] <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    a[3 + foo(2)] <- a[b[2, 3]] + 4
    writeNumber(a[6])
end
"""
        expect = "17.0"
        self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    def test_536(self):
        # Array as function parameter
        input = """func foo(number a[4], bool b[3, 2], string c[2]) begin
    a[1] <- 5
    b[1, 0] <- true
end

func main() begin
    number x[4] <- [1, 2, 3, 4]
    bool y[3, 2] <- [[true, false], [false, true], [true, true]]
    
    writeNumber(x[1])
    writeBool(y[1, 0])
    
    foo(x, y, ["PPL", "hard"])
    
    writeNumber(x[1])
    writeBool(y[1, 0])
end
"""
        expect = "2.0false5.0true"
        self.assertTrue(TestCodeGen.test(input, expect, 536))
    
    def test_537(self):
        # Array as function return value
        input = """func createArray()
begin
    number x[10] <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return x
end

func main() begin
    dynamic arr <- createArray()
    number brr[10] <- createArray()
    writeNumber(arr[5] + brr[5])
end
"""
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    def test_538(self):
        # Array as reference
        input = """func main() begin
    number a[3] <- [1, 2, 3]
    number b[3] <- a
    b[1] <- 5
    writeNumber(a[1])
end
"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    def test_539(self):
        # Array in array
        input = """func main() begin
    number a[3] <- [1, 2, 3]
    number b[3] <- [4, 5, 6]
    number c[3] <- [7, 8, 9]
    number x[3, 3] <- [a, b, c]
    
    writeNumber(a[0] + b[1] + c[2] + x[2, 0])
end
"""
        expect = "22.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    def test_540(self):
        # Index operator: Array access from function call
        input = """func foo()
begin
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
end

func main() begin
    number a <- foo()[2]
    writeNumber(a)
end
"""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 540))
    
    def test_541(self):
        # Array Literal: Type inference of whole array
        input = """func main() begin
    dynamic a <- [1, 2, 3, 4, 5]
    dynamic b <- [[1, 2, 3], [4, 5, 6]]
    dynamic c <- [[[true, true, false], [true, true, false]], [[true, true, false], [true, true, false]]]
    dynamic d <- ["PPL", "is", "very", "hard"]
    
    writeNumber(a[2] * a[3] + b[1, 2] * b[0, 1])
    writeBool(c[1, 1, 1])
    writeString(d[0] ... (" " ... d[1]))
end
"""
        expect = "24.0truePPL is"
        self.assertTrue(TestCodeGen.test(input, expect, 541))
    
    def test_542(self):
        # Array Literal: Type inference of array elements 1
        input = """func init()
dynamic x
dynamic y
dynamic z
dynamic t
dynamic u

func main() begin
    init()
    number w[3, 2, 4, 2] <- [x, [y, z], [[t, t, t, t], [t, t, [100, 200], [u[0], u[1]]]]]
    
    writeNumber(w[0, 0, 0, 0]) ## 1.0
    writeNumber(w[1, 1, 2, 1]) ## 3.0
    writeNumber(w[2, 1, 3, 1]) ## u[1] = 400.0
end

func init() begin
    x <- [[[1, 2], [3, 4], [5, 6], [7, 8]], [[8, 7], [6, 5], [4, 3], [2, 1]]]
    y <- [[1, 2], [3, 4], [5, 6], [7, 8]]
    z <- [[8, 7], [6, 5], [4, 3], [2, 1]]
    t <- [100, 200]
    u <- [300, 400]
end
"""
        expect = "1.03.0400.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    def test_543(self):
        # Array Literal: Type inference of array elements 2
        input = """func init()
dynamic e
dynamic f

func main() begin
    init()
    number g[2, 2] <- [[e, e], f]
    writeNumber(g[0, 0] + g[1, 1])
end

func init() begin
    e <- 1
    f <- [2, 3]
end
"""
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test_544(self):
        # Array Literal: Type inference of array elements 3
        input = """func init()
dynamic a
dynamic b
dynamic c

func main() begin
    init()
    var d <- 4
    a <- [[[b]], [[[c, d]]]] ## a: ArrayType([2, 1, 1, 2]) = [[[[1, 2]]], [[[3, 4]]]]
    writeNumber(a[0, 0, 0, 0] + a[0, 0, 0, 1] + a[1, 0, 0, 0] + a[1, 0, 0, 1]) ## 10.0
end

func init() begin
    b <- [1, 2]
    c <- 3
end
"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    def test_545(self):
        # Index operator: Type inference for variable
        input = """func init()
dynamic a
dynamic b
dynamic c
dynamic i
dynamic j
dynamic k

func main() begin
    init()
    number x1 <- a[i]
    bool x2 <- b[i, j]
    string x3 <- c[j, i]
    
    writeNumber(x1)
    writeBool(x2)
    writeString(x3)
    writeNumber(a[k])
end

func init() begin
    a <- [5, 4, 3, 2, 1]
    c <- [["PPL", "is"], ["very", "hard"]]
    b <- [[a[0] > a[1], c[0, 0] == "PPL"], [false, true], [2 = 2, 1 != 3]]
    i <- 0
    j <- 1
    k <- 2
end
"""
        expect = "5.0truevery3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 545))
    
    def test_546(self):
        # Index operator: Type inference for function call
        input = """func init()
func a()
func b()
func c()
dynamic i
dynamic j
dynamic k

func main() begin
    init()
    number x1 <- a()[i]
    bool x2 <- b()[i, k]
    string x3 <- c()[j, i]
    
    writeNumber(x1)
    writeBool(x2)
    writeString(x3)
    writeNumber(a()[k])
end

func a() return [5, 4, 3, 2, 1]
func b()
    return [[a()[0] > a()[1], c()[0, 0] == "PPL"], [false, true], [2 = 2, 1 != 3]]
func c() return [["PPL", "is"], ["very", "hard"]]
func init() begin
    i <- 0
    j <- 1
    k <- 1
end
"""
        expect = "5.0truevery4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 546))
    
    def test_547(self):
        # Index operator: Type inference for array write
        input = """func init()
dynamic a

func main() begin
    init()
    a[0] <- 5
    a[1] <- 4
    
    writeNumber(a[0])
    writeNumber(a[1])
    writeNumber(a[2])
end

func init() begin
    a <- [1, 2, 3, 4, 5]
end
"""
        expect = "5.04.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 547))
    
    def test_548(self):
        # Index operator: Type inference for read-write array
        input = """func init()
func foo(number x) return x + 1
dynamic a
dynamic b

func main() begin
    init()
    a[3 + foo(2)] <- a[b[2, 3]] + 4
    writeNumber(a[6])
end

func init() begin
    a <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    b <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
end
"""
        expect = "17.0"
        self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    def test_549(self):
        # Index operator: Securing the max stack size with Type inference
        # This testcase is designed to ensure that the max stack size is calculated correctly
        # when inferring type and generating code for ArrayCell
        input = """func bar(number x1, number x2, number x3, number x4, number x5, number x6, number x7, number x8, number x9)
dynamic arr

func pushIndices() begin
    ## The max stack size of this function should be at least 10
    arr[bar(1, 2, 3, 4, 5, 6, 7, 8, 9)] <- 10 * 10
end

func pushRhs() begin
    ## The max stack size of this function should be at least 12
    arr[9] <- arr[bar(1, 2, 3, 4, 5, 6, 7, 8, 9)] - 10
end

func main() begin
    arr <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pushIndices()
    pushRhs()
    writeNumber(arr[1])
    writeNumber(arr[9])
end

func bar(number x1, number x2, number x3, number x4, number x5, number x6, number x7, number x8, number x9) return 1
"""
        expect = "100.090.0"
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    # Other Statements (If, For, Break, Continue)
    def test_550(self):
        # If statement: Single if without block
        input = """func main() begin
    number a <- 10
    if (a > 5) a <- a + 5
    writeNumber(a)
end
"""
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input, expect, 550))
    
    def test_551(self):
        # If statement: Single if with block
        input = """func main() begin
    number a <- 10
    if (a > 5) begin
        number a <- 0
        writeNumber(a)
        a <- a + 5
    end
    writeNumber(a)
end
"""
        expect = "0.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 551))
    
    def test_552(self):
        # If statement: If-else
        input = """func main() begin
    number a <- 0
    if (a > 5) a <- a + 5
    else a <- a - 5
    writeNumber(a)
end
"""
        expect = "-5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))
    
    def test_553(self):
        # If statement: If-elif (1 elif)
        input = """func main() begin
    number a <- 0
    if (a > 5) a <- a + 5
    elif (a = 0) a <- a - 5
    writeNumber(a)
end
"""
        expect = "-5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    def test_554(self):
        # If statement: If-elif (multi elif, branched at middle elif)
        input = """func main() begin
    number a <- 1
    if (a > 5) a <- a + 5
    elif (a < 0) a <- a - 5
    elif (a = 0) a <- a + 1
    elif (a = 1) a <- a + 2
    elif (a = 2) a <- a - 3
    writeNumber(a)
end
"""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    def test_555(self):
        # If statement: If-elif (multi elif, branched at last elif)
        input = """func main() begin
    number a <- 2
    if (a > 5) a <- a + 5
    elif (a < 0) a <- a - 5
    elif (a = 0) a <- a + 1
    elif (a = 1) a <- a + 2
    elif (a = 2) a <- a - 3
    writeNumber(a)
end
"""
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))
    
    def test_556(self):
        # If statement: If-elif-else (1 elif)
        input = """func main() begin
    number a <- 2
    if (a > 5) a <- a + 5
    elif (a < 0) a <- a - 5
    else a <- a * 5
    writeNumber(a)
end
"""
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    def test_557(self):
        # If statement: If-elif-else (multi elif, branched at if)
        input = """func main() begin
    number a <- 20
    if (a > 5) a <- a + 5
    elif (a < 0) a <- a - 5
    elif (a = 0) a <- a + 1
    elif (a = 1) a <- a + 2
    elif (a = 2) a <- a + 3
    else a <- a * 5
    writeNumber(a)
end
"""
        expect = "25.0"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test_558(self):
        # If statement: If-elif-else (multi elif, branched at elif)
        input = """func main() begin
    number a <- 0
    if (a > 5) a <- a + 5
    elif (a < 0) a <- a - 5
    elif (a = 0) a <- a + 1
    elif (a = 1) a <- a + 2
    elif (a = 2) a <- a + 3
    else a <- a * 5
    writeNumber(a)
end
"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test_559(self):
        # If statement: If-elif-else (multi elif, branched at else)
        input = """func main() begin
    number a <- 4
    if (a > 5) a <- a + 5
    elif (a < 0) a <- a - 5
    elif (a = 0) a <- a + 1
    elif (a = 1) a <- a + 2
    elif (a = 2) a <- a + 3
    else a <- a * 5
    writeNumber(a)
end
"""
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input, expect, 559))
    
    def test_560(self):
        # If statement: Nested if
        input = """func main() begin
    number a <- 4
    
    if (a > 0) begin
        if (a > 10) begin
            writeString("a > 10")
        end
        elif ((a > 5) and (a <= 10)) begin
            writeString("5 < a <= 10")
        end
        else begin
            writeString("0 < a <= 5")
        end
    end
    else begin
        if (a = 0) begin
            writeString("a = 0")
        end
        else writeString("a < 0")
    end
end
"""
        expect = "0 < a <= 5"
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test_561(self):
        # If statement: Nested block
        input = """func main() begin
    number a <- 7
    begin
        if (a > 10) begin
            writeString("a > 10;")
            begin
                a <- a * 2
            end
        end
        else if ((a <= 10) and (a >= 5)) begin
            begin
                a <- a + 1
                writeString("5 <= a <= 10;")
            end
            a <- a + 1
        end
        else begin
            begin
                a <- a - 6
            end
            writeString("a < 5;")
        end
        a <- a - 1
    end
    writeNumber(a)
end
"""
        expect = "5 <= a <= 10;8.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_562(self):
        # If statement: Check unexecuted branch
        input = """number a <- 10
func foo() begin
    a <- a - 1
    return a
end

func main() begin
    number b <- 0
    if (b > 0) b <- foo()
    elif (b = 0) b <- foo() + 1
    elif (foo() > 7) b <- b + 1
    else b <- b + 2
    writeNumber(a)
    writeNumber(b)
end
"""
        expect = "9.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 562))
    
    def test_563(self):
        # If statement: Type inference 1
        input = """func init()
dynamic a
func a()

func main() begin
    init()
    if (a)
    begin
        writeString("true")
    end
    else
    begin
        writeString("false")
    end
    if (a())
        writeString("true")
    else
        writeString("false")
end

func a() return false

func init() begin
    a <- true
end
"""
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    def test_564(self):
        # If statement: Type inference 2
        input = """func init()
dynamic a

func main() begin
    init()
    if (a[1, 2])
        writeString("true")
    else
        writeString("false")
end

func init() begin
    a <- [[true, false, false], [false, true, false], [false, false, true]]
end
"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    def test_565(self):
        # For statement: Without block
        input = """func main() begin
    var i <- 0
    for i until i >= 10 by 1
        writeNumber(i)
end
"""
        expect = "0.01.02.03.04.05.06.07.08.09.0"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_566(self):
        # For statement: Check reset of loop variable
        input = """func main() begin
    var i <- 0
    for i until i >= 10 by 1
        i <- i + 1
    writeNumber(i)
end
"""
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test_567(self):
        # For statement: With block
        input = """func main() begin
    var i <- 0
    for i until i >= 10 by 1 begin
        writeNumber(i)
        i <- i + 1
    end
    writeNumber(i)
end
"""
        expect = "0.02.04.06.08.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    def test_568(self):
        # For statement: Nested for
        input = """func main() begin
    number arr[3, 5]
    var i <- 0
    var j <- 0
    for i until i = 3 by 1
    begin
        var tmp_10i <- 10 * (i + 1)
        for j until j = 5 by 1 begin
            arr[i, j] <- tmp_10i + j
            writeNumber(arr[i, j])
        end
    end
end
"""
        expect = "10.011.012.013.014.020.021.022.023.024.030.031.032.033.034.0"
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    def test_569(self):
        # For statement: Break statement
        input = """func main() begin
    number i <- 1
    for i until i = 20 by 1
    begin
        writeNumber(i)
        if (i = 10) break
    end
end
"""
        expect = "1.02.03.04.05.06.07.08.09.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    def test_570(self):
        # For statement: Continue statement
        input = """func main() begin
    number i <- 20
    for i until i = 0 by -1
    begin
        if (i >= 10)
            continue
        writeNumber(i)
    end
end
"""
        expect = "9.08.07.06.05.04.03.02.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    def test_571(self):
        # For statement: Break/Continue in nested for
        input = """func main() begin
    number arr[3, 5] <- [[10, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 10]]
    var i <- 0
    var j <- 0
    var chk10 <- false
    
    for i until i = 3 by 1 begin
        for j until j = 5 by 1 begin
            if (j = 0) continue
            if (arr[i, j] = 10) begin
                chk10 <- true
                writeNumber(i)
                writeNumber(j)
                break
            end
        end
        writeString("End of inner loop ")
        if (chk10) break
    end
end
"""
        expect = "End of inner loop 1.04.0End of inner loop "
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    def test_572(self):
        # For statement: Type inference of loop variable
        input = """func init()
dynamic a

func main() begin
    init()
    for a until a >= 10 by 3
        writeNumber(a)
end

func init() begin
    a <- 1
end
"""
        expect = "1.04.07.0"
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test_573(self):
        # For statement: Type inference of condition expression
        input = """func init()
dynamic a

func main() begin
    init()
    var i <- 0
    for i until a by 2 begin
        writeNumber(i)
        a <- i > 10
    end
end

func init() begin
    a <- false
end
"""
        expect = "0.02.04.06.08.010.012.0"
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    def test_574(self):
        # For statement: Type inference of update expression
        input = """func init()
dynamic a

func main() begin
    init()
    var i <- 0
    for i until i > 10 by a begin
        writeNumber(i)
    end
end

func init() begin
    a <- 1.5
end
"""
        expect = "0.01.53.04.56.07.59.0"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    # Solve algorithms/problems in ZCode (simplified due to lack of features)
#     def test_575(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 575))
    
#     def test_576(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 576))
    
#     def test_577(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 577))
    
#     def test_578(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 578))
    
#     def test_579(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 579))
    
#     def test_580(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 580))
    
#     def test_581(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 581))
    
#     def test_582(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 582))
    
#     def test_583(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 583))
    
#     def test_584(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 584))
    
#     def test_585(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 585))
    
#     def test_586(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 586))
    
#     def test_587(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 587))
    
#     def test_588(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 588))
    
#     def test_589(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 589))
    
#     def test_590(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 590))
    
#     def test_591(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 591))
    
#     def test_592(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 592))
    
#     def test_593(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 593))
    
#     def test_594(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 594))
    
#     def test_595(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 595))
    
#     def test_596(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 596))
    
#     def test_597(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 597))
    
#     def test_598(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 598))
    
#     def test_599(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 599))
