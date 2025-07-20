import ply.lex as lex

tokens = [
    'ID',
    'INTEGER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',
    'EQUALS_EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'GREATER_THAN',
    'LBRACKET',
    'RBRACKET',
    'DOT',
    'AMPERSAND',
    'PLUS_EQUALS', 'MINUS_EQUALS', 'TIMES_EQUALS', 'DIVIDE_EQUALS',
    'BIT_OR', 'LEFT_SHIFT',
    'QUESTION', 'COLON',
    'PLUS_PLUS', 'MINUS_MINUS',
    'MODULO', 'LESS_EQUALS', 'GREATER_EQUALS',
    'LOGICAL_AND', 'LOGICAL_OR', 'LOGICAL_NOT',
]

reserved = {
    'int': 'INT',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
    'printf': 'PRINTF',
    'for': 'FOR',
    'struct': 'STRUCT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'scanf': 'SCANF',
    'do': 'DO',
}

tokens += list(reserved.values())

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_ASSIGN    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COMMA     = r','
t_EQUALS_EQUALS = r'=='
t_NOT_EQUALS    = r'!='
t_LESS_THAN     = r'<'
t_GREATER_THAN  = r'>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'
t_AMPERSAND = r'\&'
t_PLUS_EQUALS   = r'\+='  
t_MINUS_EQUALS  = r'-='  
t_TIMES_EQUALS  = r'\*='  
t_DIVIDE_EQUALS = r'/=' 
t_BIT_OR      = r'\|'
t_LEFT_SHIFT  = r'<<'
t_QUESTION = r'\?'
t_COLON    = r':'
t_PLUS_PLUS   = r'\+\+'
t_MINUS_MINUS = r'--'
t_MODULO          = r'%'
t_LESS_EQUALS     = r'<='
t_GREATER_EQUALS  = r'>='
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR  = r'\|\|'
t_LOGICAL_NOT = r'!'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r"'[a-zA-Z]'"
    t.value = t.value[1]
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = str(t.value[1:-1])
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal encontrado: '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

def t_COMMENT(t):
    r'//.*'
    pass

def t_BLOCK_COMMENT(t):
    r'/\*[\s\S]*?\*/'
    pass

lexer = lex.lex()