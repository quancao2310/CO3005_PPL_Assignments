import unittest
import unittest.mock
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 500: Built-in function calls
    * 5-5: Variable Declarations + Assignment Statement
    * 5-5: Function Declarations + Function calls (Statement + Expression)
    * 5-5: Expressions
    * 5-5: Statements
    * 5-5: Mixed statements
    * 5-599: Solve algorithms/problems in ZCode (simplified due to lack of features)
    """
    
    # Declarations + Built-in function calls
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
        # Variables: Type Inference
        input = """var a <- 1
dynamic b <- "an inferred string "
dynamic c <- false
dynamic d <- a

func main() begin
    writeNumber(a)
    writeString(b)
    writeBool(c)
    writeNumber(d)
end
"""
        expect = "1.0an inferred string false1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    def test_505(self):
        # Functions: Normal functions
        input = """func foo() return
func bar() begin
end

func main() begin
end
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 505))
    
    def test_506(self):
        # Functions: Declaration-only first and Implementation later
        input = """func foo()
func main() begin
    number a <- foo()
    writeNumber(a)
end

func foo() return 1.5
"""
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 506))
    
    def test_507(self):
        # 
        input = """dynamic a
func init()
func main() begin
    init()
    ## dynamic b <- a + 1
    number b <- a
    writeNumber(b)
end
func init() begin
    a <- 1.23
end
"""
        expect = "1.23"
        self.assertTrue(TestCodeGen.test(input, expect, 507))
    
    def test_508(self):
        # 
        input = """number a <- 100
func main() begin
    writeNumber(a)
    number a <- 200
    writeNumber(a)
end
"""
        expect = "100.0200.0"
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test_509(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 509))
    
    def test_510(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test_511(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    def test_512(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    def test_513(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    def test_514(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    def test_515(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    def test_516(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_517(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test_518(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    def test_519(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    def test_520(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    def test_521(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    def test_522(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    def test_523(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    def test_524(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test_525(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    def test_526(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    def test_527(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    def test_528(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test_529(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    def test_530(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    def test_531(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test_532(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    def test_533(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    def test_534(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    def test_535(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    def test_536(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 536))
    
    def test_537(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    def test_538(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    def test_539(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    def test_540(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 540))
    
    def test_541(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 541))
    
    def test_542(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    def test_543(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test_544(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    def test_545(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 545))
    
    def test_546(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))
    
    def test_547(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 547))
    
    def test_548(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    def test_549(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    def test_550(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 550))
    
    def test_551(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 551))
    
    def test_552(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 552))
    
    def test_553(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    def test_554(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    def test_555(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 555))
    
    def test_556(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    def test_557(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test_558(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test_559(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 559))
    
    def test_560(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test_561(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_562(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 562))
    
    def test_563(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    def test_564(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    def test_565(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_566(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test_567(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    def test_568(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    def test_569(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    def test_570(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    def test_571(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    def test_572(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test_573(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    def test_574(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    def test_575(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 575))
    
    def test_576(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 576))
    
    def test_577(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 577))
    
    def test_578(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    def test_579(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 579))
    
    def test_580(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 580))
    
    def test_581(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    def test_582(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    def test_583(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test_584(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    
    def test_585(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    def test_586(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test_587(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 587))
    
    def test_588(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 588))
    
    def test_589(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 589))
    
    def test_590(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    def test_591(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 591))
    
    def test_592(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    def test_593(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    def test_594(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    def test_595(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 595))
    
    def test_596(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 596))
    
    def test_597(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    def test_598(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 598))
    
    def test_599(self):
        # 
        input = """
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
