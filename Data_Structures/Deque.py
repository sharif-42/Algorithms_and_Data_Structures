class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, value):
        self.items.append(value)

    def add_back(self, value):
        self.items.insert(0, value)

    def pop_front(self):
        if len(self.items) == 0:
            return "Deque is Empty"
        return self.items.pop()

    def pop_back(self):
        if len(self.items) == 0:
            return "Deque is Empty"
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    print(d.pop_back())
    d.add_front(10)
    print(d.items)
    d.add_front(20)
    print(d.items)
    d.add_back(30)
    d.add_back(40)
    d.add_back(50)
    print(d.items)
    print(d.is_empty())
    print(d.size())
    print(d.pop_back())
    print(d.pop_front())
    print(d.items)
