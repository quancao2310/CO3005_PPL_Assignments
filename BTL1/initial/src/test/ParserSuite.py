import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
    * 200-204: Types
    * 205-229: Declarations
    * 230-239: Expressions
    * 240-269: Statements
    * 270-299: Solve algorithms/problems in ZCode
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
    
    # Solve algorithms/problems in ZCode
    def test_270(self):
        # Find sum of array
        input = """func sum(number a[100], number length)
begin
    var i <- 0
    var sum <- 0
    for i until i >= length by 1
        sum <- sum + a[i]
    return sum
end

func main() begin
    writeNumber(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    writeNumber(sum([2, 0, 2, 4], 4))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    
    def test_271(self):
        # Print array - Iterative approach
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def test_272(self):
        # Print array - Recursive approach
        input = """func printArr(number a[100], number length)
begin
    if (length < 0)
        return
    printArr(a, length - 1)
    writeNumber(a[length - 1])
    writeString(" ")
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test_273(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
    
    def test_274(self):
        # Find minimum in array
        input = """func min(number a[100], number length)
begin
    if (length <= 0)
        return 1E+9 ## Represent possitive infinity
    var min <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] < min) min <- a[i]
    return min
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    
    def test_275(self):
        # Decimal to binary representation
        input = """func round(number n)

func dec_to_bin(number n) begin
    if (n < 0) return "not implemented"
    if (n = 0) return "0"
    
    var res <- ""
    var i <- 0
    for i until n <= 0 by 0 begin
        if (n % 2 == 0) res <- "0" ... res
        else res <- "1" ... res
        n <- round(n/2)
    end
    
    return res
end

func round(number n) return n - n % 1

func main() begin
    writeNumber(dec_to_bin(10))
    writeNumber(dec_to_bin(100))
    writeNumber(dec_to_bin(1000))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test_276(self):
        # Greatest Common Divisor (GCD)
        input = """func gcd(number a, number b)
begin
    if (b = 0) return a
    return gcd(b, a % b)
end

func main() begin
    writeNumber(gcd(6, 9))
    writeNumber(gcd(24, 16))
    writeNumber(gcd(1, 7))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    def test_277(self):
        # Palindrome string
        input = """func isPalindrome(string s[100], number left, number right)
begin
    ## Because ZCode string cannot be indexed, cut, etc...
    ## We assume that s is an array of 1-length strings, aka characters
    ## And we will check whether characters from left to right (inclusively) can make a palindrome string
    
    if (left > right + 1) return false
    if ((left = right) or (left = right + 1)) return true
    return (s[left] == s[right]) and isPalindrome(s, left + 1, right - 1)
end

func main()
begin
    isPalindrome(["m", "o", "m"], 0, 2)
    isPalindrome(["d", "o", "g", "e", "e", "s", "e", "s", "e", "e", "g", "o", "d"], 0, 12)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test_278(self):
        # Fibonacci sequence
        input = """number res[100]

func fib(number n)
begin
    if (res[n] != -1) return res[n]
    res[n] <- fib(n - 1) + fib(n - 2)
    return res[n]
end

func main() begin
    res[0] <- 0
    res[1] <- 1
    
    var i <- 2
    for i until i = 100 by 1 res[i] <- -1
    
    writeNumber(fib(5))
    writeNumber(fib(10))
    writeNumber(fib(50))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test_279(self):
        # Check whether one number is divisible the other (Example 1 in spec)
        input = """func areDivisors(number num1, number num2)
    return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
    end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test_280(self):
        # Check prime number (Example 2 in spec)
        input = """func isPrime(number x)

func main()
    begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
    end

func isPrime(number x)
    begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        return true
    end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    
    def test_281(self):
        # Tower of Hanoi
        input = """func print(string src, string dst, string aux)

func tower_of_hanoi(number n, string src, string dst, string aux)
begin
    if (n = 1) print(src, dst)
    else begin
        tower_of_hanoi(n - 1, src, aux, dst)
        tower_of_hanoi(1, src, dst, aux)
        tower_of_hanoi(n - 1, aux, dst, src)
    end
end

func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    output <- output ... "\\n"
    writeString(output)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    
    def test_282(self):
        # N-queens problem
        # Print one solution of N-queens problem
        input = """func printSolution(number board[100, 100], number n)
begin
    var i <- 0
    var j <- 0
	for i until i >= n by 1 begin
		for j until j >= n by 1
            if (board[i, j]) writeString("Q ")
		    else writeString(". ")
		printf("\\n")
	end
end

func isSafe(number board[100, 100], number n, number row, number col) begin
	var i <- 0
    var j <- 0
	for i until i >= col by 1
		if (board[row, i])
			return false
    
    i <- row
    j <- col
	for i until ((i < 0) or (j < 0)) by -1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
    
    i <- row
    j <- col
	for i until ((i >= n) or (j < 0)) by 1 begin
		if (board[i, j])
			return false
        j <- j - 1
    end
	
    return true
end

func solverec(number board[100, 100], number col, number n) begin
    if (col >= n) return true
    
    var i <- 0
    for i until i >= n by 1 begin
		if (isSafe(board, n, i, col)) begin
			board[i, col] <- 1
			if (solverec(board, col + 1, n)) return true
			board[i, col] <- 0
		end
	end
	
    return false
end

func solve(number n)
begin
    number board[100, 100]
    var i <- 0
    var j <- 0
    for i until i >= n by 1
        for j until j >= n by 1
            board[i, j] <- 0
    
    if (not solverec(board, 0, n)) writeString("No solution")
    else printSolution(board, n)
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))
    
    def test_283(self):
        # Knight's tour problem
        input = """number sol[10, 10]
number xMove[8] <- [ 2, 1, -1, -2, -2, -1,  1,  2 ]
number yMove[8] <- [ 1, 2,  2,  1, -1, -2, -2, -1 ]

func chkCell(number x, number y, number n)
    return (x >= 0) and (x < n) and (y >= 0) and (y < n) and (sol[x, y] == -1)

func solverec(number x, number y, number move_ith, number n) begin
    if (move_ith == n*n) return true
    number k <- 0
    number xNext
    number yNext
    for k until k = 8 by 1 begin
        xNext <- x + xMove[k]
        yNext <- y + yMove[k]
        if (chkCell(xNext, yNext, n)) begin
            sol[xNext, yNext] <- move_ith
            move_ith <- move_ith + 1
            if (solverec(xNext, yNext, move_ith, n)) return true
            move_ith <- move_ith - 1
            sol[xNext, yNext] <- -1
        end
    end
    return false
end

func solve(number n) begin
    var i <- 0
    var j <- 0
    for i until i >= n by 1
        for j until j >= n by 1
            sol[i, j] <- -1
    sol[0, 0] <- 0
    
    return solverec(0, 0, 1, n) = 1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    
    def test_284(self):
        # Linear search
        input = """func find(number arr[100], number length, number element)
begin
    var i <- 0
    for i until i >= length by 1
        if (arr[i] = element) return i
    return -1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test_285(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    
    def test_286(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    
    def test_287(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
    
    def test_288(self):
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

func swap(number arr[100], number i, number j) begin
    var tmp <- arr[i]
    arr[i] <- arr[j]
    arr[j] <- tmp
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
    
    def test_289(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    
    def test_290(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test_291(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_292(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    
    def test_293(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    
    def test_294(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    
    def test_295(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))
    
    def test_296(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test_297(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_298(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    
    def test_299(self):
        # Longest Common Subsequence (LCS)
        # Print the length of the longest common subsequence of array (or strings)
        input = """func lcs(number arr1[100], number arr2[100], number m, number n) begin
    if ((m = 0) or (n = 0)) return 0
    if (arr1[m - 1] = arr2[n - 1]) return 1 + lcs(arr1, arr2, m - 1, n - 1)
    return max(lcs(arr1, arr2, m - 1, n), lcs(arr1, arr2, m, n - 1))
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))
