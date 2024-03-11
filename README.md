# CO3005 - PPL - Assignments
This repository contains the specifications and my implementations of 4 PPL assignments in semester 232. The assignments are about creating a partial compiler for a simple, general-purposed procedural programming language - ZCode. All these assignments are correlated with each other, and each represent a step in implementing the ZCode compiler.

Here is the newest version of ZCode: [Spec](./ZCode_v1.2.2.pdf). The spec is changed over time to resolve ambiguity or any other problems regarding to language/compiler implementation.

## Assignment 1: Lexer/Parser
The first phase of the compilation is lexical analysis. This process is done by a ***Lexer***. It reads the stream of characters of the source code and groups those into meaningful sequences called ***lexemes***. It also removes extraneous whitespace and comments. After this process, all the characters becomes a token stream.

The second phase is syntax analysis. It uses the token stream to create a ***syntax tree (parse tree)*** that depicts the grammatical structure of the tokens. This process is done by a ***Parser***. It assures that the combination and order of tokens follow the grammar rules of the language.

This first assignment use a tool called ***[ANTLR](https://www.antlr.org/)*** (ANother Tool for Language Recognition). It provides a mechanism to generate a lexer and parser easily and comprehensively. You can use regular expressions, actions, commands... to write lexicon and grammar rules. More details can be found in this [documentation](https://github.com/antlr/antlr4/blob/master/doc/index.md) and other Internet resources.

## Assignment 2: AST Generation
From the parse tree which contains many unnecessary nodes (created from grammar rules defined in ANTLR), a new data structure is created called the ***Abstract Syntax Tree (AST)***. This tree represents the abstract syntax structure of the source code and help subsequence phases not to depend on parsing process anymore.

In order to traverse the parse tree to generate the AST, the ***Visitor*** design pattern is used. It allows an object called the Visitor to visit all parse tree nodes and create the corresponding AST nodes. ANTLR provides a Visitor interface that contains a visiting method for each grammar rule. You can thus implement this interface to do whatever you need (in this case generating the AST).

## Assignment 3

## Assignment 4
