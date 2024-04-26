class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
    
class BinaryTree:
    def __init__(self):
        self.root = None
        # self.children = []
    
    def _populate_tree_recur(self, level = 0):
        data_str = input()
        if data_str == "":
            return None
        level += 1
        print(level*"\t|" + "--LEFT :", end = " ")
        left = self._populate_tree_recur(level)
        print(level*"\t|" + "--RIGHT :", end = " ")
        right = self._populate_tree_recur(level)
        return BinaryTreeNode(data_str, left, right)

    def populate_tree(self):
        print("ROOT: ", end = " ")
        self.root = self._populate_tree_recur()
    
    def _print_tree_recur(self, node):
        if node == None:
            return
        self._print_tree_recur(node.left)
        self._print_tree_recur(node.right)
        print(str(node.data), end=" ")
                    
    def print_tree(self):
        self._print_tree_recur(self.root)

# class GeneralTreeNode:
#     def __init__(self, data = None):
#         self.data = data
#         self.children = []

# class GeneralTree:
#     def __init__(self):
#         self.root = None
#         # self.children = []
    
#     def _populate_tree_recur(self):
#         data_str = input()
#         if data_str == "":
#             return None
#         node = GeneralTreeNode(data_str)
#         while True:
#             child_node = self._populate_tree_recur()
#             if child_node == None:
#                 break
#             node.children.append(child_node)
#         return node

#     def populate_tree(self):
#         self.root = self._populate_tree_recur()
    
#     def _print_tree_recur(self, node):
#         if node == None:
#             return
        
#         print(str(node.data), end=" ")
#         for child_node in node.children:
#             self._print_tree_recur(child_node)


#     def print_tree(self):
#         self._print_tree_recur(self.root)



if __name__ == "__main__":
    bt = BinaryTree()
    bt.populate_tree()
    bt.print_tree()
    # gt = GeneralTree()
    # gt.populate_tree()
    # gt.print_tree()