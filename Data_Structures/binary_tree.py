class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_node(self, value, node=None, queue=[]):
        print(f"Continuing for {value}")
        new_node = Node(value=value)

        if node is None:
            self.root = new_node
            queue.insert(0, new_node)
        else:
            queue.insert(0, node)
            if node.left_child and node.right_child:
                popped_node = queue.pop()
                print("both child full so poped", popped_node.value)
                queue.insert(0, popped_node.left_child)
                queue.insert(0, popped_node.right_child)
                print('start for next sub-root', queue[-1].value)
                self.add_node(value=value, node=queue[-1], queue=queue)

            elif node.left_child is None:
                node.left_child = new_node
                queue.insert(0, new_node)

            elif node.right_child is None:
                node.right_child = new_node
                queue.insert(0, new_node)

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
    b_tree = BinaryTree()
    queue = []
    for i in list_data:
        b_tree.add_node(queue=[], node=b_tree.root, value=i)

    print("In-order ", end='= ')
    b_tree.in_order(node=b_tree.root)

    print("\nPre-order ", end='= ')
    b_tree.pre_order(node=b_tree.root)

    print("\nPost-order ", end='= ')
    b_tree.post_order(node=b_tree.root)
