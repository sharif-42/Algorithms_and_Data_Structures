class Deque:
    def __init__(self, item):
        self.items = list(item)

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

    def check_paliondrome(self):
        Flag = True
        while not self.is_empty():
            if len(self.items) == 1:
                return Flag
            front = self.pop_front()
            back = self.pop_back()
            if not front == back:
                Flag = False
                break

        return Flag


if __name__ == '__main__':
    d = Deque(input())
    print(d.check_paliondrome())
