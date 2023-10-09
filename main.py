from lexer import analyze, get_symbol_table
from tkinter import Tk
from tkinter.filedialog import askopenfilename


if __name__ == "__main__":
    Tk().withdraw()
    filename = askopenfilename()
    f = open(filename, 'r')
    code = f.read()
    analyze(code)
    symbols = get_symbol_table()
