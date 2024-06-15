# Instruction for PPL Assignments

## Introduction

The `src` folder in this folder contains everything for the 4 assignments.

Some notes:

- You actually only need 1 folder for all 4 assignments. I just want to separate them to mark each period of the assignments.
- I modify the `run.py` file for better output presentation.
- You should read all the initial code provided by your lecturer to know how it works, especially the APIs in the MachineCode.py and Emitter.py of Assignment 4. You will have to modify these 2 files to implement Assignment 4 anyway.
- You should frequently ask questions on forum to resolve ambiguity. It is your rights, so utilize it.
- Do not copy others' code, otherwise you will be punished heavily!
- If you read this, consider giving me a star? Just kidding ^^

## How this project works

To run this project, you need to do the following steps:

1. Download Python 3 and Java
2. Download ANTLR 4.9.2 at [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)
3. Download antlr4-python3-runtime Python package. Type in the terminal `pip install antlr4-python3-runtime==4.9.2`
4. Set environment variable `ANTLR_JAR` to the file antlr-4.9.2-complete.jar in your computer. You should then restart the computer so that the environment variable is in effect.
5. Change the current directory to the `src` folder. There exists a file named `run.py`. These are several CLI commands to run this file:

- `python run.py gen`: Generate the ANTLR files in the `target` directory (same level as `src`, for easy access to submit those files in Assignment 1 + 2).
- `python run.py clean`: Delete those files previously generated in the `target` directory.
- `python run.py gui`: Visualize the parse tree created by ANTLR. You need to replace the content of the files in the `src/test/gui` directory for your input. Don't change the files' name. Note: There are online tools that can visualize ANTLR parse tree now, so you don't need to run this anymore. Use whatever you want.
- `python run.py test LexerSuite`: Test the lexical analysis process with 100 testcases in LexerSuite.
- `python run.py test ParserSuite`: Test the syntax analysis process with 100 testcases in ParserSuite.
- `python run.py test ASTGenSuite`: Test the AST generation with 100 testcases in ASTGenSuite.
- `python run.py test CheckerSuite`: Test the semantics analysis process with 100 testcases in CheckSuite.
- `python run.py test CodeGenSuite`: Test the code generation with 100 testcases in CheckCodeGenSuite.
