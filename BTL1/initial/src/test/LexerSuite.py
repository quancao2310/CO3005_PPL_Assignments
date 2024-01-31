import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 100-110: Simple Cases
    * 111-119: ID
    * 120-126: Operators, Separators, Keywords
    * 127-136: Numbers, Comments
    * 137-148: Strings
    * 149-159: Expressions
    * 160-169: Statements
    * 170-199: Mixed Cases
    """
    
    # Simple Cases
    def test_100(self):
        # Integer literals
        input = "0 4 9 16 20 29252 8241 1212 12124 0 214124 2091284 19004"
        expect = "0,4,9,16,20,29252,8241,1212,12124,0,214124,2091284,19004,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 100))
    
    def test_101(self):
        # Float literals
        input = "1234.5678"
        expect = "1234.5678,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))
    
    def test_102(self):
        # String literals
        input = "\"simple string\""
        expect = "simple string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))
    
    def test_103(self):
        # Boolean literals
        input = "true false true false true"
        expect = "true,false,true,false,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))
    
    def test_104(self):
        # Operators
        input = "+ - * /"
        expect = "+,-,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))
    
    def test_105(self):
        # Separators
        input = "(())"
        expect = "(,(,),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))
    
    def test_106(self):
        # Comment
        input = "## This is a comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))
    
    def test_107(self):
        # Identifiers (ID)
        input = "id1 id2 id3 id4"
        expect = "id1,id2,id3,id4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))
    
    def test_108(self):
        # Keywords
        input = "if elif else"
        expect = "if,elif,else,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))
    
    def test_109(self):
        # Arrays
        input = "[1, 2, 3, 4]"
        expect = "[,1,,,2,,,3,,,4,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))
    
    def test_110(self):
        # Escape Characters
        input = "SOS\b\r\t\f\nHUHU"
        expect = "SOS,\n,HUHU,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))
    
    # ID
    def test_111(self):
        # Lower case
        input = "this is a very interesting subject"
        expect = "this,is,a,very,interesting,subject,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))
    
    def test_112(self):
        # Upper case
        input = "ABC DEF"
        expect = "ABC,DEF,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))
    
    def test_113(self):
        # Alphabetic characters
        input = "aAbBcC AaBbCc"
        expect = "aAbBcC,AaBbCc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))
    
    def test_114(self):
        # Alphanumeric characters
        input = "aBc123 DeF456 g7h8i9"
        expect = "aBc123,DeF456,g7h8i9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))
    
    def test_115(self):
        # Underscore
        input = "a_0 a_1 b2_3 c_C2 De_f _abc _123"
        expect = "a_0,a_1,b2_3,c_C2,De_f,_abc,_123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))
    
    def test_116(self):
        # Case sensitive
        input = "chipi ChIpI cHaPi CHAPI"
        expect = "chipi,ChIpI,cHaPi,CHAPI,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
    
    def test_117(self):
        # Illegal ID 1 (results in mixing with other tokens)
        input = "1abc )def[ (John] A++ ...--msg=hello world"
        expect = "1,abc,),def,[,(,John,],A,+,+,...,-,-,msg,=,hello,world,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))
    
    def test_118(self):
        # Illegal ID 2 (with illegal characters)
        input = "SOS#SOS"
        expect = "SOS,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 118))
    
    def test_119(self):
        # Illegal ID 3 (ID starts with numbers)
        input = "8X 9X 10_xyz"
        expect = "8,X,9,X,10,_xyz,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))
    
    # Operators, Separators, Keywords
    def test_120(self):
        # All operators
        input = "+ - * / % not and or = <- != < <= > >= ... =="
        expect = "+,-,*,/,%,not,and,or,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 120))
    
    def test_121(self):
        # Advanced operators combinations
        input = "+%-...<-%-====+<-<<====+**=<=>=/*+<-"
        expect = "+,%,-,...,<-,%,-,==,==,+,<-,<,<=,==,=,+,*,*,=,<=,>=,/,*,+,<-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))
    
    def test_122(self):
        # All separators, including end-of-line (\n)
        input = "( ) [ ] , \n"
        expect = "(,),[,],,,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))
    
    def test_123(self):
        # Advanced separators combinations
        input = """([(][((],,[[(
)]\n]\n[])],),
,))\n\n)()]]["""
        expect = """(,[,(,],[,(,(,],,,,,[,[,(,\n,),],\n,],\n,[,],),],,,),,,\n,,,),),\n,\n,),(,),],],[,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 123))
    
    def test_124(self):
        # All keywords
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))
    
    def test_125(self):
        # Numbers + Operators Combinations
        input = "2!=*9<-115>912<*1218>2==8!=<-<->=85"
        expect = "2,!=,*,9,<-,115,>,912,<,*,1218,>,2,==,8,!=,<-,<-,>=,85,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))
    
    def test_126(self):
        # Separators + Operators Combinations
        input = ")!=*<-((\n>()<*()(>)==!=<-<->=\n!=+!=<<-,"
        expect = "),!=,*,<-,(,(,\n,>,(,),<,*,(,),(,>,),==,!=,<-,<-,>=,\n,!=,+,!=,<,<-,,,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))
    
    # Numbers, Comments
    def test_127(self):
        # Multiple zeros
        input = "001 002 003 0010 001234"
        expect = "001,002,003,0010,001234,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))
    
    def test_128(self):
        # Float with decimal part only
        input = "1.2 9. 9.0 9.01 02.3 005.05130"
        expect = "1.2,9.,9.0,9.01,02.3,005.05130,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))
    
    def test_129(self):
        # Float with exponential part only
        input = "1e2 1e+20 1e-200 3E04 3E+04 4E-4 0e1 0E-1"
        expect = "1e2,1e+20,1e-200,3E04,3E+04,4E-4,0e1,0E-1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))
    
    def test_130(self):
        # Float with both decimal and exponential parts
        input = "0.0482 12. 12.3 12e3 2E-1 2e-1 231E+10 12.3e3 12.3e-30 9.e01"
        expect = "0.0482,12.,12.3,12e3,2E-1,2e-1,231E+10,12.3e3,12.3e-30,9.e01,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))
    
    def test_131(self):
        # Error Float
        input = "123E"
        expect = "123,E,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))
    
    def test_132(self):
        # Illegal numbers (results in mixing with other tokens)
        input = "18aa928mas 92.E+3ajds+450e3-4 4-01"
        expect = "18,aa928mas,92.E+3,ajds,+,450e3,-,4,4,-,01,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))
    
    def test_133(self):
        # Multiple comments
        input = """## Hello world
##This is some comments"""
        expect = """\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 133))
    
    def test_134(self):
        # Multiple comments with escape characters
        input = """## Hello world \\n\\b\\e\\z\\r\\f \\\\a \\\\b \\c
## This is something that you would not understand"""
        expect = "\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))
    
    def test_135(self):
        # ## in comments
        input = "## Comment 1 ## Comment 2"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))
    
    def test_136(self):
        # Mix numbers with comments
        input = "0 1.2 3E4 5e+6 7.8e-9 ## These are some valid number literals in ZCode"
        expect = "0,1.2,3E4,5e+6,7.8e-9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))
    
    # Strings
    def test_137(self):
        # End-of-line Characters in string
        input = r""" "abc\n\n\ndef" """
        expect = r"""abc\n\n\ndef,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 137))
    
    def test_138(self):
        # Other escape characters in string
        # Actual string of this test case is "escape \b \r \t \f \n \' \\ characters"
        input = r""" "escape \b \r \t \f \n \' \\ characters" """
        expect = r"""escape \b \r \t \f \n \' \\ characters,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 138))
    
    def test_139(self):
        # The double-quote character (escaped by single-quote)
        input = """ "He asked me: \'"Where is John?\'"" """
        expect = """He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 139))
    
    def test_140(self):
        # String of special characters of ZCode (should behave normally)
        input = """ "#%*()_+-=<>/" """
        expect = """#%*()_+-=<>/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 140))
    
    def test_141(self):
        # String with comments
        input = """"lorem ipsum 1 ## comments"
## Real comments "lorem ipsum 2"
"lorem ipsum 3" """
        expect = """lorem ipsum 1 ## comments,\n,\n,lorem ipsum 3,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141))
    
    def test_142(self):
        # Multiple strings
        input = """ "ABC" "DEF" "GHI" "1234" """
        expect = """ABC,DEF,GHI,1234,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 142))
    
    def test_143(self):
        # UncloseString Error
        input = """ "unclosed.."""
        expect = """Unclosed String: unclosed.."""
        self.assertTrue(TestLexer.test(input, expect, 143))
    
    def test_144(self):
        # IllegalEscape Error
        input = r""" "a string with some \r\n\t \a \e \i \o \u" """
        expect = r"""Illegal Escape In String: a string with some \r\n\t \a"""
        self.assertTrue(TestLexer.test(input, expect, 144))
    
    def test_145(self):
        # One string spanned on multiple lines => results in UncloseString Error
        input = """a <- "String that spanned
on multiple
lines" """
        expect = """a,<-,Unclosed String: String that spanned"""
        self.assertTrue(TestLexer.test(input, expect, 145))
    
    def test_146(self):
        # Unclose string with illegal escape characters
        input = r"""a <- "String with something: \a"""
        expect = r"""a,<-,Illegal Escape In String: String with something: \a"""
        self.assertTrue(TestLexer.test(input, expect, 146))
    
    def test_147(self):
        # Single-quote character (both escaped and unescaped)
        input = r"""a <- "SQ1: ' - SQ2: \' - All accepted!" """
        expect = r"""a,<-,SQ1: ' - SQ2: \' - All accepted!,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147))
    
    def test_148(self):
        #!! Escaping the single-quote and then write a double-quote next to it => Unclosed String
        input = r""""John\'"" """
        expect = r"""John\',Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 148))
    
    # Expressions
    def test_149(self):
        #
        input = """"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 149))
    
    # Statements
    
    # Mixed Cases
    def test_170(self):
        input = """## This is a single comment.
a <- 5
### This is the second comment."""
        expect = """\n,a,<-,5,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 170))
    
    # def test_199(self):
    #     self.assertTrue(TestLexer.test("", "<EOF>", 199))
