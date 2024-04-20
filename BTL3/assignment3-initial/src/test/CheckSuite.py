import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 400-424: Redeclared Variable/Parameter/Function
    * 425-432: Undeclared Identifier/Function
    * 433-453: Type Mismatch In Expression
    * 454-4xx: Type Cannot Be Inferred
    * 4xx-4xx: Type Mismatch In Statement
    * 4xx-4xx: No Function Definition
    * 4xx-4xx: Must In Loop
    * 4xx-4xx: No Entry Point
    * 4xx-499: Solve algorithms/problems in ZCode (simplified due to lack of features)
    """
    
    def test_400(self):
        # Declaring Variables: Normal case
        input = """number a <- 1
bool b <- true
string c <- "Hello"
number d

func main() begin
    number a <- 2
    bool b <- false
    begin
        string c <- "World"
        d <- 3
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_401(self):
        # Redeclared Variable in global scope
        input = """number a <- 1
func main() return
bool a
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_402(self):
        # Redeclared Variable in block scope 1
        input = """func main() begin
    number a
    string b
    number c
    dynamic c
end
"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_403(self):
        # Redeclared Variable in block scope 2
        input = """func main() begin
    number a
    string b
    begin
        number c
        string c <- "Redeclared"
    end
end
"""
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_404(self):
        # Redeclared Variable in block scope 3
        input = """func main() begin
    number a
    if (a > 0) begin
        number a
        number b
        string b
    end
end
"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_405(self):
        # Redeclared Variable when using if-statement without block
        input = """func main() begin
    number a
    if (false) number a
end
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_406(self):
        # Redeclared Variable when using for-statement without block
        input = """func main() begin
    number i
    for i until true by 1
        number x
    number x
end
"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_407(self):
        # Declare Variable with the same name as Function (No error)
        input = """func foo() return 1
func main() begin
    number foo <- foo()
    number bar <- foo + 1 + foo()
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_408(self):
        # Declaring Functions: Normal case
        input = """func foo() return
func bar() begin
end

func main() begin
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_409(self):
        # Declaring Functions with a later-declared implementation
        input = """func foo()
func main() begin
    number a
    bool b <- foo() = 2.5
end

func foo() return 1.5
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_410(self):
        # Redeclared Function: Full implementation
        input = """func foo() begin
    number a
end

func main() begin
    foo()
end

func foo() return
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_411(self):
        # Redeclared Function: With declaration-only part 1
        input = """func foo()
func foo()

func main() return
func foo() begin
end
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_412(self):
        # Redeclared Function: With declaration-only part 2
        input = """func foo() begin
    number a <- 3
end

func main() return
func foo()
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test_413(self):
        # Redeclared Function: With declaration-only part 3
        input = """func foo()
func main() return

func foo() return
func foo() return
"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_414(self):
        # Redeclared Function: With parameters (No overloading supported)
        input = """func bar(number a, bool b) return
func bar(number a) return

func main() return
"""
        expect = "Redeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_415(self):
        # Redeclared Function: Different signature when implementing 1
        input = """func bar(number a, bool b)
func main() return

func bar(number a) begin
end
"""
        expect = "Redeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_416(self):
        # Redeclared Function: Different signature when implementing 2
        input = """func a(number x)
func a(string x) return

func main() begin
end
"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_417(self):
        # Redeclared Function: Built-in functions
        input = """func main() return

func writeNumber(number a) begin
    number x <- readNumber()
end
"""
        expect = "Redeclared Function: writeNumber"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_418(self):
        # Declare Function with the same name as global Variable (No error)
        input = """number a
func a() return

func main() begin
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_419(self):
        # Declare Function but rename the parameters when implementing (No error)
        input = """func foo(number a)

func main() begin
    number b <- foo(4)
end

func foo(number num) return num/2
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_420(self):
        # Declaring Parameters: Normal case
        input = """func foo(number a, bool b, string c) return
func bar(number num) return num/2

func main() begin
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_421(self):
        # Redeclared Parameters (function scope)
        input = """func foo(number a, bool b, string b) return

func main() begin
end
"""
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_422(self):
        # Redeclared Parameter in declaration-only part (No error - Forum said so...)
        input = """func foo(number a, bool a, bool a)
func main() return

func foo(number x, bool y, bool z) return
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_423(self):
        # Declare Variable with the same name as Parameter (No error - Due to function scope being different from block scope)
        input = """func foo(number x, bool y) begin
    string x <- "str"
    bool y <- true
end

func main() begin
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_424(self):
        # Declare Parameter with the same name as Function (No error)
        input = """func foo() return
func bar(number foo, number bar, string main) begin
    foo()
    number x <- bar
end

func main() return
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_425(self):
        # Undeclared Identifier: Use a variable that is not declared
        input = """func main() begin
    a <- 123
end
"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_426(self):
        # Undeclared Identifier: Use a variable declared in block scope
        input = """func main() begin
    begin
        number a <- 123
    end
    a <- 456
end
"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_427(self):
        # Undeclared Identifier: Use an undeclared variable but have the same name as a function
        input = """func foo() return

func main() begin
    foo <- "Undeclared"
end
"""
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test_428(self):
        # Declared Identifier: Declared variables with non-block if/for and use them outside (No error)
        input = """func main() begin
    if (true) number a <- 1
    a <- 2
    for a until (true) by -1 string s <- "abc"
    s <- "def"
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_429(self):
        # Undeclared Function: Call an undeclared function with CallStmt
        input = """func main() begin
    foo()
end
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test_430(self):
        # Undeclared Function: Call an undeclared function with CallExpr
        input = """func main() begin
    number x <- foo()
end
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_431(self):
        # Undeclared Function: Call a function before its declaration
        input = """func main() begin
    foo()
end

func foo() return
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_432(self):
        # Undeclared Function: Call a function by using a variable with the same name
        input = """number foo <- 1
func main() begin
    number x <- foo()
end
"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_433(self):
        # Expressions: Normal case
        input = """func foo() return 1

func main() begin
    number a <- -1 + 2 * 3 / 4 % 5 - 6
    bool b <- true and false or not true
    string c <- "Hello"..."World"
    bool d <- (1 < 2) and (3 <= 4) and (5 > 6) and (7 >= 8) and (9 = 10) and (11 != 12) and ("ZCode" == "ZCode")
    
    number x[10] <- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number y <- x[0] + foo()
    
    string s[2, 3] <- [["1", "2", "3"], ["4", "5", "6"]]
    var ss <- s[0, 0]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_434(self):
        # Type Mismatch In Expression: Array Literal: Different types
        input = """func main() begin
    number x[5] <- [1, 2, 3, "4", true]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(4), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_435(self):
        # Type Mismatch In Expression: Array Literal: Nested arrays
        input = """func main() begin
    number x[2, 2] <- [[1, 2], ["3", "4"]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(StringLit(3), StringLit(4)))"
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_436(self):
        # Type Mismatch In Expression: Array Literal: Mismatched dimensions
        input = """func main() begin
    number x[2, 2] <- [[1.0, 2.0], [3.0, 4e0, 5.0]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_437(self):
        # Type Mismatch In Expression: Array Literal: Type inference 1
        # https://lms.hcmut.edu.vn/mod/forum/discuss.php?d=11332
        input = """dynamic x
func main() begin
    number a[2, 2] <- [x, [x, x]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_438(self):
        # Type Mismatch In Expression: Array Literal: Type inference 2
        input = """func main() begin
    dynamic x
    dynamic y
    dynamic t <- [[x, y], [x, y, 2]]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(y)), ArrayLit(Id(x), Id(y), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test_439(self):
        # Type Mismatch In Expression: Array Literal: Type inference 3
        input = """func main() begin
    dynamic x
    dynamic y
    dynamic a <- [[x, y], 2]
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(y)), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_440(self):
        # Type Mismatch In Expression: Index Operator: Using on non-array type
        input = """func main() begin
    string x
    number y <- x[1, 2]
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test_441(self):
        # Type Mismatch In Expression: Index Operator: Index is not a number
        input = """func main() begin
    string x[2, 3, 5]
    var y <- x[1, 2, "3"]
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0), NumLit(2.0), StringLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_442(self):
        # Array Literal and Index Operator: Type inference 1
        input = """func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic e
    dynamic f
    
    number x[3, 3] <- [a, b, c]
    a <- [1, 2, 3]
    b <- [4, 5, 6]
    c <- [7, 8, 9]
    
    writeNumber(a[d] + b[e] + c[f] + x[d, e])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_443(self):
        # Array Literal and Index Operator: Type inference 2
        input = """func main() begin
    dynamic x
    dynamic y
    dynamic z
    dynamic t
    dynamic u
    dynamic v
    number w[3, 2, 4, 2] <- [x, [y, z], [[t, t, t, t], [t, t, [100, 200], [u[0, 1], u[1, 2]]]]]
    
    dynamic a
    dynamic b
    dynamic c
    var d <- 1
    a <- [[[b]], [[[c, d]]]] ## a: ArrayType([2, 1, 1, 2])
    b <- [2024, 10 / 10]
    a <- [[[[1, 2]]], [[[3, 4]]]]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_444(self):
        # Type Mismatch In Expression: Unary Operator: Prefix-minus on non-number type
        input = """func main() begin
    string a
    bool b <- -a
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_445(self):
        # Type Mismatch In Expression: Unary Operator: Logical NOT on non-boolean type
        input = """func main() begin
    number a
    bool b <- not a
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_446(self):
        # Type Mismatch In Expression: Binary Operator: Arithmetic operator
        input = """func main() begin
    dynamic x
    dynamic t
    x <- 3.456
    begin
        begin
            dynamic z
            t <- true
            z <- t - x
        end
    end
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(-, Id(t), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_447(self):
        # Type Mismatch In Expression: Binary Operator: Logic operator
        input = """func main() begin
    dynamic x
    dynamic t
    x <- 3.456
    begin
        t <- true
        begin
            dynamic z <- t and x
        end
    end
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(t), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_448(self):
        # Type Mismatch In Expression: Binary Operator: String operator
        input = """func main() begin
    dynamic x
    var t <- true
    x <- "3.456"
    begin
        string z
        z <- t ... x
    end
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(t), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_449(self):
        # Type Mismatch In Expression: Binary Operator: Relational operator
        input = """func main() begin
    dynamic x <- 3.456
    begin
        dynamic t <- t == (t < x)
    end
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(<, Id(t), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_450(self):
        # Type Mismatch In Expression: Function Call: Return type mismatch
        input = """func foo(number a[1, 1, 2]) return 1
func main() begin
    dynamic z
    number x <- foo([[z]])[2]
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(z)))]), [NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_451(self):
        # Type Mismatch In Expression: Function Call: Void-type function in expression
        input = """func foo(number a[1, 1, 2]) begin
    var z <- a[0, 0, 0]
end
func main() begin
    dynamic z
    number x <- foo([[z]])
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(z)))])"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_452(self):
        # Type Mismatch In Expression: Function Call: Wrong parameter type
        input = """func foo(number a, bool b) begin
    return (a > 0) and b
end
func main() begin
    dynamic z
    bool x <- foo(z, "false")
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(z), StringLit(false)])"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_453(self):
        # Type Mismatch In Expression: Function Call: Different number of parameters
        input = """func foo(number a, bool b, string z) begin
    return (a > 0) and b
end
func main() begin
    dynamic z
    bool x <- foo(z, false)
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(z), BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_454(self):
        # Type Cannot Be Inferred: 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_455(self):
        # Type Cannot Be Inferred: 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_456(self):
        # Type Cannot Be Inferred: 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_457(self):
        # Type Cannot Be Inferred: 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_458(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_459(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_460(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_461(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_462(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_463(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_464(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_465(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_466(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_467(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_468(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_469(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_470(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_471(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_472(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_473(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test_474(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_475(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_476(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_477(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_478(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_479(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_480(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_481(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_482(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_483(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_484(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_485(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_486(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test_487(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_488(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test_489(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_490(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_491(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_492(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test_493(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_494(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test_495(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_496(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test_497(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test_498(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test_499(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
# Temporary

# class CheckSuite(unittest.TestCase):