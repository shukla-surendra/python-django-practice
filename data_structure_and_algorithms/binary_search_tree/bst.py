class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self):
        self.root_node = None

    # O(log N)
    def insert(self, data):
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.insert_node(data, self.root_node)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if self.root_node:
            return self.get_min(self.root_node)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)
        else:
            return node.data

    def get_max_value(self):
        if self.root_node:
            return self.get_max(self.root_node)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)
        else:
            return node.data

    def traverse(self):
        if self.root_node:
            self.traverse_in_order(self.root_node)
    # recursive function
    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    # deletion needs to implement


bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(1)
bst.insert(80)
bst.insert(9)
bst.insert(50)


print("smallest item in BST", bst.get_min_value())
print("biggest item in BST", bst.get_max_value())

print("**************************************************")
bst.traverse();


bst_alpha = BinarySearchTree()
bst_alpha.insert("D")
bst_alpha.insert("A")
bst_alpha.insert("C")
bst_alpha.insert("B")
bst_alpha.insert("F")
bst_alpha.insert("E")


print("smallest item in BST", bst_alpha.get_min_value())
print("biggest item in BST", bst_alpha.get_max_value())

print("**************************************************")
bst_alpha.traverse();