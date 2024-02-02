import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 200-204: Types
    * 205-229: Declarations
    * 230-239: Expressions
    * 240-269: Statements
    * 270-299: Mixed Cases
    """
    
    # Types
    def test_200(self):
        # Boolean
        input = """bool a
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    
    def test_201(self):
        # Number
        input = """number a
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_202(self):
        # String
        input = """string a
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    def test_203(self):
        # 1-dimensional array
        input = """number a[10]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_204(self):
        # Multi-dimensional array
        input = """bool a[10, 20, 30]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    # Declarations
    def test_205(self):
        # Boolean declaration
        input = """bool a
        bool b <- true
        bool c <- false
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    
    def test_206(self):
        # Number declaration
        input = """number a
number b <- 1
number c <- 2.5
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    
    def test_207(self):
        # String declaration
        input = """string a
string b <- "PPL Assignment"
string c <- "This is a string \\n"

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    
    def test_208(self):
        # Invalid string token
        input = """string s <- "This is an invalid string: \\f \\a \\b \\n"
"""
        expect = """This is an invalid string: \\f \\a"""
        self.assertTrue(TestParser.test(input, expect, 208))
    
    def test_209(self):
        # Keyword "var" and "dynamic" declaration
        input = """var x <- 1
var y <- true
var z <- "str"

dynamic x <- 1
dynamic y
dynamic z <- "str"
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))
    
    def test_210(self):
        # Array declaration
        input = """number a[5] <- [2, 3, 5, 7, 11]
string sss[4] <- ["PPL", "is", "very", "hard"]
bool abc[4] <- [true, true, false, false]

number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
bool c[2, 2, 3] <- [[[true, true, false], [true, true, false]], [[true, true, false], [true, true, false]]]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test_211(self):
        # Declaration with comments
        input = """bool a
## Comment 1
bool b <- true ## Comment 2
######## Comment 3
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_212(self):
        # Invalid array declaration 1: Initialize non-array expression to array variable
        input = """number x[2] <- 2
"""
        expect = "Error on line 1 col 15: 2"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test_213(self):
        # Invalid array declaration 2: Initialize array with wrong dimensions 1
        input = """number x[2.3e1] <- [1, 2, 3]
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_214(self):
        # Invalid array declaration 3: Initialize array with wrong dimensions 2
        input = """number x[3, 4] <- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test_215(self):
        # Invalid array declaration 4: Wrong element types
        input = """number arr[4] <- [1, true, 3, "x"]
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test_216(self):
        # Invalid array declaration 5: Use var-keyword
        input = """var arr[4] <- [1, 2, 3, 4]
"""
        expect = """Error on line 1 col 7: ["""
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test_217(self):
        # Invalid declaration 1: var-keyword without initialization
        input = """var x <- 1
var y
"""
        expect = """Error on line 2 col 6: \n"""
        self.assertTrue(TestParser.test(input, expect, 217))
    
    def test_218(self):
        # Invalid declaration 2: wrong type (will not give error now)
        input = """string s <- 123
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_219(self):
        # Invalid declaration 3: wrong token
        input = """number s <= "abc"
"""
        expect = """Error on line 1 col 9: <="""
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_220(self):
        # Function declaration
        input = """func main()
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 220))
    
    def test_221(self):
        # Function with return statement
        input = """func main() return 1
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))
    
    def test_222(self):
        # Function with block statement
        input = """func main() begin
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))
    
    def test_223(self):
        # Function with 1 parameter
        input = """
func foo(number x)
begin
    return x
end

func main() begin
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))
    
    def test_224(self):
        # Function with many parameters
        input = """func foo(number x, number y, string s[9])
begin
    s[5] <- "Awesome"
    return x + y
end

func main() begin
    foo(1, 2, "xyz")
    return
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))
    
    def test_225(self):
        # Function with local variables
        input = """func main()
begin

number a
string b <- "x"
var c <- false

end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test_226(self):
        # Function with declaration and implementation parts
        input = """func bar(number x)

func main() begin
    number a <- bar(2024)
    string b <- bar("John")
    writeNumber(a)
end


func bar(number x)
begin
    return x + 1
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226))
    
    def test_227(self):
        # Function with global variables
        input = """number MOD <- 1e9 + 7
number _val1 <- 1000
number _val2 <- 20.24
func main()
begin
    writeNumber(_val1 % MOD)
    writeNumber(_val2 % MOD)
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))
    
    def test_228(self):
        # Invalid function declaration 1: Unclosed function
        input = """func main()
begin
number a
string b <- "x"
var c <- false

func foo()
"""
        expect = """Error on line 7 col 0: func"""
        self.assertTrue(TestParser.test(input, expect, 228))
    
    def test_229(self):
        # Invalid function declaration 2: Error token
        input = """func main() {
    number a
    string b <- "x"
    var c <- false
}
"""
        expect = """{"""
        self.assertTrue(TestParser.test(input, expect, 229))
    
    # Expressions
    def test_230(self):
        # Number expressions
        input = """
number a <- x + y
number a <- x - y
number a <- x * y
number a <- x / y
number a <- x % y
number a <- -x
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))
    
    def test_231(self):
        # Boolean and relational expressions
        input = """
bool a <- x and y
bool a <- x or y
bool a <- not y

bool a <- x = y
bool a <- x != y
bool a <- x < y
bool a <- x <= y
bool a <- x > y
bool a <- x >= y
bool a <- x == y
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test_232(self):
        # String and indexing expressions
        input = """
string a <- x...y

var x <- arr[1, 2, 3]

func main() begin
    a[3 + foo(2), x, y] <- a[b[2, 3]] + 4
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))
    
    def test_233(self):
        # Function call expression and sub-expression
        input = """
dynamic a <- foo(213)
dynamic a <- bar(foo("x" + 4.213))
dynamic a <- (foo() + 2) * "adsad"
dynamic a <- -(x + x)*(x-x) ... foo(x, y, z)
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test_234(self):
        # Unary operators
        input = """func main()
begin
    var x <- -1
    var x <- --1
    var x <- ---1
    var x <- ----1
    var x <- -----1
    var x <--------1
    
    var y <- not x
    var y <- not not x
    var y <- not not not x
    var y <- not not not not not not x
    
    var z <- a[1]
    var z <- a[1, 2, a[3]]
    var z <- a[1, "a", "B"]
    var z <- a[[true, false]]
end
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test_235(self):
        # Complex expressions
        input = """
number a <- ((a + b - c) * (d / e)) + ((f % g) - ((h % i) + (j / k) * (l + m) / (n - o))) + (p * q)
number b <- ((a1 + a2) * a3) / (a1 - a2) % (a1 != a2) and (not (a3 < a2) or (a1 <= a3 and (a2 >= a1 or (a3 == a2 and (a1 != a2))))) or (a1 + a2) * (a3 > a2) / (a1 <= a3)
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))
    
    def test_236(self):
        # Invalid expression 1: Non-associative operators
        # Relational operators (!=) does not have associativity so you have to use parentheses to calculate this expression
        input = """number a <- a3 == a2 and a1 != a2
"""
        expect = """Error on line 1 col 28: !="""
        self.assertTrue(TestParser.test(input, expect, 236))
    
    def test_237(self):
        # Invalid expression 2: Missing argument in function call
        input = """bool a <- foo(1,2,)
"""
        expect = """Error on line 1 col 18: )"""
        self.assertTrue(TestParser.test(input, expect, 237))
    
    def test_238(self):
        # Invalid expression 3: Unclosed indexing
        input = """func void()
begin
string x <- a[0 ... "asdas'"da\\f"
end
"""
        expect = """Error on line 3 col 34: \n"""
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def test_239(self):
        # Invalid expression 4: Missing operand
        input = """func f()
begin
string x <- 1+----123+/aaajam
end
"""
        expect = """Error on line 3 col 22: /"""
        self.assertTrue(TestParser.test(input, expect, 239))
    
    # Statements
    def test_240(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240))
    
    def test_241(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))
    
    def test_242(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test_243(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test_244(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test_245(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_246(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246))
    
    def test_247(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))
    
    def test_248(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))
    
    def test_249(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 249))
    
    def test_250(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))
    
    def test_251(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_252(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252))
    
    def test_253(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))
    
    def test_254(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 254))
    
    def test_255(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))
    
    def test_256(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 256))
    
    def test_257(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def test_258(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))
    
    def test_259(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))
    
    def test_260(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_261(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))
    
    def test_262(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 262))
    
    def test_263(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_264(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def test_265(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))
    
    def test_266(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))
    
    def test_267(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))
    
    def test_268(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))
    
    def test_269(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 269))
    
    def test_270(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270))
    
    def test_271(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def test_272(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test_273(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test_274(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))
    
    def test_275(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test_276(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))
    
    def test_277(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test_278(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test_279(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test_280(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))
    
    def test_281(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))
    
    def test_282(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 282))
    
    def test_283(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test_284(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test_285(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 285))
    
    def test_286(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286))
    
    def test_287(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))
    
    def test_288(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 288))
    
    def test_289(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289))
    
    def test_290(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test_291(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_292(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 292))
    
    def test_293(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 293))
    
    def test_294(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 294))
    
    def test_295(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 295))
    
    def test_296(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test_297(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_298(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 298))
    
    def test_299(self):
        # 
        input = """"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 299))
#     def test_201(self):
#         # 
#         input = """func main()
# begin
# if (a = 1)
# if (a = 2)
# if (a = 3)
# b <- 3
# else b <- 4
# elif (a = 5) return
# end
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, ))
    
    # Mixed Cases
