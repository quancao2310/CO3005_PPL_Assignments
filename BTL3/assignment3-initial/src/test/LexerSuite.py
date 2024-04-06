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
        input = """SOS\b\t\f\nHUHU"""
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
        input = "chipi ChIpI cHaPa CHAPA"
        expect = "chipi,ChIpI,cHaPa,CHAPA,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
    
    def test_117(self):
        # Illegal ID 1 (results in mixing with other tokens)
        input = "1abc )fed[ (John] A++ ...--msg=hello world"
        expect = "1,abc,),fed,[,(,John,],A,+,+,...,-,-,msg,=,hello,world,<EOF>"
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
        # Comment in comment
        input = "## Comment 1 ## Comment 2"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))
    
    def test_136(self):
        # Mix numbers with comment
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
        # Escaping the single-quote and then write a double-quote next to it => Unclosed String
        input = r""""John\'"" """
        expect = r"""John\',Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 148))
    
    # Expressions
    def test_149(self):
        # Simple expression
        input = "1 + 1 = 2"
        expect = "1,+,1,=,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))
    
    def test_150(self):
        # Number expressions
        input = "number a <- --x + y - y * y / y % y"
        expect = "number,a,<-,-,-,x,+,y,-,y,*,y,/,y,%,y,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))
    
    def test_151(self):
        # Boolean and relational expressions
        input = """bool a <- not x and y or y
x = y, x != y, x < y, x <= y, x > y, x >= y, x == y"""
        expect = "bool,a,<-,not,x,and,y,or,y,\n,x,=,y,,,x,!=,y,,,x,<,y,,,x,<=,y,,,x,>,y,,,x,>=,y,,,x,==,y,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))
    
    def test_152(self):
        # String and indexing expressions
        input = """string a <- x...y
var x <- arr[1]
func main() begin
    a[3 + foo(2), x, y] <- a[b[2, 3]] + 4
end
"""
        expect = "string,a,<-,x,...,y,\n,var,x,<-,arr,[,1,],\n,func,main,(,),begin,\n,a,[,3,+,foo,(,2,),,,x,,,y,],<-,a,[,b,[,2,,,3,],],+,4,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))
    
    def test_153(self):
        # Function call expression and sub-expression
        input = 'dynamic a <- foo(213) and bar(foo("x" + 4.213)) + ((foo() + 2) * "adsad" / -(x + x)*(x-x) ... foo(x, y, z))'
        expect = "dynamic,a,<-,foo,(,213,),and,bar,(,foo,(,x,+,4.213,),),+,(,(,foo,(,),+,2,),*,adsad,/,-,(,x,+,x,),*,(,x,-,x,),...,foo,(,x,,,y,,,z,),),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))
    
    def test_154(self):
        # Unary operators
        input = "var x <--------------1"
        expect = "var,x,<-,-,-,-,-,-,-,-,-,-,-,-,-,-,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))
    
    def test_155(self):
        # Complex expressions
        input = "((a + b - c) * d / e) + (j / k) * l + (p * q)"
        expect = "(,(,a,+,b,-,c,),*,d,/,e,),+,(,j,/,k,),*,l,+,(,p,*,q,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))
    
    def test_156(self):
        # Invalid expression 1: Non-associative operators
        input = "number a <- a3 == a2 and a1 != a2"
        expect = "number,a,<-,a3,==,a2,and,a1,!=,a2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))
    
    def test_157(self):
        # Invalid expression 2: Missing argument in function call
        input = "bool a <- foo(1,2,)"
        expect = "bool,a,<-,foo,(,1,,,2,,,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))
    
    def test_158(self):
        # Invalid expression 3: Unclosed indexing
        input = """string x <- a[0 ... "asdas'"da\\f" """
        expect = """string,x,<-,a,[,0,...,asdas'"da\\f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))
    
    def test_159(self):
        # Invalid expression 4: Missing operand
        input = "string x <- 1+----123+/aaajam"
        expect = "string,x,<-,1,+,-,-,-,-,123,+,/,aaajam,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))
    
    # Statements
    def test_160(self):
        # Assignment statement
        input = "l[3] <- value * aPi"
        expect = "l,[,3,],<-,value,*,aPi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))
    
    def test_161(self):
        # Block statement
        input = """begin
number r
r <- 2.0
end
"""
        expect = "begin,\n,number,r,\n,r,<-,2.0,\n,end,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))
    
    def test_162(self):
        # If statement
        input = "if (a = 1) writeBool(true)"
        expect = "if,(,a,=,1,),writeBool,(,true,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))
    
    def test_163(self):
        # If statement: nested if
        input = "if (a = 1) if (b = 1) writeString(s)"
        expect = "if,(,a,=,1,),if,(,b,=,1,),writeString,(,s,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))
    
    def test_164(self):
        # If-elif-else statement
        input = """if (a = 1) s <- "1"
elif (a = 2) s <- "2"
else s <- "3"
"""
        expect = "if,(,a,=,1,),s,<-,1,\n,elif,(,a,=,2,),s,<-,2,\n,else,s,<-,3,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))
    
    def test_165(self):
        # For statement
        input = "for i until i >= 10 by 1 writeNumber(i)"
        expect = "for,i,until,i,>=,10,by,1,writeNumber,(,i,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))
    
    def test_166(self):
        # Break statement
        input = "for i until i = 20 by 1 if (i = 10) break"
        expect = "for,i,until,i,=,20,by,1,if,(,i,=,10,),break,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))
    
    def test_167(self):
        # Continue statement
        input = "for i until i = 0 by -1 if (i >= 10) continue"
        expect = "for,i,until,i,=,0,by,-,1,if,(,i,>=,10,),continue,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))
    
    def test_168(self):
        # Return statement
        input = "return return 1 return t*p"
        expect = "return,return,1,return,t,*,p,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))
    
    def test_169(self):
        # Function call statement
        input = """foo()
pow(2, 3)
pow(pow(2, 3), pow(4, 2))
"""
        expect = "foo,(,),\n,pow,(,2,,,3,),\n,pow,(,pow,(,2,,,3,),,,pow,(,4,,,2,),),\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))
    
    # Mixed Cases
    def test_170(self):
        # Random tokens 1
        input = """ and and	not	]
begin var var for -	continue
or ,	( by
string return "abcd" ... )	a1	> - bool	for until
) ) continue
"""
        expect = """and,and,not,],
,begin,var,var,for,-,continue,
,or,,,(,by,
,string,return,abcd,...,),a1,>,-,bool,for,until,
,),),continue,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 170))
    
    def test_171(self):
        # Random tokens 2
        input = """	)	not begin
true	by
for begin >=	and	!= begin end	%
<	102.1
end <- <	121	!=
<
> <= [ dynamic
continue	= number	return	< , ]	>=	end = end end	else ...	% != - ] func ==	func > elif	< %
by	,	until	"abcd"
break	dynamic break false	] = func continue
return >
"""
        expect = """),not,begin,
,true,by,
,for,begin,>=,and,!=,begin,end,%,
,<,102.1,
,end,<-,<,121,!=,
,<,
,>,<=,[,dynamic,
,continue,=,number,return,<,,,],>=,end,=,end,end,else,...,%,!=,-,],func,==,func,>,elif,<,%,
,by,,,until,abcd,
,break,dynamic,break,false,],=,func,continue,
,return,>,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 171))
    
    def test_172(self):
        # Random tokens 3
        input = """ %
=
elif ) else	
	bool	number number	continue	/	elif and var
!=	and
elif continue	"abcd" a1	<= false <-
133.68 number
break	>=	* continue elif	a1 elif	elif
46e121	if * 126.9E-5776 string
%	elif	dynamic number	false
<=	( false	*	>=
, until	!=	)
break
[	string	continue [	or 71.49e-5776	%
begin - ... 
 
 continue	==	until	(
<- ) 42.62 bool	func >=	or until	continue	return	if	break
    """
        expect = """%,
,=,
,elif,),else,
,bool,number,number,continue,/,elif,and,var,
,!=,and,
,elif,continue,abcd,a1,<=,false,<-,
,133.68,number,
,break,>=,*,continue,elif,a1,elif,elif,
,46e121,if,*,126.9E-5776,string,
,%,elif,dynamic,number,false,
,<=,(,false,*,>=,
,,,until,!=,),
,break,
,[,string,continue,[,or,71.49e-5776,%,
,begin,-,...,
,
,continue,==,until,(,
,<-,),42.62,bool,func,>=,or,until,continue,return,if,break,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 172))
    
    def test_173(self):
        # Random tokens 4
        input = " true = <- elif <- &"
        expect = "true,=,<-,elif,<-,Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 173))
    
    def test_174(self):
        # Random tokens 5
        input = " [ STRINGLIT else until / <= == ^"
        expect = "[,STRINGLIT,else,until,/,<=,==,Error Token ^"
        self.assertTrue(TestLexer.test(input, expect, 174))
    
    def test_175(self):
        # Random tokens 6
        input = """func fAqCy41(put8fbW) 
 begin 
func fci4bwp(p3HkPQh) 
 begin 
var v74jw0H <-2936
 end
 end
"""
        expect = """func,fAqCy41,(,put8fbW,),
,begin,
,func,fci4bwp,(,p3HkPQh,),
,begin,
,var,v74jw0H,<-,2936,
,end,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 175))
    
    def test_176(self):
        # Random tokens 7
        input = """+ ...\tbreak and
... and return\tby   bool
continue\t> ( ,
or -\t+\t"abcd" -\t+ and        ]
and [" qQJEAOtaT \\# "
< else"""
        expect = "+,...,break,and,\n,...,and,return,by,bool,\n,continue,>,(,,,\n,or,-,+,abcd,-,+,and,],\n,and,[,Illegal Escape In String:  qQJEAOtaT \\#"
        self.assertTrue(TestLexer.test(input, expect, 176))
    
    def test_177(self):
        # Random tokens 8
        input = """	dynamic ...
%	until	<	until	break
until <- ( / 45	-	func
, and

	[ end	% [	if - , >="""
        expect = """dynamic,...,
,%,until,<,until,break,
,until,<-,(,/,45,-,func,
,,,and,
,
,[,end,%,[,if,-,,,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 177))
    
    def test_178(self):
        # Random tokens 9
        input = """	dynamic ...
%	until	<	until	break" boiV \n "
until <- ( / 45	-	func
, and

	[ end	% [	if - , >="""
        expect = "dynamic,...,\n,%,until,<,until,break,Unclosed String:  boiV "
        self.assertTrue(TestLexer.test(input, expect, 178))
    
    def test_179(self):
        # Random tokens 10
        input = """ func
"abcd"	!= bool	bool +
break , until break "abcd"	] +
[ a1
for
a1	end end !=	continue ("""
        expect = """func,
,abcd,!=,bool,bool,+,
,break,,,until,break,abcd,],+,
,[,a1,
,for,
,a1,end,end,!=,continue,(,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 179))
    
    def test_180(self):
        # Comments with statements
        input = """## This is a single comment.
a <- 5
### This is the second comment."""
        expect = "\n,a,<-,5,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180))
    
    def test_181(self):
        # Simple program
        input = """func main() return 1
"""
        expect = "func,main,(,),return,1,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))
    
    def test_182(self):
        # Print array
        input = """func printArr(number a[100], number length)
begin
    var i <- 0
    for i until i >= length by 1 begin
        writeNumber(a[i])
        writeString(" ")
    end
    writeString("\\n")
end
"""
        expect = """func,printArr,(,number,a,[,100,],,,number,length,),
,begin,
,var,i,<-,0,
,for,i,until,i,>=,length,by,1,begin,
,writeNumber,(,a,[,i,],),
,writeString,(, ,),
,end,
,writeString,(,\\n,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 182))
    
    def test_183(self):
        # Find maximum in array
        input = """func max(number a[100], number length)
begin
    if (length <= 0)
        return -1e9 ## Represent negative infinity
    var max <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] > max) max <- a[i]
    return max
end
"""
        expect = """func,max,(,number,a,[,100,],,,number,length,),
,begin,
,if,(,length,<=,0,),
,return,-,1e9,
,var,max,<-,a,[,0,],
,var,i,<-,0,
,for,i,until,i,>=,length,by,1,
,if,(,a,[,i,],>,max,),max,<-,a,[,i,],
,return,max,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 183))
    
    def test_184(self):
        # Linear search
        input = """func find(number arr[100], number length, number element)
begin
    var i <- 0
    for i until i >= length by 1
        if (arr[i] = element) return i
    return -1
end
"""
        expect = """func,find,(,number,arr,[,100,],,,number,length,,,number,element,),
,begin,
,var,i,<-,0,
,for,i,until,i,>=,length,by,1,
,if,(,arr,[,i,],=,element,),return,i,
,return,-,1,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))
    
    def test_185(self):
        # Binary search
        input = """func find(number arr[100], number length, number element)
begin
    var left <- 0
    var right <- length - 1
    number mid
    for _ until left > right by 0 begin
        mid <- (left + right) / 2
        if (element = arr[mid]) return mid
        elif (element > arr[mid]) left <- mid + 1
        else right <- mid - 1
    end
    return -1
end
"""
        expect = """func,find,(,number,arr,[,100,],,,number,length,,,number,element,),
,begin,
,var,left,<-,0,
,var,right,<-,length,-,1,
,number,mid,
,for,_,until,left,>,right,by,0,begin,
,mid,<-,(,left,+,right,),/,2,
,if,(,element,=,arr,[,mid,],),return,mid,
,elif,(,element,>,arr,[,mid,],),left,<-,mid,+,1,
,else,right,<-,mid,-,1,
,end,
,return,-,1,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185))
    
    def test_186(self):
        # Interpolation search
        input = """func interpolationSearch(number arr[100], number element, number left, number right)
begin
    if ((left > right) or (element < arr[left]) or (element > arr[right])) return -1
    number pos <- left + (right - left)*(element - arr[left])/(arr[right] - arr[left])
    if (element = arr[pos]) return pos
    else if (element < arr[pos]) return interpolationSearch(arr, element, left, pos-1)
    return interpolationSearch(arr, element, pos+1, right)
end
"""
        expect = """func,interpolationSearch,(,number,arr,[,100,],,,number,element,,,number,left,,,number,right,),
,begin,
,if,(,(,left,>,right,),or,(,element,<,arr,[,left,],),or,(,element,>,arr,[,right,],),),return,-,1,
,number,pos,<-,left,+,(,right,-,left,),*,(,element,-,arr,[,left,],),/,(,arr,[,right,],-,arr,[,left,],),
,if,(,element,=,arr,[,pos,],),return,pos,
,else,if,(,element,<,arr,[,pos,],),return,interpolationSearch,(,arr,,,element,,,left,,,pos,-,1,),
,return,interpolationSearch,(,arr,,,element,,,pos,+,1,,,right,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186))
    
    def test_187(self):
        # Jump search
        input = """func jumpSearch(number arr[100], number n, number element)
begin
    number m <- sqrt(n)
    number k <- 0
    for k until k*m >= n by 1 begin
        if (element = arr[k*m]) return k*m
        if (element < arr[k*m]) break
    end
    k <- k - 1
    number i <- k*m + 1
    for i until i >= (k+1)*m by 1 begin
        if ((i >= n) or (element < arr[i])) break
        if (element = arr[i]) return i
    end
    return -1
end
"""
        expect = """func,jumpSearch,(,number,arr,[,100,],,,number,n,,,number,element,),
,begin,
,number,m,<-,sqrt,(,n,),
,number,k,<-,0,
,for,k,until,k,*,m,>=,n,by,1,begin,
,if,(,element,=,arr,[,k,*,m,],),return,k,*,m,
,if,(,element,<,arr,[,k,*,m,],),break,
,end,
,k,<-,k,-,1,
,number,i,<-,k,*,m,+,1,
,for,i,until,i,>=,(,k,+,1,),*,m,by,1,begin,
,if,(,(,i,>=,n,),or,(,element,<,arr,[,i,],),),break,
,if,(,element,=,arr,[,i,],),return,i,
,end,
,return,-,1,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 187))
    
    def test_188(self):
        # Bubble sort
        input = """func bubbleSort(number arr[100], number length)
begin
    number i <- 1
    for i until i >= length by 1 begin
        number j <- length - 1
        for j until j < i by -1
            if (arr[j] < arr[j - 1]) swap(arr, j, j - 1)
    end
end
"""
        expect = """func,bubbleSort,(,number,arr,[,100,],,,number,length,),
,begin,
,number,i,<-,1,
,for,i,until,i,>=,length,by,1,begin,
,number,j,<-,length,-,1,
,for,j,until,j,<,i,by,-,1,
,if,(,arr,[,j,],<,arr,[,j,-,1,],),swap,(,arr,,,j,,,j,-,1,),
,end,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188))
    
    def test_189(self):
        # Selection sort
        input = """func selectionSort(number arr[100], number length)
begin
    number i <- 0
    for i until i >= length-1 by 1 begin
        number min_idx <- i
        number j <- i + 1
        for j until j >= length by 1
            if (arr[j] < arr[min_idx]) min_idx <- j
        swap(arr, i, min_idx)
    end
end
"""
        expect = """func,selectionSort,(,number,arr,[,100,],,,number,length,),
,begin,
,number,i,<-,0,
,for,i,until,i,>=,length,-,1,by,1,begin,
,number,min_idx,<-,i,
,number,j,<-,i,+,1,
,for,j,until,j,>=,length,by,1,
,if,(,arr,[,j,],<,arr,[,min_idx,],),min_idx,<-,j,
,swap,(,arr,,,i,,,min_idx,),
,end,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 189))
    
    def test_190(self):
        # Insertion sort
        input = """func insertionSort(number arr[100], number length)
begin
    number i <- 1
    for i until i >= length by 1 begin
        number tmp <- arr[i]
        number j <- i-1
        for j until ((j < 0) or (tmp >= arr[j])) by -1
            arr[j+1] <- arr[j]
        arr[j+1] <- tmp
    end
end
"""
        expect = """func,insertionSort,(,number,arr,[,100,],,,number,length,),
,begin,
,number,i,<-,1,
,for,i,until,i,>=,length,by,1,begin,
,number,tmp,<-,arr,[,i,],
,number,j,<-,i,-,1,
,for,j,until,(,(,j,<,0,),or,(,tmp,>=,arr,[,j,],),),by,-,1,
,arr,[,j,+,1,],<-,arr,[,j,],
,arr,[,j,+,1,],<-,tmp,
,end,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 190))
    
    def test_191(self):
        # Shell sort
        input = """func sortSegment(number arr[100], number length, number segment_idx, number k)
begin
    number i <- segment_idx + k
    for i until i >= length by k begin
        number tmp <- arr[i]
        number j <- i-k
        for j until ((j < 0) or (tmp >= arr[j])) by -k
            arr[j+k] <- arr[j]
        arr[j+k] <- tmp
    end
end

func shellSort(number arr[100], number length, number num_of_segment_list[10], number num_phases) begin
    number i <- num_phases-1
    for i until i < 0 by -1 begin
        number segment <- 0
        for segment until segment > num_of_segment_list[i] by 1
            sortSegment(arr, length, segment, num_of_segment_list[i])
    end
end
"""
        expect = """func,sortSegment,(,number,arr,[,100,],,,number,length,,,number,segment_idx,,,number,k,),
,begin,
,number,i,<-,segment_idx,+,k,
,for,i,until,i,>=,length,by,k,begin,
,number,tmp,<-,arr,[,i,],
,number,j,<-,i,-,k,
,for,j,until,(,(,j,<,0,),or,(,tmp,>=,arr,[,j,],),),by,-,k,
,arr,[,j,+,k,],<-,arr,[,j,],
,arr,[,j,+,k,],<-,tmp,
,end,
,end,
,
,func,shellSort,(,number,arr,[,100,],,,number,length,,,number,num_of_segment_list,[,10,],,,number,num_phases,),begin,
,number,i,<-,num_phases,-,1,
,for,i,until,i,<,0,by,-,1,begin,
,number,segment,<-,0,
,for,segment,until,segment,>,num_of_segment_list,[,i,],by,1,
,sortSegment,(,arr,,,length,,,segment,,,num_of_segment_list,[,i,],),
,end,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191))
    
    def test_192(self):
        # Merge sort
        input = """func round(number n) return n - n % 1
func merge(number arr[100], number left, number right, number mid) begin
    number left_length <- mid - left + 1
    number right_length <- right - mid
    number arr_left[50]
    number arr_right[50]
    
    number i <- 0
    number j <- 0
    
    for i until i >= left_length by 1
        arr_left[i] <- arr[left + i]
    for j until j >= right_length by 1
        arr_right[j] <- arr[mid + 1 + j]
    
    number k <- left
    for k until k > right by 1 begin
        if ((i < left_length) and ((j >= right_length) or (arr_left[i] <= arr_right[j]))) begin
            arr[k] <- arr_left[i]
            i <- i + 1
        end
        else begin
            arr[k] <- arr_right[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right) begin
    if (left >= right) return
    number mid <- round((left + right) / 2)
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, right, mid)
end
"""
        expect = """func,round,(,number,n,),return,n,-,n,%,1,
,func,merge,(,number,arr,[,100,],,,number,left,,,number,right,,,number,mid,),begin,
,number,left_length,<-,mid,-,left,+,1,
,number,right_length,<-,right,-,mid,
,number,arr_left,[,50,],
,number,arr_right,[,50,],
,
,number,i,<-,0,
,number,j,<-,0,
,
,for,i,until,i,>=,left_length,by,1,
,arr_left,[,i,],<-,arr,[,left,+,i,],
,for,j,until,j,>=,right_length,by,1,
,arr_right,[,j,],<-,arr,[,mid,+,1,+,j,],
,
,number,k,<-,left,
,for,k,until,k,>,right,by,1,begin,
,if,(,(,i,<,left_length,),and,(,(,j,>=,right_length,),or,(,arr_left,[,i,],<=,arr_right,[,j,],),),),begin,
,arr,[,k,],<-,arr_left,[,i,],
,i,<-,i,+,1,
,end,
,else,begin,
,arr,[,k,],<-,arr_right,[,j,],
,j,<-,j,+,1,
,end,
,end,
,end,
,
,func,mergeSort,(,number,arr,[,100,],,,number,left,,,number,right,),begin,
,if,(,left,>=,right,),return,
,number,mid,<-,round,(,(,left,+,right,),/,2,),
,mergeSort,(,arr,,,left,,,mid,),
,mergeSort,(,arr,,,mid,+,1,,,right,),
,merge,(,arr,,,left,,,right,,,mid,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192))
    
    def test_193(self):
        # Quick sort
        input = """func swap(number arr[100], number i, number j)
func partition(number arr[100], number left, number right) begin
    number pivot <- arr[left]
    number i <- left + 1
    number j <- right
    
    for i until i > j by 0 begin
        for i until ((i > j) or (arr[i] >= pivot)) by 1 begin
        end
        for j until ((i > j) or (arr[j] < pivot)) by -1 begin
        end
        if (i < j) begin
            swap(arr, i, j)
            i <- i + 1
            j <- j - 1
        end
    end
    swap(arr, j, left)
    return j
end

func quickSort(number arr[100], number left, number right) begin
    if (left >= right) return
    number pos <- partition(arr, left, right)
    quickSort(arr, left, pos - 1)
    quickSort(arr, pos + 1, right)
end
"""
        expect = """func,swap,(,number,arr,[,100,],,,number,i,,,number,j,),
,func,partition,(,number,arr,[,100,],,,number,left,,,number,right,),begin,
,number,pivot,<-,arr,[,left,],
,number,i,<-,left,+,1,
,number,j,<-,right,
,
,for,i,until,i,>,j,by,0,begin,
,for,i,until,(,(,i,>,j,),or,(,arr,[,i,],>=,pivot,),),by,1,begin,
,end,
,for,j,until,(,(,i,>,j,),or,(,arr,[,j,],<,pivot,),),by,-,1,begin,
,end,
,if,(,i,<,j,),begin,
,swap,(,arr,,,i,,,j,),
,i,<-,i,+,1,
,j,<-,j,-,1,
,end,
,end,
,swap,(,arr,,,j,,,left,),
,return,j,
,end,
,
,func,quickSort,(,number,arr,[,100,],,,number,left,,,number,right,),begin,
,if,(,left,>=,right,),return,
,number,pos,<-,partition,(,arr,,,left,,,right,),
,quickSort,(,arr,,,left,,,pos,-,1,),
,quickSort,(,arr,,,pos,+,1,,,right,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 193))
    
    def test_194(self):
        # Heap sort
        input = """func heapSort(number arr[100], number length)
begin
    buildHeap(arr, length) ## Build heap algorithm in next testcase
    
    var i <- length - 1
    for i until i < 0 by -1 begin
        swap(arr, 0, i)
        reHeapDown(arr, i, 0)
    end
end
"""
        expect = """func,heapSort,(,number,arr,[,100,],,,number,length,),
,begin,
,buildHeap,(,arr,,,length,),
,
,var,i,<-,length,-,1,
,for,i,until,i,<,0,by,-,1,begin,
,swap,(,arr,,,0,,,i,),
,reHeapDown,(,arr,,,i,,,0,),
,end,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 194))
    
    def test_195(self):
        # Build heap
        input = """func reHeapDown(number arr[100], number length, number index) begin
    number l <- 2*index + 1
    number r <- 2*index + 2
    number largest <- index
    if ((l < length) and (arr[l] > arr[largest])) largest <- l
    if ((r < length) and (arr[r] > arr[largest])) largest <- r
    if (largest != index) begin
        swap(arr, index, largest)
        reHeapDown(arr, length, largest)
    end
end

func buildHeap(number arr[100], number length) begin
    number internal <- round(length/2) - 1
    for internal until internal < 0 by -1
        reHeapDown(arr, length, internal)
end
"""
        expect = """func,reHeapDown,(,number,arr,[,100,],,,number,length,,,number,index,),begin,
,number,l,<-,2,*,index,+,1,
,number,r,<-,2,*,index,+,2,
,number,largest,<-,index,
,if,(,(,l,<,length,),and,(,arr,[,l,],>,arr,[,largest,],),),largest,<-,l,
,if,(,(,r,<,length,),and,(,arr,[,r,],>,arr,[,largest,],),),largest,<-,r,
,if,(,largest,!=,index,),begin,
,swap,(,arr,,,index,,,largest,),
,reHeapDown,(,arr,,,length,,,largest,),
,end,
,end,
,
,func,buildHeap,(,number,arr,[,100,],,,number,length,),begin,
,number,internal,<-,round,(,length,/,2,),-,1,
,for,internal,until,internal,<,0,by,-,1,
,reHeapDown,(,arr,,,length,,,internal,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 195))
    
    def test_196(self):
        # Insert an element into a heap
        input = """func reHeapUp(number arr[100], number length, number index) begin
    if (index = 0) return
    number parent <- round((index - 1)/2)
    if (arr[index] > arr[parent]) begin
        swap(arr, index, parent)
        reHeapUp(arr, length, parent)
    end
end

func insertHeap(number arr[100], number length, number element)
begin
    arr[length] <- element
    length <- length + 1
    reHeapUp(arr, length, length - 1)
    return length
end
"""
        expect = """func,reHeapUp,(,number,arr,[,100,],,,number,length,,,number,index,),begin,
,if,(,index,=,0,),return,
,number,parent,<-,round,(,(,index,-,1,),/,2,),
,if,(,arr,[,index,],>,arr,[,parent,],),begin,
,swap,(,arr,,,index,,,parent,),
,reHeapUp,(,arr,,,length,,,parent,),
,end,
,end,
,
,func,insertHeap,(,number,arr,[,100,],,,number,length,,,number,element,),
,begin,
,arr,[,length,],<-,element,
,length,<-,length,+,1,
,reHeapUp,(,arr,,,length,,,length,-,1,),
,return,length,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 196))
    
    def test_197(self):
        # Delete an element from a heap
        input = """func removeHeap(number arr[100], number length)
begin
    if (length <= 0) return
    var deleted <- arr[0]
    arr[0] <- arr[length - 1]
    length <- length - 1
    reHeapDown(arr, length, 0)
    return deleted
end
"""
        expect = """func,removeHeap,(,number,arr,[,100,],,,number,length,),
,begin,
,if,(,length,<=,0,),return,
,var,deleted,<-,arr,[,0,],
,arr,[,0,],<-,arr,[,length,-,1,],
,length,<-,length,-,1,
,reHeapDown,(,arr,,,length,,,0,),
,return,deleted,
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))
    
    def test_198(self):
        # Longest Increasing Subsequence (LIS)
        # Print the length of the longest increasing subsequence of array
        input = """func lis(number arr[100], number n) begin
    number lis[100]
    lis[0] <- 1
    
    number i <- 1
    for i until i >= n by 1 begin
        lis[i] <- 1
        
        number j <- 0
        for j until j >= i by 1
            if ((arr[i] > arr[j]) and (lis[j] + 1 > lis[i]))
                lis[i] <- lis[j] + 1
    end
    return max(lis, n)
end
"""
        expect = """func,lis,(,number,arr,[,100,],,,number,n,),begin,
,number,lis,[,100,],
,lis,[,0,],<-,1,
,
,number,i,<-,1,
,for,i,until,i,>=,n,by,1,begin,
,lis,[,i,],<-,1,
,
,number,j,<-,0,
,for,j,until,j,>=,i,by,1,
,if,(,(,arr,[,i,],>,arr,[,j,],),and,(,lis,[,j,],+,1,>,lis,[,i,],),),
,lis,[,i,],<-,lis,[,j,],+,1,
,end,
,return,max,(,lis,,,n,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))
    
    def test_199(self):
        # Longest Common Subsequence (LCS)
        # Print the length of the longest common subsequence of array (or strings)
        input = """func lcs(number arr1[100], number arr2[100], number m, number n) begin
    if ((m = 0) or (n = 0)) return 0
    if (arr1[m - 1] = arr2[n - 1]) return 1 + lcs(arr1, arr2, m - 1, n - 1)
    return max(lcs(arr1, arr2, m - 1, n), lcs(arr1, arr2, m, n - 1))
end
"""
        expect = """func,lcs,(,number,arr1,[,100,],,,number,arr2,[,100,],,,number,m,,,number,n,),begin,
,if,(,(,m,=,0,),or,(,n,=,0,),),return,0,
,if,(,arr1,[,m,-,1,],=,arr2,[,n,-,1,],),return,1,+,lcs,(,arr1,,,arr2,,,m,-,1,,,n,-,1,),
,return,max,(,lcs,(,arr1,,,arr2,,,m,-,1,,,n,),,,lcs,(,arr1,,,arr2,,,m,,,n,-,1,),),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))
