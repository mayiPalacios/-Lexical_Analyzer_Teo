import re
import ply.lex as lex


#token declaration
Digit = r'[0-9]'
Letters = r'[a-zA-Z]'

#Logical operators
SUM = r'\+'
LESS = r'-'
MULTIPLY = r'\*'
DIV = r'/'
EQUAL = r'='

#reserved_words = r'\b(cout|namespace|using)\b'

reserved_words = {
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

sample_text = """
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, world!" << endl;
    return 0;
}
"""


results = re.findall(reserved_words, sample_text)

for word in results:
    print("Reserved word found:", word)