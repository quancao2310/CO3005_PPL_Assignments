import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 400-4xx: Redeclared Variable/Parameter/Function
    * 4xx-4xx: Undeclared Identifier/Function
    * 4xx-4xx: Type Mismatch In Expression
    * 4xx-4xx: Type Cannot Be Inferred
    * 4xx-4xx: Type Mismatch In Statement
    * 4xx-4xx: No Function Definition
    * 4xx-4xx: Must In Loop
    * 4xx-4xx: No Entry Point
    * 4xx-499: Mixed Cases
    """
    
    def test_400(self):
        input = """number a
"""
        expect = "No Entry Point"
        # self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_401(self):
        input = """func main()
"""
        expect = "No Function Definition: main"
        # self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_402(self):
        input = """func main() return 1
"""
        expect = "No Entry Point"
        # self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_403(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    var a <- [x,y]
end

func foo(number a, number b)
begin
	return 0
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x), Id(y)))"
        # self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_404(self):
        input = """func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    number x[3,3] <- [a,b,c]
    a <- [1,2,3]
    b <- [4,5,6]
    c <- [7,8,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_405(self):
        input = """func main()
begin 
    dynamic a
    number x[3,3] <- a[1]
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_406(self):
        input = """func main()
begin
    dynamic num
    bool arr <- num and (num > num)
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_407(self):
        input = """func main()
begin
    number arr[2,2] <- [[1,2],[1,2]]
    var x <- arr[0,3]
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_408(self):
        input = """dynamic b
var a <- b + 1
"""
        expect = "No Entry Point"
        # self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_409(self):
        input = """dynamic x
number a[2,2] <- [x,[x,x]]
func main() return
"""
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        # self.assertTrue(TestChecker.test(input, expect, 409)) # wrong
    
    def test_410(self):
        input = """dynamic a
string x <- [a]
func main() return
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_411(self):
        input = """func main() return
func foo() begin
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test_412(self):
        input = """func foo(number a)
func foo(number a)
func foo(number a)
func main() return
func foo(number a) return a
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test_413(self):
        input = """func main() return
func foo() begin
end
dynamic a
dynamic x <- a == (a+2)
func main() return
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_414(self):
        input = """func main() return
func foo()
func foo()
func foo() begin
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 414))
    
    def test_415(self):
        input = """func main() return
func foo() begin
end
func foo() begin
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 415))
    
    def test_416(self):
        input = """func foo(number a)
func foo(string a, bool b) return a

func main()

begin 

end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test_417(self):
        input = """func main() begin 
    var x <- (x + 1) = x
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(x), None, var, BinaryOp(=, BinaryOp(+, Id(x), NumLit(1.0)), Id(x)))"
        # self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_418(self):
        input = """dynamic x
dynamic y
dynamic a <- [[x, y], 2]
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(y)), NumLit(2.0))"
        # self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_419(self):
        input = """dynamic x
dynamic y
dynamic t <- [[x, y], [x, y, 2]]
func main() return
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(y)), ArrayLit(Id(x), Id(y), NumLit(2.0)))"
        # self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_420(self):
        input = """dynamic a
string x <- [a]
func main() return
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        # self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_421(self):
        input = """dynamic a
number b <- a[0]
func main() return
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_422(self):
        input = """func main()
begin
    dynamic a
    dynamic b
    number arr[2, 2] <- [[a, b]]
    number c[2, 2] <- arr
end
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_423(self):
        input = """dynamic y
number a[3]
dynamic b <- a[[y]]
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_424(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test_425(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_426(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 426))
    
    def test_427(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 427))
    
    def test_428(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_429(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 429))
    
    def test_430(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_431(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_432(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_433(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_434(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_435(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_436(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_437(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_438(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test_439(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_440(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test_441(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test_442(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_443(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test_444(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_445(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_446(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_447(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_448(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_449(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_450(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_451(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_452(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_453(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_454(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_455(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_456(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_457(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_458(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_459(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_460(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_461(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_462(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_463(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_464(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_465(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_466(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_467(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_468(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_469(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_470(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_471(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_472(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test_473(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test_474(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_475(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_476(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_477(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_478(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_479(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_480(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_481(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_482(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_483(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_484(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_485(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_486(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test_487(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_488(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test_489(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 489))
    
    def test_490(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test_491(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_492(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test_493(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 493))
    
    def test_494(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 494))
    
    def test_495(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 495))
    
    def test_496(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 496))
    
    def test_497(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 497))
    
    def test_498(self):
        input = """
"""
        expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 498))
    
    def test_499(self):
        input = """
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
