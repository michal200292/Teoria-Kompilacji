from src import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'IF'),
    ('nonassoc', 'ELSE'),
    # ('right', 'MULASSIGN', 'DIVASSIGN', 'SUBASSIGN', 'ADDASSIGN'),
    ('nonassoc', 'LESSTHAN', 'GREATERTHAN', 'GREATEREQUAL', 'LESSEQUAL', 'EQUAL', 'NOTEQUAL'),
    ('left', 'ADD', 'SUB'),
    ('left', 'DOTADD', 'DOTSUB'),
    ('left', 'MUL', 'DIV'),
    ('left', 'DOTMUL', 'DOTDIV'),
    ('left', 'TRANSPOSE'),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program_instructions(p):  # !#!#!#! moze na @odwrut
    """program : instruction program
               | instruction"""


def p_instruction(p):
    """instruction : instruction_while
                        | instruction_for
                        | instruction_if
                        | instruction_print ";"
                        | instruction_return ";"
                        | instruction_assign ";"
                        | BREAK ";"
                        | CONTINUE ";" """


def p_braces(p):
    """instruction : "{" program "}" """


def p_instruction_while(p):
    """ instruction_while : WHILE "(" expression ")" instruction"""


def p_instruction_for(p):
    """instruction_for : FOR ID ASSIGN expression RANGE expression instruction"""


# def p_break(p):
#     """break : BREAK"""
#
#
# def p_continue(p):
#     """continue : CONTINUE"""


def p_instruction_if(p):  # !!!!
    """ instruction_if : IF "(" expression ")" instruction
                       | IF "(" expression ")" instruction ELSE instruction"""


def p_instruction_print(p):
    """ instruction_print : PRINT printables"""


def p_printables(p):
    """ printables : printable
                   | printable "," printables"""


def p_printable(p):
    """ printable : expression"""


def p_instruction_return(p):
    """ instruction_return : RETURN
                           | RETURN expression"""


def p_instruction_assign(p):
    """ instruction_assign : assignable ASSIGN expression
                           | assignable ADDASSIGN expression
                           | assignable SUBASSIGN expression
                           | assignable MULASSIGN expression
                           | assignable DIVASSIGN expression"""


def p_assignable(p):
    """ assignable : ID
                   | matrix_element
                   | vector_element"""


def p_expression_trans(p):
    """expression : expression TRANSPOSE"""


def p_expression_nested(p):
    """expression : "(" expression ")" """


def p_expression_create_matrix(p):
    """expression : create_matrix "(" expression ")" """


def p_expression_minus(p):  # !!!!!
    """expression : SUB expression"""


def p_expression_literal(p):
    """expression : assignable
                  | matrix"""


def p_expression_intnum(p):
    """expression : INTNUM"""


def p_expression_floatnum(p):
    """expression : FLOATNUM"""


def p_expression_string(p):
    """expression : STRING"""


def p_binary_expression(p):
    """expression : expression ADD expression
            | expression SUB expression
            | expression MUL expression
            | expression DIV expression
            | expression DOTADD expression
            | expression DOTSUB expression
            | expression DOTMUL expression
            | expression DOTDIV expression
            | expression GREATERTHAN expression
            | expression LESSTHAN expression
            | expression EQUAL expression
            | expression NOTEQUAL expression
            | expression LESSEQUAL expression
            | expression GREATEREQUAL expression
            """


def p_matrix(p):
    """ matrix : "[" vectors "]" """


def p_create_matrix(p):
    """ create_matrix : ZEROS
                      | ONES
                      | EYE"""


def p_matrix_element(p):
    """ matrix_element : ID "[" INTNUM "," INTNUM "]" """


def p_vectors(p):  # !!!
    """vectors : vector "," vectors
               | vector """


def p_vector(p):
    """vector : "[" variables "]" """


def p_vector_element(p):
    """ vector_element : ID "[" expression "]" """


def p_variables(p):
    """variables : expression "," variables
                 | expression """


# def p_variable(p):
#     """variable : INTNUM
#                 | FLOATNUM
#                 | assignable """


# def p_identifier(p):
#     """identifier : ID "[" expression_vector "]"
#                   | ID"""
#
#
# def p_statement_expression(p):
#     """statement : expression"""
#
#
# def p_expression_create_matrix(p):
#     """expression : EYE "(" expression ")"
#                   | ZEROS "(" expression ")"
#                   | ONES "(" expression ")" """
#
#
# def p_expression_initialize_matrix(p):
#     """expression : "[" expression_vector "]"
#                   | "[" expression_vector "]" "," expression
#                   | expression_vector"""
#
#
# def p_expression_vector_expression(p):
#     """expression_vector : expression_vector "," expression
#                          | expression"""
#
#
# def p_expression_bin_operation(p):
#     """expression : expression ADD expression
#                   | expression SUB expression
#                   | expression MUL expression
#                   | expression DIV expression"""
#
#
# def p_expression_minus(p):
#     """expression : SUB INTNUM
#                   | SUB ID
#                   | SUB FLOATNUM"""
#
#
# def p_expression_intnum(p):
#     """expression : INTNUM"""
#
#
# def p_expression_floatnum(p):
#     """expression : FLOATNUM"""
#
#
# def p_expression_identifier(p):
#     """expression : ID TRANSPOSE
#                   | identifier"""


# def p_program(p):
#     """program : instructions_opt"""
#
#
# def p_instructions_opt_1(p):
#     """instructions_opt : instructions """
#
#
# def p_instructions_opt_2(p):
#     """instructions_opt : """
#
#
# def p_instructions_1(p):
#     """instructions : instructions instruction """
#
#
# def p_instructions_2(p):
#     """instructions : instruction """


# to finish the grammar
# ....

parser = yacc.yacc()
