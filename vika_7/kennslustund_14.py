class BT_node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def populate_tree(self):
        self.root = self.populate_tree_recur()

    def populate_tree_recur(self):
        value = input("Enter node value: ")
        if value == "":
            return None
        new_node = BT_node(value)

        new_node.left = self.populate_tree_recur()
        new_node.right = self.populate_tree_recur()

        return new_node

    def print_preorder(self):
        self.print_preorder_recur(self.root)
        print("")
        self.print_inorder_recur(self.root)
        print("")
        self.print_postorder_recur(self.root)
    
    def print_preorder_recur(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        self.print_preorder_recur(node.left)
        self.print_preorder_recur(node.right)
        
    def print_inorder_recur(self, node):
        if node == None:
            return
        self.print_inorder_recur(node.left)
        print(node.data, end=" ")
        self.print_inorder_recur(node.right)
        
    def print_postorder_recur(self, node):
        if node == None:
            return
        self.print_postorder_recur(node.left)
        self.print_postorder_recur(node.right)
        print(node.data, end=" ")


class GT_node:
    def __init__(self, data=None):
        self.children = []
        self.data = data

class GeneralTree:
    def __init__(self):
        self.root = None

    def populate_G_tree(self):
        print("ROOT: ", end = " ")
        self.root = self.populate_G_tree_recur()
    
    def populate_G_tree_recur(self, level = 0):
        value = input("Enter node value: ")
        if value == "":
            return None
        new_node = GT_node(value)
        level += 1
        while True:
            print(level *'  ' + "---NODE: ", end = " ")
            child_node = self.populate_G_tree_recur(level)
            if child_node is None:
                break
            new_node.children.append(child_node)
        # for i in range(0, len(self.children)):
        #     new_node = GT_node(new_node.children[i])
            
        return new_node
    
    def print_preorder_G(self):
        self.print_preorder_G_recur(self.root)
    
    def print_preorder_G_recur(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        for child in node.children:
            self.print_preorder_G_recur(child)



# test here
tree = BT_node()
tree.populate_tree()
tree.print_preorder()
# tree.populate_G_tree()
# tree.print_preorder_G()


