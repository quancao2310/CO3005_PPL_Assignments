import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 300-399: 
    """
    
    def test_300(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_301(self):
        input = """func foo() begin
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 301))
