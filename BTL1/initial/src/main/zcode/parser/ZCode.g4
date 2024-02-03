grammar ZCode;
// Cao Minh Quan - 2112109

@lexer::header {
# Cao Minh Quan - 2112109
from lexererr import *
}

options {
  language=Python3;
}

// ********************GRAMMAR********************
program: nullable_newline_list decl_list EOF;

// --------------------DECLARATIONS--------------------
decl_list: decl decl_list
         | decl
         ;

decl: variable_decl
    | function_decl
    ;

// Variables
variable_decl: primitive_decl
             | var_keyword_decl
             | dynamic_keyword_decl
             | array_decl
             ;

primitive_decl: primitive_type IDENTIFIER optional_init nonempty_newline_list;
var_keyword_decl: VAR IDENTIFIER ASSIGN expression nonempty_newline_list;
dynamic_keyword_decl: DYNAMIC IDENTIFIER optional_init nonempty_newline_list;
optional_init: ASSIGN expression | ;

array_decl: primitive_type IDENTIFIER array_dimensions optional_array_init nonempty_newline_list;
array_dimensions: LEFT_SQUARE_BRACKET dimension_list RIGHT_SQUARE_BRACKET;
dimension_list: NUMBER_LIT COMMA dimension_list
              | NUMBER_LIT
              ;
optional_array_init: ASSIGN array_lit | ;

// Functions
function_decl: FUNC IDENTIFIER param_decl optional_impl nonempty_newline_list;
param_decl: LEFT_PAREN param_list RIGHT_PAREN;
param_list: param_list_prime | ;
param_list_prime: param COMMA param_list_prime
                | param
                ;
param: primitive_type IDENTIFIER
     | primitive_type IDENTIFIER array_dimensions
     ;
optional_impl: nullable_newline_list body | ;
body: return_stmt
    | block_stmt
    ;

// --------------------STATEMENTS--------------------
statement: variable_stmt
         | assignment_stmt
         | if_stmt
         | for_stmt
         | break_stmt
         | continue_stmt
         | return_stmt nonempty_newline_list
         | call_stmt
         | block_stmt nonempty_newline_list
         ;

// Variable statement
variable_stmt: variable_decl;

// Assignment statement
assignment_stmt: lhs_asmt ASSIGN expression nonempty_newline_list;
lhs_asmt: IDENTIFIER
        | IDENTIFIER LEFT_SQUARE_BRACKET expr_list RIGHT_SQUARE_BRACKET
        ;

// If statement
if_stmt: IF LEFT_PAREN expression RIGHT_PAREN nullable_newline_list statement elif_list else_stmt;
elif_stmt: ELIF LEFT_PAREN expression RIGHT_PAREN nullable_newline_list statement;
elif_list: elif_stmt elif_list
         | 
         ;
else_stmt: ELSE statement | ;

// For statement
for_stmt: FOR IDENTIFIER UNTIL expression BY expression nullable_newline_list statement;

// Break statement
break_stmt: BREAK nonempty_newline_list;

// Continue statement
continue_stmt: CONTINUE nonempty_newline_list;

// Return statement
return_stmt: RETURN return_value;
return_value: expression | ;

// Function call statement
call_stmt: call_expr nonempty_newline_list;

// Block statement
block_stmt: BEGIN nonempty_newline_list stmt_list END;
stmt_list: statement stmt_list
         | 
         ;

// --------------------EXPRESSIONS--------------------
expression: expr1 CONCAT expr1
          | expr1
          ;
expr1: expr2 rel_op expr2
     | expr2
     ;
expr2: expr2 (AND | OR) expr3
     | expr3
     ;
expr3: expr3 (ADD | SUB) expr4
     | expr4
     ;
expr4: expr4 (MUL | DIV | MOD) expr5
     | expr5
     ;
expr5: NOT expr5
     | expr6
     ;
expr6: SUB expr6
     | expr7
     ;
expr7: index_expr
     | operand
     ;

operand: NUMBER_LIT
       | STRING_LIT
       | boolean_lit
       | array_lit
       | call_expr
       | IDENTIFIER
       | LEFT_PAREN expression RIGHT_PAREN
       ;

boolean_lit: TRUE | FALSE;
array_lit: LEFT_SQUARE_BRACKET expr_list RIGHT_SQUARE_BRACKET;

// Function call
call_expr: IDENTIFIER LEFT_PAREN argument_list RIGHT_PAREN;
argument_list: expr_list | ;

// Indexing expression
index_expr: expr_for_indexing LEFT_SQUARE_BRACKET expr_list RIGHT_SQUARE_BRACKET;
expr_for_indexing: IDENTIFIER
                 | call_expr
                 ;

// --------------------COMMONLY USED/GROUPING GRAMMAR RULES--------------------
primitive_type: NUMBER | BOOL | STRING;
rel_op: EQ | STRING_EQ | NEQ | LT | GT | LTE | GTE;

expr_list: expression COMMA expr_list
         | expression
         ;

// This rule is used to end a statement or declaration
// as one must end with at least one \n
nonempty_newline_list: NEWLINE nonempty_newline_list // At least 1 \n
                     | NEWLINE
                     ;

// Some statements/declarations allow \n but not compulsory
// such as function body, if-statement, for-statement
nullable_newline_list: NEWLINE nullable_newline_list // At least 0 \n
                     | 
                     ;

// ********************LEXICON********************
// --------------------KEYWORDS--------------------
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

// --------------------OPERATORS--------------------
ASSIGN: '<-';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NOT: 'not';
AND: 'and';
OR: 'or';

EQ: '=';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

CONCAT: '...';
STRING_EQ: '==';

// --------------------SEPARATORS--------------------
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';
COMMA: ',';
NEWLINE: '\r'? '\n' {self.text = '\n'};

// --------------------LITERALS--------------------
NUMBER_LIT: INT DEC? EXP?;
fragment INT: [0-9]+;
fragment DEC: '.' [0-9]*;
fragment EXP: [eE] [+-]? [0-9]+;

STRING_LIT: '"' VALID_CHAR* '"' {self.text = self.text[1:-1]};
fragment ESC_CHAR: '\\' [bfrnt'\\];
fragment INVALID_ESC_CHAR: '\\' ~[bfrnt'\\];
fragment VALID_CHAR: ESC_CHAR | '\'"' | ~["\r\n\\];

// --------------------COMMENTS--------------------
COMMENT: '##' ~[\n]* -> skip;

// --------------------IDENTIFIERS--------------------
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

// --------------------WHITESPACE--------------------
WS: [ \b\t\f]+ -> skip;

// Error tokens
UNCLOSE_STRING: '"' VALID_CHAR* ([\r\n] | EOF) {
if self.text[-1] in ['\r', '\n']:
    raise UncloseString(self.text[1:-1])
else:
    raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' VALID_CHAR* INVALID_ESC_CHAR {
raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: . {
raise ErrorToken(self.text)
};