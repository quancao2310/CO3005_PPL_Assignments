## To run this project, you need to do the following steps:

1. Download Python 3 and Java
2. Download ANTLR 4.9.2 at [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)
3. Download antlr4-python3-runtime Python package. Type in the terminal **pip install antlr4-python3-runtime==4.9.2**
4. Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer. You should then restart the computer so that the environment variable is in effect.
5. Change the current directory to the /src folder. There exists a file named _run.py_. These are several CLI commands to run this file:

- **python run.py gen**: Generate the ANTLR files in the ../target directory (for easy access to submit those files).
- **python run.py clean**: Delete those files previously generated in the ../target directory.
- **python run.py gui**: Visualize the parse tree created by ANTLR. Note: You need to replace the content of the files in the ./test/gui directory for your input. Don't change the files' name.
- **python run.py test LexerSuite**: Test the lexical analysis process with 100 testcases in LexerSuite.
- **python run.py test ParserSuite**: Test the syntax analysis process with 100 testcases in ParserSuite.
- **python run.py test ASTGenSuite**: Test the AST generation with 100 testcases in ASTGenSuite.
- **python run.py test CheckerSuite**: Test the semantics analysis process with 100 testcases in CheckSuite.
- **python run.py test CodeGenSuite**: Test the Code generation with 100 testcases in CheckCodeGenSuite.
