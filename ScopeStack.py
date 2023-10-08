class ScopeStack:
    def __init__(self):
        self.stack = ["global"]

    def push(self, scope_name):
        self.stack.append(scope_name)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
