class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node


class LinkedList:
    def __init__(self):
        # head None means Linked list is empty
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    # Add a node at the front
    # head is alway points the first element
    def insert_at_the_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    # This function is defined in Linked List class
    # Appends a new node at the end.  This method is
    #  defined inside LinkedList class shown above */
    def insert_at_the_end(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next_node

        # 6. Change the next of last node
        last.next_node = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next_node


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_the_front(10)
    lst.insert_at_the_front(20)
    lst.insert_at_the_front(50)
    print(lst.size)
    lst.printList()
