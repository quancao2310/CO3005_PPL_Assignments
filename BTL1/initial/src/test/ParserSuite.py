import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        # Simple program
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_201(self):
        # 
        input = """func main()
begin
if (a = 1)
if (a = 2)
if (a = 3)
b <- 3
else b <- 4
elif (a = 5) return
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))