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
        # Illegal Escape error of string token
        input = """string s <- "This is an invalid string: \\f \\a \\b \\n"
"""
        expect = """This is an invalid string: \\f \\a"""
        self.assertTrue(TestParser.test(input, expect, 208))
    
    def test_209(self):
        # Unclose String error of string token
        input = """string s <- "This is also an invalid string: \\f 
\\a \\b \\n"
"""
        expect = """This is also an invalid string: \\f """
        self.assertTrue(TestParser.test(input, expect, 209))
    
    def test_210(self):
        # Keyword "var" and "dynamic" declaration
        input = """var x <- 1
var y <- true
var z <- "str"

dynamic x <- 1
dynamic y
dynamic z <- "str"
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test_211(self):
        # Array declaration
        input = """string __s[9312e1202]
number a[5] <- [2, 3, 5, 7, 11]
string sss[4] <- ["PPL", "is", "very", "hard"]
bool abc[4] <- [true, true, false, false]

number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
bool c[2, 2, 3] <- [[[true, true, false], [true, true, false]], [[true, true, false], [true, true, false]]]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_212(self):
        # Declaration with comments
        input = """bool a
## Comment 1
bool b <- true ## Comment 2
######## Comment 3
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test_213(self):
        # Array declaration with initializing non-array expression
        input = """number x[2] <- foo(x)
number y[2] <- x
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_214(self):
        # Invalid array declaration 1: Initialize array with wrong dimensions
        input = """number x[2.3e1] <- [1, 2, 3]
number x[3, 4] <- [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test_215(self):
        # Invalid array declaration 2: Wrong element types
        input = """number arr[4] <- [1, true, 3, "x"]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test_216(self):
        # Invalid array declaration 3: Use var-keyword
        input = """var arr[4] <- [1, 2, 3, 4]
"""
        expect = "Error on line 1 col 7: ["
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test_217(self):
        # Invalid declaration 1: var-keyword without initialization
        input = """var x <- 1
var y
"""
        expect = "Error on line 2 col 5: \n"
        self.assertTrue(TestParser.test(input, expect, 217))
    
    def test_218(self):
        # Invalid declaration 2: wrong type (will not give error now)
        input = """string s <- 123
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_219(self):
        # Invalid declaration 3: wrong token
        input = """number s <= "abc"
"""
        expect = "Error on line 1 col 9: <="
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_220(self):
        # Function declaration
        input = """func main()
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    
    def test_221(self):
        # Function with return statement
        input = """func main() return 1
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    
    def test_222(self):
        # Function with block statement
        input = """func main() begin
end
"""
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "Error on line 7 col 0: func"
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
        expect = "successful"
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
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    
    def test_233(self):
        # Function call expression and sub-expression
        input = """
dynamic a <- foo(213)
dynamic a <- bar(foo("x" + 4.213))
dynamic a <- (foo() + 2) * "adsad"
dynamic a <- -(x + x)*(x-x) ... foo(x, y, z)
"""
        expect = "successful"
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test_235(self):
        # Complex expressions
        input = """
number a <- ((a + b - c) * (d / e)) + ((f % g) - ((h % i) + (j / k) * (l + m) / (n - o))) + (p * q)
number b <- ((a1 + a2) * a3) / (a1 - a2) % (a1 != a2) and (not (a3 < a2) or (a1 <= a3 and (a2 >= a1 or (a3 == a2 and (a1 != a2))))) or (a1 + a2) * (a3 > a2) / (a1 <= a3)
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    
    def test_236(self):
        # Invalid expression 1: Non-associative operators
        # Relational operators (!=) does not have associativity so you have to use parentheses to calculate this expression
        input = """number a <- a3 == a2 and a1 != a2
"""
        expect = "Error on line 1 col 28: !="
        self.assertTrue(TestParser.test(input, expect, 236))
    
    def test_237(self):
        # Invalid expression 2: Wrong array indexing
        input = """bool a <- a[1][2]
"""
        expect = "Error on line 1 col 14: ["
        self.assertTrue(TestParser.test(input, expect, 237))
    
    def test_238(self):
        # Invalid expression 3: Unclosed indexing
        input = """func void()
begin
string x <- a[0 ... "asdas'"da\\f"
end
"""
        expect = "Error on line 3 col 33: \n"
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def test_239(self):
        # Invalid expression 4: Missing operand
        input = """func f()
begin
string x <- 1+----123+/aaajam
end
"""
        expect = "Error on line 3 col 22: /"
        self.assertTrue(TestParser.test(input, expect, 239))
    
    # Statements
    def test_240(self):
        # Scalar variable assignment
        input = """func main() begin
a <- 100
b <- "oifj'"safjms'"fp"
c <- true and true
d <- 0.13E-1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    
    def test_241(self):
        # Index assignment
        input = """func main() begin
l[3] <- value * aPi
foo[x, y, z + 1] <- abc[231.e+9]
rec[rec[rec[rec[rec[rec[rec[rec[rec[rec[rec["infinitely"]]]]]]]]]]] <- "stack"..."overflow"
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    
    def test_242(self):
        # Invalid assignment statement
        input = """func main() begin
f()[0, 1, 2] <- "abc"
end
"""
        expect = "Error on line 2 col 3: ["
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test_243(self):
        # Block statement
        input = """func main() begin
    begin
        number r
        number s
        r <- 2.0
    end
    begin
        
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test_244(self):
        # Nested blocks
        input = """func main() begin
    begin
        number r
        number s <- 3
        r <- 2.0
        begin
            s <- r * r - r
            writeNumber(s)
        end
        writeNumber(s)
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test_245(self):
        # Invalid block statement 1: missing newline
        input = """func main() begin begin
        number r
        number s <- 3
        r <- 2.0
    end
end
"""
        expect = "Error on line 1 col 18: begin"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_246(self):
        # Invalid block statement 2: missing end -> unclosed block
        input = """func main() begin
    begin
        number r
        number s <- 3
        r <- 2.0
end
"""
        expect = "Error on line 7 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 246))
    
    def test_247(self):
        # If statement: 1 line
        input = """func main() begin
    if (a = 1) writeBool(true)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    
    def test_248(self):
        # If statement: block statement
        input = """func main() begin
    if (a = 1)
    
    begin
        bool x <- true
        writeBool(x)
        x <- x ... a + 2
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    
    def test_249(self):
        # If statement: nested if
        input = """func main() begin
    if (a = 1)
        if (b = 1) begin
            string s <- readString()
            writeString(s)
        end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    
    def test_250(self):
        # If-else statement
        input = """func main() begin
    if (PPL_is_easy()) begin
        writeString("u are lying")
    end
    else begin
        writeString("coi SCORM di em")
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    def test_251(self):
        # If-elif-else statement
        input = """number status <- 404

func main()
begin
    string msg
    if (status = 200)
        msg <- "OK"
    elif (status = 400)
        msg <- "Bad Request"
    elif (status = 401) msg <- "Unauthorized"
    elif (status = 404)
        
        msg <- "Not Found"
    elif (status = 500)
        msg <- "Internal Server Error"
    else msg <- "Other messages"
    printString(msg)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_252(self):
        # Mixed if-elif-else statement
        input = """func main() begin
if ("adk\\rasd")
if (sdad)
if (true and false)
foo(1)
elif (adm2 or fs)
foo(2)
else foo(3)
elif (_13kacs)
if (akdsd)
foo(4)
else foo(5)
else foo(6)
elif ("\\''"ashduau23/fik")
foo(7)
else foo(8)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    
    def test_253(self):
        # Invalid if statement 1: else with no if
        input = """func main() begin
if (a = 1) writeBool(true)
else writeBool(false)
else writeBool(invalid)
end
"""
        expect = "Error on line 4 col 0: else"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    def test_254(self):
        # Invalid if statement 2: elif with no if
        input = """func main() begin
if (a = 1) writeBool(true)
else writeBool(false)
elif (false) writeBool(invalid)
end
"""
        expect = "Error on line 4 col 0: elif"
        self.assertTrue(TestParser.test(input, expect, 254))
    
    def test_255(self):
        # For statement
        input = """func main() begin
var i <- 0
for i until i >= 10 by 1
writeNumber(i)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
    
    def test_256(self):
        # For statement: block statement
        input = """func main() begin
number arr[20, 10]
var i <- 0
var j <- 0

for i until i >= 20 by 1
begin
    var tmp_10i <- 10*i
    for j until j >= 10 by 1 begin
        arr[i, j] <- tmp_10i + j
        writeNumber(arr[i, j])
    end
end

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    
    def test_257(self):
        # For statement: nested for
        input = """func main() begin
number arr[20, 10]
var i <- 0
var j <- 0
for i until i >= 20 by 1
    for j until j >= 10 by 1
        arr[i, j] <- readNumber()
writeNumber(i)
writeNumber(j)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def test_258(self):
        # For statement: break statement
        input = """func main() begin
number i <- 1
for i until i = 20 by 1
begin
    writeBool(true)
    if (i = 10) break
end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    
    def test_259(self):
        # For statement: continue statement
        input = """func main() begin
number i <- 20
for i until i = 0 by -1
begin
    if (i >= 10)
        continue
    writeString("less than 10")
end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    
    def test_260(self):
        # Invalid for statement
        input = """func main() begin
for i until i < 10 by i <- i + 1
    writeBool(false)
end
"""
        expect = "Error on line 2 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 260))
    
    def test_261(self):
        # Return statement: return only
        input = """func main() begin
    return
end

func foo(number x) begin
    if (x > 1) return
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    
    def test_262(self):
        # Return statement: return expression 1
        input = """
func pow(number x, number n) begin
    ## Calculate x^n (n >= 0)
    if (n = 0) return 1
    
    var tmp <- pow(x, round(n/2))
    if (n % 2 = 1) return tmp*tmp*x
    return tmp*tmp
end

func round(number n)
begin
    return n - n % 1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    
    def test_263(self):
        # Return statement: return expression 2 (array)
        input = """func main() begin
number x[50] <- createArray(50)
return [1, 2, 3]
end

func createArray(number n)
begin
    if (n > 100) n <- 100
    
    number res[100]
    var i <- 0
    for i until i = n by 1
        res[i] <- 0
    i <- n
    for i until i = 100 by 1
        res[i] <- -1
    return res
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_264(self):
        # Invalid return statement
        input = """func main() begin
return return
end
"""
        expect = "Error on line 2 col 7: return"
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def test_265(self):
        # Function call statement
        input = """func main() begin
    foo()
    pow(2, 3)
    pow(0, 4)
    pow(pow(2, 3), pow(4, 2))
    pow(arr[2, 3], 4 - 2 + 6 * round(7/3))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    
    def test_266(self):
        # Invalid statement 1: statement outside of function 1
        input = """abc <- 100
"""
        expect = "Error on line 1 col 0: abc"
        self.assertTrue(TestParser.test(input, expect, 266))
    
    def test_267(self):
        # Invalid statement 2: statement outside of function 2
        input = """func main() begin
end
if (a = 1) return
"""
        expect = "Error on line 3 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 267))
    
    def test_268(self):
        # Invalid statement 3: function declaration inside function
        input = """func main() begin
func foo() return 1
end
"""
        expect = "Error on line 2 col 0: func"
        self.assertTrue(TestParser.test(input, expect, 268))
    
    def test_269(self):
        # Invalid statement 4: wrong statement for function body (not return or block)
        input = """func main()
for i until i = 1 by 1 return
"""
        expect = "Error on line 2 col 0: for"
        self.assertTrue(TestParser.test(input, expect, 269))
    
    # Mixed Cases
    def test_270(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    
    def test_271(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def test_272(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test_273(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test_274(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    
    def test_275(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test_276(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    def test_277(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test_278(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test_279(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test_280(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    
    def test_281(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    
    def test_282(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    
    def test_283(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test_284(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test_285(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    
    def test_286(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    
    def test_287(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    
    def test_288(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    
    def test_289(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    
    def test_290(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test_291(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_292(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    
    def test_293(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    
    def test_294(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    
    def test_295(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
    
    def test_296(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test_297(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_298(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    
    def test_299(self):
        # 
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
