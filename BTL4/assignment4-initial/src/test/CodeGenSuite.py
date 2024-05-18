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
    * 530-5: Array expressions + Index operator
    * 5-5: Statements
    * 5-5: Mixed statements
    * 5-599: Solve algorithms/problems in ZCode (simplified due to lack of features)
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
        # 
        input = """func main() begin

end
"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    
#     def test_531(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 531))
    
#     def test_532(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 532))
    
#     def test_533(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 533))
    
#     def test_534(self):
#         # 
#         input = """func main() begin
# string __s[9312e1202]
# number a[5] <- [2, 3, 5, 7, 11]
# string sss[4] <- ["PPL", "is", "very", "hard"]
# bool abc[4] <- [true, true, false, false]

# number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
# bool c[2, 2, 3] <- [[[true, true, false], [true, true, false]], [[true, true, false], [true, true, false]]]

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 534))
    
#     def test_535(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 535))
    
#     def test_536(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 536))
    
#     def test_537(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 537))
    
#     def test_538(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 538))
    
#     def test_539(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 539))
    
#     def test_540(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 540))
    
#     def test_541(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 541))
    
#     def test_542(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 542))
    
#     def test_543(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 543))
    
#     def test_544(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 544))
    
#     def test_545(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 545))
    
#     def test_546(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 546))
    
#     def test_547(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 547))
    
#     def test_548(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 548))
    
#     def test_549(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 549))
    
#     def test_550(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 550))
    
#     def test_551(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 551))
    
#     def test_552(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 552))
    
#     def test_553(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 553))
    
#     def test_554(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 554))
    
#     def test_555(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 555))
    
#     def test_556(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 556))
    
#     def test_557(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 557))
    
#     def test_558(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 558))
    
#     def test_559(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 559))
    
#     def test_560(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 560))
    
#     def test_561(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 561))
    
#     def test_562(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 562))
    
#     def test_563(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 563))
    
#     def test_564(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 564))
    
#     def test_565(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 565))
    
#     def test_566(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 566))
    
#     def test_567(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 567))
    
#     def test_568(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 568))
    
#     def test_569(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 569))
    
#     def test_570(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 570))
    
#     def test_571(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 571))
    
#     def test_572(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 572))
    
#     def test_573(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 573))
    
#     def test_574(self):
#         # 
#         input = """func main() begin

# end
# """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 574))
    
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
