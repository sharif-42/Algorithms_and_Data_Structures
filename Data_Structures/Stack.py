# LIFO operation
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty")
            return None
        else:
            self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def stack_print(self):
        print("printing stack elements")
        for i in self.stack:
            print(i)


if __name__ == '__main__':
    stk = Stack()
    stk.pop()
    stk.push(1)
    stk.push(15)
    stk.push(10)
    stk.stack_print()
    stk.pop()
    stk.pop()
    stk.stack_print()
