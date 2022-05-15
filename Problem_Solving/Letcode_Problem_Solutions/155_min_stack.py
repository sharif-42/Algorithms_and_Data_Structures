class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            if x <= self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min = self.min[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == '__main__':
    ms = MinStack()
    ms.push(10)
    print(ms.stack)
    ms.push(11)
    print(ms.stack)
    print(ms.min)
    print(ms.getMin())
    ms.push(-5)
    print(ms.stack)
    print(ms.min)
    print(ms.getMin())
    ms.pop()
    print(ms.stack)

