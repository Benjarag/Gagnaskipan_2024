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

    def __str__(self):
        ret_str = ""
        if self.left != None:
            ret_str += str(self.left)
        ret_str += "{" + str(self.key) + ":" + str(self.data) + "} "
        if self.right != None:
            ret_str += str(self.right)
        return ret_str

class BSTMap:
    '''
    Implement the class BSTMap with a binary search tree data structure.
    The class must fully implement the Map ADT, including the following operations:
    '''

    def __init__(self):
        self.root = None
        self.size = 0
        
    def recursive_insert(self, key, data, node):# favored
        if node == None:
            self.size += 1
            return BT_node(key, data)
        elif key < node.key:
            node.left = self.recursive_insert(key, data, node.left)
        elif node.key < key:
            node.right = self.recursive_insert(key, data, node.right)
        else:
            raise ItemExistsException()
        return node

    def insert(self, key, data):
        '''
        ○ Adds this value pair to the collection
        ○ If equal key is already in the collection, raise ItemExistsException()
        '''
        self.root = self.recursive_insert(key, data, self.root)

    def recursive_find(self, node, key):# favored
        if node is None:
            return None
        if node.key == key:
            return node
        elif node.key > key:
            return self.recursive_find(node.left, key)
        return self.recursive_find(node.right, key)
    
    def update(self, key, data):# favored
        '''
        ○ Sets the data value of the value pair with equal key to data
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        node = self.recursive_find(self.root, key)
        if node == None:
            raise NotFoundException()
        node.data = data
        
    def find(self, key):# favored
        '''
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        node = self.recursive_find(self.root, key)
        if node is None:
            raise NotFoundException()
        return node.data
        
    def contains(self, key):# favored
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
        self.root = self.recursive_remove(self.root, key)
        self.size -= 1
    
    def __setitem__(self, key, data):
        '''
        ○ Override to allow this syntax:
            ■ some_bst_map[key] = data
        ○ If equal key is already in the collection, update its data value
            ■ Otherwise add the value pair to the collection
        '''
        self.insert(key, data)
        
    def __getitem__(self, key):
        '''
        ○ Override to allow this syntax:
            ■ my_data = some_bst_map[key]
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        return self.find(key)

    def __len__(self):
        '''
        ○ Override to allow this syntax:
            ■ length_of_structure = len(some_bst_map)
        ○ Returns the number of items in the entire data structure
        '''
        return self.size

    # def str_recur(self, node):
    #     if node == None:
    #         return "" 
    #     # if node is not None:
    #     return self.str_recur(node.left) + "{" + f'{node.key}:{node.data}' + '} ' + self.str_recur(node.right)
       

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
        return str(self.root).strip() if self.root != None else ""



class MyComparableKey:
    def __init__(self, int_value, string_value):
        '''
        ○ A constructor that takes an integer value and a string value
        '''
        self.int_value = int_value
        self.string_value = string_value

    def __lt__(self, other):
        '''
        Compares two instances of MyComparableKey and returns True if the value of
        self is lower, otherwise False.
        ○ A key value is considered lower if the integer value is lower.
            ■ In case of equal integers the order of the strings is used.
        ○ It is OK to use built in operators for base types in this implementation.
        
        '''
        if self.int_value == other.int_value:
            return self.string_value < other.string_value
        return self.int_value < other.int_value

      