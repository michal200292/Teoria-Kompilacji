import ply.lex as lex

tokens = ('ID', 'INTNUM', 'FLOATNUM', 'STRING',
          'ADD', 'SUB', 'MUL', 'DIV',
          'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
          'ASSIGN', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
          'LESSTHAN', 'GREATERTHAN', 'LESSEQUAL', 'GREATEREQUAL',
          'NOTEQUAL', 'EQUAL', 'RANGE', 'TRANSPOSE', 'IF',
          'ELSE', 'FOR', 'WHILE', 'BREAK', 'CONTINUE', 'RETURN',
          'EYE', 'ZEROS', 'ONES', 'PRINT'
          )

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

literals = ['(', ')', '[', ']', '{', '}', ',', ';']

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ASSIGN = r'='
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_RANGE = r':'
t_TRANSPOSE = r'\''
t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'/'

t_ignore = ' \t'


def t_ID(t):
    r'[_a-zA-Z][_\w]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_FLOATNUM(t):
    r'([-+]?)([0-9]*\.[0-9]+|[0-9]+\.[0-9]*)([eE][-+]?[0-9]+)?'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'".*?"'
    t.value = str(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t):
    print("line %d: illegal character '%s'" % (t.lineno, t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()
