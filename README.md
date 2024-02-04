# CO3005 - PPL - Assignments
This repository contains the specifications and my implementations of 4 PPL assignments in semester 232. The assignments are about creating a partial compiler for a simple, general-purposed procedural programming language - ZCode. All these assignments are correlated with each other, and each represent a step in implementing the ZCode compiler.

Here is the newest version of ZCode: [Spec](./ZCode_v1.2.2.pdf). The spec is changed over time to resolve ambiguity or any other problems regarding to language/compiler implementation.

## Assignment 1: Lexer/Parser
The first phase of the compilation is lexical analysis. This process is done by a **Lexer**. It reads the stream of characters of the source code and groups those into meaningful sequences called **lexemes**. It also removes extraneous whitespace and comments. After this process, all the characters becomes a token stream.

The second phase is syntax analysis. It uses the token stream to create a syntax tree that depicts the grammatical structure of the tokens. This process is done by a **Parser**. It assures that the combination and order of tokens follow the grammar rules of the language.

This first assignment use a tool called [ANTLR](https://www.antlr.org/) (ANother Tool for Language Recognition). It provides a mechanism for powerfully generating a lexer and parser in an easy and comprehensive way. You can use regular expressions, actions, commands... to write lexicon and grammar rules. More details can be found in this [documentation](https://github.com/antlr/antlr4/blob/master/doc/index.md) and other Internet resources.

## Assignment 2

## Assignment 3

## Assignment 4
