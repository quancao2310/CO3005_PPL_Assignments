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
        input = """number a <- 5
        string b <- "hello"
        bool c <- true
        dynamic d <- a
        dynamic e
        func main()
        begin
            e <- d
            writeNumber(e)
            return
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
