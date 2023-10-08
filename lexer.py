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
    'new': 'NEW',
    'int': 'INT',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
}

tokens += tuple(reserved.values())

t_OP = r'[+\-*/%=!&|^<>]=?'
t_BRACE_L = r'\{'
t_BRACE_R = r'\}'
t_PREPROCESSOR = r'\#\w+'
t_END_INSTRUCTION = r'\;'

""" OPs
SUM = r'\+'
LESS = r'-'+
MULTIPLY = r'\*'
DIV = r'/'
EQUAL = r'='
"""

symbol_table = SymbolTable()
is_declaring = False
var_type = None
var_name = None
scope_tracking = 0


def t_ID(t):
    r'\b[A-Za-z_][A-Za-z0-9_]*\b'
    t.type = reserved.get(t.value, 'ID')
    global is_declaring
    global var_type
    global var_name
    if t.type in ['INT', 'FLOAT', 'DOUBLE', 'CHAR']:
        is_declaring = True
        var_type = t.type
    elif is_declaring and t.type == 'ID':
        var_name = t.value
    return t


def t_SEMICOLON(t):
    r';'
    global is_declaring
    global var_type
    global var_name
    if is_declaring and var_name:
        symbol_table.add_symbol(var_name, var_type, "Sin asignación", scope_tracking)
        is_declaring = False
    return t


def t_COMMA(t):
    r','
    global is_declaring
    global var_type
    global var_name
    if is_declaring and var_name:
        symbol_table.add_symbol(var_name, var_type, "Sin asignación", scope_tracking)
        is_declaring = False
    return t


def t_PAREN_R(t):
    r'\)'
    global is_declaring
    global var_type
    global var_name
    if is_declaring and var_name:
        symbol_table.add_symbol(var_name, var_type, "Sin asignación", scope_tracking)
        is_declaring = False
    return t


def t_PAREN_L(t):
    r'\('
    global is_declaring
    is_declaring = False
    return t


def t_NUMBER(t):
    r'\b\d+\b'
    global is_declaring
    global var_type
    global var_name
    if is_declaring and var_name:
        t.value = int(t.value)
        symbol_table.add_symbol(var_name, var_type, t.value, scope_tracking)
        is_declaring = False
    return t


def t_STRING(t):
    r'"[^"]*"'
    global is_declaring
    global var_type
    global var_name
    if is_declaring and var_name:
        symbol_table.add_symbol(var_name, f"Variable: {var_type} with value {t.value}")
        is_declaring = False
    return t


def t_COMMENT(t):
    r'//.*'
    pass


def t_BLOCK_COMMENT(t):
    r'\/\*(.|\n)*\*\/'
    # return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    #print(f"Caracter no contemplado '{t.value[0]}' linea {t.lineno}")
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()


def analyze(data):
    global is_declaring
    global var_type
    global scope_tracking
    global var_name
    count_iterations = 0
    lexer.prev_token_type = None
    is_declaring = False
    var_type = None
    var_name = None
    lexer.input(data)
    print("+------------------ Lista de elementos lexicográficos -------------------+")
    print("+----------------------+-----------------+-----------------+-------------+")
    print("| Type                 | Value           | Line            | Locatio     |")
    print("+----------------------+-----------------+-----------------+-------------+")
    while True:
        tok = lexer.token()
        if not tok:
            break
        count_iterations += 1
        if not is_declaring:
            count_iterations = 0
        if count_iterations == 4 and is_declaring:
            is_declaring = False
            count_iterations = 0
        lexer.prev_token_type = tok.type

        print(f"| {tok.type:20} | {tok.value:15} | {tok.lineno:15} | {tok.lexpos:11} |")


        if tok.value == "{":
            scope_tracking += 1
        elif tok.value == "}":
            scope_tracking -= 1
    print("+----------------------+-----------------+-----------------+-------------+", "\n")

def get_symbol_table():
    return symbol_table.print_table()
