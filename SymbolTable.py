from collections import defaultdict
class SymbolTable:
    def __init__(self):
        self.table = defaultdict(lambda : None)

    def add_symbol(self, symbol, symbol_type=None):
        self.table[symbol] = {'type': symbol_type}

    def get_table(self):
        return self.table
