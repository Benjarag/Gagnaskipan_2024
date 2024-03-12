class ItemExistsException(Exception):
    pass

class Map_ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
    

class SLL_node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next
        

class Map_SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def recursive_insert(self, node, key, value):
        if node is None:
            self.size += 1
            new_node = SLL_node(key, value)
            print(new_node.data)
            return new_node
        elif node.key > key:
            print(node.key, key)
            node.next = self.recursive_insert(node.next, key, value)
            print(node.next.data)
        elif node.key < key:
            print(node.key, key) 
            self.size += 1
            new_node = SLL_node(key, value)
            new_node.next = node
            print(new_node.data, new_node.next.data)
            return new_node
        else:
            raise ItemExistsException()
        return node

    def insert(self, key, value):
        '''
        ■ Adds an item to the map with this key and data value
        '''
        self.head = self.recursive_insert(self.head, key, value)
        
    def find(self, key):
        '''
        ■ Returns the data value associated with that key
        '''
        pass

    def update(self, key, value):
        '''
        ■ Sets a new value for the data associated with that key
        '''
        pass

    def remove(self, key):
        '''
        ■ Removes the item associated with that key from the map
        '''
        pass

    def str_recur(self, node):
        if node == None:
            return ""
        return self.str_recur(node.next) + str(node.key) + " : " + str(node.data) + "\n"

    def __str__(self):
        return self.str_recur(self.head)



# tests

mapsll = Map_SLL()
mapsll.insert("d", 4)
mapsll.insert("c", 3)
mapsll.insert("a", 1)
# mapsll.insert("b", 2)
print(mapsll.size)
print(mapsll)