import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 400-424: Redeclared Variable/Parameter/Function
    * 425-432: Undeclared Identifier/Function
    * 433-453: Type Mismatch In Expression
    * 454-459: Type Cannot Be Inferred
    * 460-474: Type Mismatch In Statement
    * 475-479: No Function Definition
    * 480-484: Must In Loop
    * 485-489: No Entry Point
    * 490-499: Solve algorithms/problems in ZCode (simplified due to lack of features)
    """
    
    # Redeclared Variable/Parameter/Function
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
    
    # Undeclared Identifier/Function
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
        # Declared Identifier: Declare variables with non-block if/for and use them outside (No error)
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
    
    # Type Mismatch In Expression
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
    
    dynamic e
    dynamic f
    number g[2, 2] <- [[e, e], f]
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
    
    # Type Cannot Be Inferred
    def test_454(self):
        # Type Cannot Be Inferred: Assign an unknown-type variable with another unknown-type variable
        input = """dynamic x <- 3
func main() begin
    dynamic y
    begin
        dynamic x
        x <- y
    end
end
"""
        expect = "Type Cannot Be Inferred: AssignStmt(Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_455(self):
        # Type Cannot Be Inferred: Assign an unknown-type variable with an unknown-return-type function call
        input = """func foo()
func main() begin
    var y <- foo()
end

func foo() return 123
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_456(self):
        # Type Cannot Be Inferred: Return an unknown-type variable in an unknown-return-type function
        input = """dynamic x

func foo(number n) begin
    for n until true by 1 begin
        dynamic x <- n / 2
        if (x % 2 = 0) break
    end
    return x
end

func main() begin
    number x <- foo(10)
end
"""
        expect = "Type Cannot Be Inferred: Return(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_457(self):
        # Type Cannot Be Inferred: Array Literal 1
        input = """dynamic a
dynamic b
dynamic c

func main() begin
    var x <- [a, b, c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayLit(Id(a), Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_458(self):
        # Type Cannot Be Inferred: Array Literal 2 (Forum said so...)
        input = """dynamic a
dynamic b
dynamic c

func main() begin
    bool x <- [a, b, c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), BoolType, None, ArrayLit(Id(a), Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_459(self):
        # Type Cannot Be Inferred: Index Operator
        input = """func main() begin
    dynamic a
    begin
        number c
    end
    var c <- a[100]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(a), [NumLit(100.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    # Type Mismatch In Statement
    def test_460(self):
        # Type Mismatch In Statement: Variable declaration/Assignment statment with different types 1
        input = """func main() begin
    string x <- 1
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(x), StringType, None, NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_461(self):
        # Type Mismatch In Statement: Variable declaration/Assignment statment with different types 2
        input = """func main() begin
    dynamic x
    dynamic y
    dynamic z
    string a[3] <- [x, y, z]
    number b
    b <- x
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_462(self):
        # Type Mismatch In Statement: Variable declaration/Assignment statment with different types 3
        input = """func main() begin
    var x <- (x >= readNumber()) or ("a" == "b")
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(x), None, var, BinaryOp(or, BinaryOp(>=, Id(x), CallExpr(Id(readNumber), [])), BinaryOp(==, StringLit(a), StringLit(b))))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_463(self):
        # Type Mismatch In Statement: Variable declaration/Assignment statment with different types 4
        input = """func main() begin
    number arr[2]
    arr <- [1, 2, 3, 4]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_464(self):
        # Type Mismatch In Statement: Variable declaration/Assignment statment with different types 5
        input = """func main() begin
    dynamic x
    dynamic y
    if (x) y <- x
    else y <- 1.25
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), NumLit(1.25))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_465(self):
        # Type Mismatch In Statement: If statement with non-boolean condition
        input = """func main() begin
    number x
    bool y
    begin
        dynamic x
        if (x) number y <- 1
        elif (y) return
    end
end
"""
        expect = "Type Mismatch In Statement: If((Id(x), VarDecl(Id(y), NumberType, None, NumLit(1.0))), [(Id(y), Return())], None)"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_466(self):
        # Type Mismatch In Statement: For statement with non-boolean condition
        input = """func main() begin
    dynamic i
    for i until 10 by 1 begin
    end
end
"""
        expect = "Type Mismatch In Statement: For(Id(i), NumLit(10.0), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_467(self):
        # Type Mismatch In Statement: For statement with non-number loop variable
        input = """func main() begin
    string i
    for i until "a" == "a" by 1 begin
    end
end
"""
        expect = "Type Mismatch In Statement: For(Id(i), BinaryOp(==, StringLit(a), StringLit(a)), NumLit(1.0), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_468(self):
        # Type Mismatch In Statement: For statement with non-number step
        input = """func main() begin
    number j <- 0
    number i
    for j until j > 10 by i = 1 begin
    end
end
"""
        expect = "Type Mismatch In Statement: For(Id(j), BinaryOp(>, Id(j), NumLit(10.0)), BinaryOp(=, Id(i), NumLit(1.0)), Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_469(self):
        # Type Mismatch In Statement: Return an expression in a void function
        input = """func bar()
func main() begin
    bar()
end

func bar() begin
    return readBool()
end
"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(readBool), []))"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_470(self):
        # Type Mismatch In Statement: Return none in a known-return-type function
        input = """func foo() begin
    number x <- 1
    if (x > 0) return 2
    else
        return
end

func main() return
"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_471(self):
        # Type Mismatch In Statement: Return statement with different types
        input = """dynamic res
func foo(string s)
func main() begin
    var x <- foo("ABC") * 20
end

func foo(string s) begin
    if (res) return 100
    return res
end
"""
        expect = "Type Mismatch In Statement: Return(Id(res))"
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_472(self):
        # Type Mismatch In Statement: Function Call statement return a non-void value
        input = """func foo(number a[1, 1, 2]) return 1
func main() begin
    dynamic z
    foo(z)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(z)])"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_473(self):
        # Type Mismatch In Statement: Function Call statement with wrong parameter type
        input = """func foo(number a, bool b) begin
    writeBool((a > 0) and b)
end
func main() begin
    dynamic z
    foo(z, "false")
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(z), StringLit(false)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test_474(self):
        # Type Mismatch In Statement: Function Call statement with different number of parameters
        input = """func foo(number a, bool b, string z) begin
    writeBool((a > 0) and b and (z == "true"))
end
func main() begin
    foo(98765, true)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(98765.0), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    # No Function Definition
    def test_475(self):
        # No Function Definition with non-parameter function
        input = """func bar()
func main() begin
    bar()
end
"""
        expect = "No Function Definition: bar"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_476(self):
        # No Function Definition with main function
        input = """func main()
"""
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_477(self):
        # No Function Definition with parameter function
        input = """func bar(string s)
func main() begin
    number z <- bar("Hola'"")
end
"""
        expect = "No Function Definition: bar"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_478(self):
        # No Function Definition with many same-name parameters function
        input = """func foo(number a, bool a, string a)
func main() return
"""
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_479(self):
        # No Function Definition with a variable having the same name as the function
        input = """func foo()
func main() begin
    var foo <- foo() + 123
end
"""
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    # Must In Loop
    def test_480(self):
        # Must In Loop: Break
        input = """func main() begin
    break
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_481(self):
        # Must In Loop: Continue
        input = """func main() begin
    continue
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_482(self):
        # Must In Loop: Break/Continue before the loop
        input = """func main() begin
    number i
    
    break
    for i until i > 10 by 1
    begin
    end
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_483(self):
        # Must In Loop: Break/Continue after the loop
        input = """func main() begin
    number i
    
    for i until i > 10 by 1
    begin
    end
    continue
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_484(self):
        # Break/Continue in a nested loop (No error)
        input = """func main() begin
    number i
    number j
    
    for i until i > 10 by 1 begin
        if (i = 5) continue
        for j until j > 10 by 1 begin
            if (i + j = 10) break
        end
        if (i = 9) break
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    # No Entry Point
    def test_485(self):
        # No Entry Point: Program with variables only
        input = """number a
bool b
string c
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_486(self):
        # No Entry Point: Program with functions only but no main
        input = """func a() return
func b() begin
end
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test_487(self):
        # No Entry Point: Program with a variable named "main"
        input = """number main
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_488(self):
        # No Entry Point: Function main with parameters
        input = """func main(number a, number b) return
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test_489(self):
        # No Entry Point: Function main with non-void return type
        input = """func main() return 1
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    # Solve algorithms/problems in ZCode (simplified due to lack of features)
    def test_490(self):
        # Factorial
        input = """func fact(number n) begin
    if (n = 1) return 1
    return n * fact(n - 1)
end

func main() begin
    number n <- readNumber()
    writeNumber(fact(n))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_491(self):
        # Find sum of array
        input = """func sum(number a[10], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum
end

func main() begin
    writeNumber(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(sum([2, 0, 2, 4, 0, 0, 0, 0, 0, 0], 10))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_492(self):
        # Find maximum in array
        input = """func max(number a[10], number length)
begin
    if (length <= 0)
        return -1e9 ## Represent negative infinity
    var max <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] > max) max <- a[i]
    return max
end

func main() begin
    writeNumber(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(max([2, 0, 2, 4, 0, 0, 0, 0, 0, 0], 10))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test_493(self):
        # XOR function
        input = """func xor(bool a, bool b) return (a and not b) or (not a and b)
func main() begin
    writeBool(xor(true, true))
    writeBool(xor(true, false))
    writeBool(xor(false, true))
    writeBool(xor(false, false))
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_494(self):
        # Check leap year
        input = """func is_leap(number year) return (year % 400 = 0) or ((year % 4 = 0) and (year % 100 != 0))

func main() begin
    number year <- readNumber()
    
    writeNumber(year)
    if (is_leap(year))
        writeString(" is a leap year\\n")
    else
        writeString(" is not a leap year\\n")
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test_495(self):
        # Fibonacci sequence
        input = """number fib[100]

func main() begin
    fib[0] <- 0
    fib[1] <- 1
    
    var i <- 2
    for i until i = 100 by 1
        fib[i] <- fib[i - 1] + fib[i - 2]
    
    writeNumber(fib[99])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_496(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test_497(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test_498(self):
        # Binary search
        input = """func binary_search(number arr[20], number length, number element)
begin
    var left <- 0
    var right <- length - 1
    number mid
    var _ <- 0
    for _ until left > right by 0 begin
        mid <- (left + right) / 2
        if (element = arr[mid]) return mid
        elif (element > arr[mid]) left <- mid + 1
        else right <- mid - 1
    end
    return -1
end

func main() begin
    dynamic arr <- [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    number x <- readNumber()
    var pos <- binary_search(arr, 20, x)
    
    if (pos = -1) writeString("Not found")
    else begin
        writeString("Found at position ")
        writeNumber(pos)
        writeString("\\n")
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test_499(self):
        # Bubble sort
        input = """func swap(number arr[10], number i, number j)

func bubble_sort(number arr[10]) begin
    var i <- 1
    bool changed
    for i until i = 10 by 1 begin
        var j <- 9
        changed <- false
        for j until j < i by -1
            if (arr[j] < arr[j - 1]) begin
                swap(arr, j, j - 1)
                changed <- true
            end
        if (not changed) break
    end
end

func swap(number arr[10], number i, number j) begin
    var tmp <- arr[i]
    arr[i] <- arr[j]
    arr[j] <- tmp
end

func main() begin
    var arr <- [10.64, 11.26, 19.81, 30.66, 25.18, 54.68, 49.18, 54.36, 99.75, 12.82]
    bubble_sort(arr)
    
    var i <- 0
    for i until i = 10 by 1
        writeNumber(arr[i])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
