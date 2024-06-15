# CO3005 - PPL - Assignments

This repository contains the specifications and my implementations of 4 PPL assignments in semester 232. The assignments are about creating a partial compiler for a simple, general-purposed procedural programming language - ZCode. All these assignments are correlated with each other, and each represent a step in implementing the ZCode compiler.

Here is the newest version of ZCode: [Spec](./ZCode_v1.2.2.pdf). The spec is changed over time to resolve ambiguity or any other problems regarding to language/compiler implementation.

> [!NOTE]
> For more information on how to run the project, please refer to the README inside `BTL4/assignment4-initial` folder.

## Assignment 1: Lexer/Parser

The first phase of the compilation is lexical analysis. This process is done by a **_Lexer_**. It reads the stream of characters of the source code and groups those into meaningful sequences called **_lexemes_**. It also removes extraneous whitespace and comments. After this process, all the characters becomes a token stream.

The second phase is syntax analysis. It uses the token stream to create a **_syntax tree (parse tree)_** that depicts the grammatical structure of the tokens. This process is done by a **_Parser_**. It assures that the combination and order of tokens follow the grammar rules of the language.

This first assignment use a tool called **_[ANTLR](https://www.antlr.org/)_** (ANother Tool for Language Recognition). It provides a mechanism to generate a lexer and parser easily and comprehensively. You can use regular expressions, actions, commands... to write lexicon and grammar rules. More details can be found in this [documentation](https://github.com/antlr/antlr4/blob/master/doc/index.md) and other Internet resources.

## Assignment 2: AST Generation

From the parse tree which contains many unnecessary nodes (created from grammar rules defined in ANTLR), a new data structure is created called the **_Abstract Syntax Tree (AST)_**. This tree represents the abstract syntax structure of the source code and help subsequence phases not to depend on parsing process anymore.

In order to traverse the parse tree to generate the AST, the **_Visitor_** design pattern is used. It allows an object called the Visitor to visit all parse tree nodes and create the corresponding AST nodes. ANTLR provides a Visitor interface that contains a visiting method for each grammar rule. You can thus implement this interface to do whatever you need (in this case generating the AST).

## Assignment 3: Semantic Analysis (Static Checking)

The AST can then be translated to machine code and run. However, there may be some potential errors in the program. Therefore, the compiler performs another check in the AST without executing the code. This process is called **_Semantic Analysis_**. In this process, some aspects need to be checked such as scope constraint, type constraint, the semantics of statements, functions, OOP...

There are many ways to check the AST for those constraints. In this assignment, the Visitor pattern is reused for its simplicity and familiarity. You also have to organize and store your scopes and types of the program variables/functions/classes in order to check them later.

## Assignment 4: Code Generation

After checking for some potential errors, the source code is then translated into some code that the machines can execute. It can be the machine code, or an (or some) intermediate representation which is then translated into target machine code by another machine.

The intermediate code should be easier to be produced and translated into the target machine code. For this assignment, the chosen intermediate representation is **_Java bytecode_**, and the machine that can later process it is **_Java virtual machine (JVM)_**.

Our task is to translate the AST into **_Jasmin code_**, an assembly-like syntax of Java bytecode. The Jasmin code is then translated into Java bytecode by a Jasmin assembler, and then processed by JVM.

The Visitor is also reused, but now you are also provided with some APIs by your lecturers. These APIs help you write your intermediate code generator faster. You must understand these APIs, and how Jasmin/Java bytecode works in order to produce the right code for JVM.
