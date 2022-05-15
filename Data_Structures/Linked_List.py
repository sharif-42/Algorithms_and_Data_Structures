# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        """
        Always Keeping the head at the beginning.
        :param new_data: data element to be add
        :return:
        """
        new_node = Node(data=new_data)
        new_node.next = self.head

        self.head = new_node

    def print_linked_list(self):
        print("Element in Linked List")
        temp_head = self.head
        while temp_head:
            print(str(temp_head.data) + " ", end="")
            temp_head = temp_head.next
        print()

    def insert_at_the_end(self, new_data):
        new_node = Node(data=new_data)
        while self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node, new_data):
        """
        A data will be added after a specific node
        :param prev_node: Previous node, after that new node will be added
        :param new_data: the data should be added after the specific node
        :return: None
        """
        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        prev_node = new_node.next

    def search_element(self, key):
        """
        :param key: element should search
        :return: None
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    linked_list = LinkedList()
    item_to_add = [1, 10, 5, 100, 6, 1000]
    for item in item_to_add:
        linked_list.insert_at_beginning(item)
    linked_list.print_linked_list()
    linked_list.insert_at_the_end(new_data=2000)
    linked_list.print_linked_list()
    key = 5
    find = linked_list.search_element(key=key)
    print(f"Key {key} in Linked List?: {find}")
    linked_list.insert_at_the_end(new_data=22222)
    linked_list.print_linked_list()

