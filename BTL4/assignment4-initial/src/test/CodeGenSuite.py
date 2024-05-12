import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 500-5xx: 
    * 5xx-5xx: 
    * 5xx-599:
    """
    def test_500(self):
        input = """number a <- 16
string b <- "hello"
bool c <- true
dynamic d <- a
dynamic e

func foo(bool g, string a, number b) begin
    bool f
    dynamic e
    return d
end

func main()
begin
    begin
        number b
        number c
    end
    e <- d
    number g <- e
    writeNumber(g)
end
        """
        expect = "16.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    def test_501(self):
        input = """number a[5] <- [1, 2, 3, 4, 5]
number b[5] <- a
dynamic c

func main()
begin
    c <- readNumber()
    if (c = 0) writeNumber(a[0])
    elif (c = 1) writeNumber(a[1])
    elif (c = 2) writeNumber(a[2])
    else writeNumber(a[3])
end
        """
        expect = "4.0"
        # print("Please enter number 0 to check if-statement: ")
        self.assertTrue(TestCodeGen.test(input, expect, 501))
