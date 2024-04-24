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
        input = """func main()
        begin
            writeNumber(1)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
