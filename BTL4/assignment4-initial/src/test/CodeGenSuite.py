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
    def test_number(self):
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
    return
end
        """
        expect = "16.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
