# FIFO operations

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if len(self.queue) == 0:
            print('Queue is empty so cant pop element')
            return
        self.queue.pop()

    def print_queue(self):
        if len(self.queue) == 0:
            print('Queue is empty')
            return

        print("queue elements are :", end=" ")
        for i in self.queue:
            print(i, end=" ")
        print("")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.print_queue()
    q.enqueue(20)
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.dequeue()
