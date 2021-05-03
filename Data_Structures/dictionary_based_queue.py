from collections import OrderedDict


class Queue:
    def __init__(self, initial_data=None, **kwargs):
        self.data = OrderedDict()
        if initial_data:
            self.data.update(initial_data)
        if kwargs:
            self.data.update(kwargs)

    def enqueue(self, item):
        key, value = item
        if key in self.data.keys():
            self.data.move_to_end(key)
        else:
            self.data[key] = value

    def dequeue(self):
        try:
            self.data.popitem(last=False)
        except KeyError:
            print("Queue is Empty!")

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"Queue({self.data.items()})"


if __name__ == '__main__':
    q = Queue(a=1, b=2, c=3)
    q.dequeue()
    print(q)

    q.enqueue(('one', 1))
    print(q.data)

    q1 = Queue(initial_data=q.data)
    print(q1.data)
    q1.enqueue(('Two', 1))
    print(q1.data)

    q1.dequeue()
    print(q1.data)
