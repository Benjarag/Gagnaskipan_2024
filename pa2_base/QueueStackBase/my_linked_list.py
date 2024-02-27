class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.front = None
        self.size = 0
    
    # O(1)
    def push_front(self, data):
        '''
        Takes a parameter and adds its value
        to the front of the list
        '''
        new_node = Node(data, self.front)
        self.front = new_node
        self.size += 1
    
    # O(1)
    def pop_front(self):
        '''
        Removes the item from the front of the list
        and returns its value
            ■ If the list is empty, return None
        '''
        if self.front is None:
            return None
        value = self.front.data
        self.front = self.front.next
        self.size -= 1
        return value
    
    # O(1)
    def push_back(self, data):
        '''
        Takes a parameter and adds its value 
        to the back of the list
        '''
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.size += 1
            return
        
        current = self.front
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
        return
     
    # O(n)
    def pop_back(self):
        '''
        Removes the item from the back of the list
        and returns its value
            ■ If the list is empty, return None
        '''   
        if self.front is None:
            return None
        if self.size == 1:
            value = self.front.data
            self.front = None
            self.size -= 1
            return value

        current = self.front
        while current.next.next:
            current = current.next
        value = current.next.data
        current.next = None
        self.size -= 1
        
        return value


    # O(1)
    def get_size(self):
        '''
        Returns the number of items
        currently in the list
        '''        
        return self.size

    # O(n)
    def __str__(self):
        '''
        Returns a string with 
        all the items in the list,
        separated by a single space
        '''
        ret_str = ""
        node = self.front
   
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str



