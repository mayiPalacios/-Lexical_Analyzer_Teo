import ply.lex as lex
from SymbolTable import SymbolTable

tokens = (
    'ID',
    'NUMBER',
    'STRING',
    'COMMENT',
    'OP',
    'PAREN_L',
    'PAREN_R',
    'BRACE_L',
    'BRACE_R',
    'SEMICOLON',
    'COMMA',
    'PREPROCESSOR',
    'END_INSTRUCTION',
    'BLOCK_COMMENT'
)

reserved = {
    'cout': 'COUT',
    'namespace': 'NAMESPACE',
    'using': 'USING',
    'auto': 'AUTO',
    'break': 'BREAK',
    'case': 'CASE',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'do': 'DO',
    'else': 'ELSE',
    'for': 'FOR',
    'if': 'IF',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'while': 'WHILE',
    'new': 'NEW'
}

tokens += tuple(reserved.values())

t_OP = r'[+\-*/%=!&|^<>]=?'
t_PAREN_L = r'\('
t_PAREN_R = r'\)'
t_BRACE_L = r'\{'
t_BRACE_R = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_PREPROCESSOR = r'\#\w+'
#t_ASSIGNATION = r'\='
t_END_INSTRUCTION = r'\;'

""" OPs
SUM = r'\+'
LESS = r'-'+
MULTIPLY = r'\*'
DIV = r'/'
EQUAL = r'='
"""

symbol_table = SymbolTable()


def t_ID(t):
    r'\b[A-Za-z_][A-Za-z0-9_]*\b'
    '''t.type = reserved.get(t.value, 'ID')
    if t.type == 'ID':  # Only add user-defined IDs, not reserved words.
        symbol_table.add_symbol(t.value, "Identificador")'''
    return t


def t_NUMBER(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    return t


def t_COMMENT(t):
    r'//.*'
    pass

def t_BLOCK_COMMENT(t):
    r'\/\*(.|\n)*\*\/'
    #return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caracter no contemplado '{t.value[0]}' linea {t.lineno}")
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()


def analyze(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        if reserved.get(tok.value) is not None:
            symbol_table.add_symbol(tok.value, "RESERVED")
        else:
            symbol_table.add_symbol(tok.value, tok.type)
        print(tok.type, tok.value, tok.lineno, tok.lexpos)


def get_symbol_table():
    return symbol_table.get_table()
