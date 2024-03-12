'''
Programming assignment 4: Map ADT with binary search tree
Using recursion is not a requirement, but recommended in traversing trees
'''
class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass


class BT_node:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BSTMap:
    '''
    Implement the class BSTMap with a binary search tree data structure.
    The class must fully implement the Map ADT, including the following operations:
    '''

    def __init__(self):
        self.root = None
        self.size = 0
        
    def recursive_insert(self, node, key, data):
        if node is None:
            self.size += 1
            new_node = BT_node(key, data)
            return new_node

        elif node.key > key:
            node.left = self.recursive_insert(node.left, key, data)
        elif node.key < key:
            node.right = self.recursive_insert(node.right, key, data)
        else:
            raise ItemExistsException()
        return node

    def insert(self, key, data):
        '''
        ○ Adds this value pair to the collection
        ○ If equal key is already in the collection, raise ItemExistsException()
        '''
        node = BT_node(key, data)
        self.root = self.recursive_insert(self.root, key, data)

    def update(self, key, data):
        '''
        ○ Sets the data value of the value pair with equal key to data
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        current_node = self.root
        parent_node = None

        while current_node is not None:
            if key == current_node.key:
                current_node.data = data
                return
            elif key < current_node.key:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right
        raise NotFoundException()
        
    def recursive_find(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node.data
        elif node.key > key:
            return self.recursive_find(node.left, key)
        return self.recursive_find(node.right, key)

    def find(self, key):
        '''
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        data_value = self.recursive_find(self.root, key)
        if data_value is None:
            raise NotFoundException()
        return data_value

    def recursive_contain(self, node, key):
        if node.key == key:
            return True
        
    def contains(self, key):
        '''
        ○ Returns True if equal key is found in the collection, otherwise False
        '''
        val = self.recursive_find(self.root, key)
        if val:
            return True
        else:
            return False
    
    def swap_and_remove_with_leftmost(self, node):
        if node.left is not None:
            self.swap_and_remove_with_leftmost(node.left)
        else:
            value = node.data
            self._remove_node(node)
            return value

    def _remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        elif node.right is None:
            return node.right
        elif node.left is None:
            return node.left
        elif node.left is not None and node.right is not None:

            node.data = self.swap_and_remove_with_leftmost(node.right)
        

    def recursive_remove(self, node, key):
        if node is None:
            raise NotFoundException()
        
        elif node.key > key:
            node.left = self.recursive_remove(node.left, key)
        elif node.key < key:
            node.right = self.recursive_remove(node.right, key)
        else: # ==
            return self._remove_node(node)
        
    def remove(self, key):
        '''
        ○ Removes the value pair with equal key from the collection
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        self.size -= 1
        self.root = self.recursive_remove(self.root, key)
    
    def __setitem__(self, key, data):
        '''
        ○ Override to allow this syntax:
            ■ some_bst_map[key] = data
        ○ If equal key is already in the collection, update its data value
            ■ Otherwise add the value pair to the collection
        '''
        true_false = self.recursive_find(self.root, key)
        if true_false is None:
            self.insert(key, data)
        else:
            self.update(key, data)

    def __getitem__(self, key):
        '''
        ○ Override to allow this syntax:
            ■ my_data = some_bst_map[key]
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        if self.contains(key):
            data_value = self.find(key)
            return data_value
        else:
            raise NotFoundException()

    def __len__(self):
        '''
        ○ Override to allow this syntax:
            ■ length_of_structure = len(some_bst_map)
        ○ Returns the number of items in the entire data structure
        '''
        return self.size

    def str_recur(self, node):
        if node == None:
            return "" 
        # if node is not None:
        return self.str_recur(node.left) + "{" + f'{node.key}:{node.data}' + '} ' + self.str_recur(node.right)
       

    def __str__(self):
        '''
        ○ Returns a string with the items ordered by key and separated by a single space.
        ○ Each item is printed on the following format: {value_of_key:value_of_data}
            ■ m[5] = “five”
              m[3] = “three”
              m[7] = “seven”
              print(“output: ” + str(m))
                ● output: {3:three} {5:five} {7:seven}
        '''
        return self.str_recur(self.root)

# m = BSTMap()

# m.insert(5, "five")
# m.insert(3, "three")
# m.insert(7, "seven")


# print(m[3])