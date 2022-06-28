class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        """
        Always Keeping the head at the beginning.
        :param new_data: data element to be add
        :return:
        """
        new_node = ListNode(val=new_data)
        new_node.next = self.head

        self.head = new_node

    def print_linked_list(self):
        print("Element in Linked List")
        temp_head = self.head
        while temp_head:
            print(str(temp_head.val) + " ", end="")
            temp_head = temp_head.next
        print()

    def middleNode(self):
        list_data = []
        temp_head = self.head
        while temp_head:
            list_data.append(temp_head.val)
            temp_head = temp_head.next
        return list_data[len(list_data)//2]
        # nodes = []
        #
        # while head:
        #     nodes.append(head)
        #     head = head.next
        #
        # return nodes[len(nodes) // 2]


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    solution = Solution()
    for d in head:
        solution.insert_at_beginning(new_data=d)
    solution.print_linked_list()
    s = solution.middleNode()
    print(s)
