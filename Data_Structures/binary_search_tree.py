class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.queue = []

    def get_root(self):
        return self.root

    def add_node(self, value, node=None):
        if node is None:
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left_child is None:
                    node.left_child = Node(value=value)
                else:
                    self.add_node(node=node.left_child, value=value)
            else:
                if node.right_child is None:
                    node.right_child = Node(value=value)
                else:
                    self.add_node(node=node.right_child, value=value)

    def pre_order(self, node):
        """
        Root -> Left -> Right
        :param node:
        :return:
        """
        # First print the data of node
        print(node.value, end=',')
        if node.left_child:
            # Then recur on left child
            self.pre_order(node=node.left_child)
        if node.right_child:
            # Finally recur on right child
            self.pre_order(node=node.right_child)

    def in_order(self, node):
        """
        Left -> Root -> Right
        :param node:
        :return:
        """
        if node is not None:
            # First recur on left child
            self.in_order(node.left_child)

            # then print the data of node
            print(node.value, end=',')

            # now recur on right child
            self.in_order(node.right_child)

    def post_order(self, node):
        """
        Left -> Right -> Root
        :param node:
        :return:
        """
        if node.left_child:
            # First recur on left child
            self.pre_order(node=node.left_child)
        if node.right_child:
            # the recur on right child
            self.pre_order(node=node.right_child)

        # Finally print the data of node
        print(node.value, end=',')


if __name__ == '__main__':
    list_data = [80, 90, 40, 34, 60, 28, 38, 55]
    bst = BinarySearchTree()
    queue = []
    for i in list_data:
        bst.add_node(node=bst.root, value=i)

    print("In-order ", end='= ')
    bst.in_order(node=bst.root)

    print("\nPre-order ", end='= ')
    bst.pre_order(node=bst.root)

    print("\nPost-order ", end='= ')
    bst.post_order(node=bst.root)
