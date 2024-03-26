class GeneralTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []

class GeneralTree:
    def __init__(self):
        #this tree will be used in tests but your code must work for other tree setups as well
        self.root = GeneralTreeNode(7)
        root_child_1 = GeneralTreeNode(2)
        root_child_2 = GeneralTreeNode(1)
        root_child_3 = GeneralTreeNode(9)
        self.root.children = [root_child_1,root_child_2,root_child_3]
        root_grandchild_1 = GeneralTreeNode(13)
        root_grandchild_2 = GeneralTreeNode(4)
        root_grandchild_3 = GeneralTreeNode(2)
        root_grandchild_4 = GeneralTreeNode(6)
        root_grandchild_5 = GeneralTreeNode(1)
        root_grandchild_6 = GeneralTreeNode(8)
        root_grandchild_7 = GeneralTreeNode(15)
        root_grandchild_8 = GeneralTreeNode(5)
        self.root.children[0].children = [root_grandchild_1]
        self.root.children[1].children = [root_grandchild_2,root_grandchild_3,root_grandchild_4,root_grandchild_5]
        self.root.children[2].children = [root_grandchild_6,root_grandchild_7,root_grandchild_8]

    def find_smallest(self):
        '''
        Finds and returns the smallest value in the tree
        '''
        return self.find_smallest_recursive(self.root)

    def find_smallest_recursive(self, node):
        if node is None:
            return None
        elif node.children == []:
            return node.data
        else:
            count_of_children = len(node.children)
            minimum = node.data
            for i in range(count_of_children):
                new_minimum = min(node.data, self.find_smallest_recursive(node.children[i]))
                if minimum > new_minimum:
                    minimum = new_minimum
            return minimum
                


    def sum_tree(self):
        '''
        Adds and returns all numbers in the tree
        '''
        return self.sum_tree_recursive(self.root)

    def sum_tree_recursive(self, node):
        if node is None:
            return 0
        else:
            count_of_children = len(node.children)
            total_num = node.data
            for i in range(count_of_children):
                total_num += self.sum_tree_recursive(node.children[i])
            return total_num

    def odd_numbers(self):
        '''
        Returns a list of all numbers in the tree
        '''
        return self.odd_numbers_recursive(self.root)
    
    def odd_numbers_recursive(self, node):
        if node is None:
            return []
        else:
            count_of_children = len(node.children)
            odd_number_list = []
            if node.data % 2 != 0:
                odd_number_list.append(node.data)
            for i in range(count_of_children):
                odd_number_list += self.odd_numbers_recursive(node.children[i])
            return odd_number_list


if __name__ == "__main__":
    print("Testing find_smallest")
    tree = GeneralTree()
    print(tree.find_smallest())
    print("Testing sum_tree")
    tree = GeneralTree()
    print(tree.sum_tree())
    print("Testing odd_numbers")
    tree = GeneralTree()
    print(sorted(tree.odd_numbers()))
    
    # expected output:
    # Testing find_smallest
    # 1
    # Testing sum_tree
    # 73
    # Testing odd_numbers
    # [1, 1, 5, 7, 9, 13, 15]