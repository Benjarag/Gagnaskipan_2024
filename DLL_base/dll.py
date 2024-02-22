
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = Node()
        self.tailer = Node()
        self.current = self.tailer
        self.tailer.prev = self.header
        self.header.next = self.tailer
        self.size = 0
        
    def insert(self, data):
        '''
        Inserts an item with that value in front 
        of the node at the current position
            ■ The new node is now in the current position
        '''
        new_node = Node(data, self.current.prev, self.current)
        new_node.prev.next = new_node
        new_node.next.prev = new_node

        self.size += 1
        self.current = new_node

    def remove(self):
        '''
        Removes the node at the current position if there is one
        (otherwise does nothing)
            ■ The node behind the removed node is 
              now in the current position
        '''
        if self.current != self.header and self.current != self.tailer:
            self.current.next.prev = self.current.prev
            self.current.prev.next = self.current.next

            self.current = self.current.next

            self.size -= 1

    def get_value(self):
        '''
        Returns the value of the item at the current 
        position in the list (None if not item)
        '''
        return self.current.data
    
    def move_to_next(self):
        '''
        Moves the current position one item
        closer to the tail/trailer
            ■ Do nothing if at end
        '''
        if self.current.next is not None:
            self.current = self.current.next

    def move_to_prev(self):
        '''
        Moves the current position one item closer to the head/header
            ■ Do nothing if at beginning
        '''
        if self.current.prev is not None:
            self.current = self.current.prev

    def move_to_pos(self, pos):
        '''
        Moves the current position to item #position in the list
            ■ The first actual data item is #0
            ■ Do nothing if position not between 
              beginning and end (including both)
        '''
        if pos < 0 or pos >= self.size:    
            return

        counter = 0
        self.current = self.header.next

        while counter != pos:
            counter += 1
            self.current = self.current.next
        return
    
    def clear(self):
        '''
        Clears all nodes from the list
        '''
        self.size = 0

    def get_first_node(self):
        '''
        Returns the first Node of the list
            ■ The headers next pointer should be pointing to this node
            ■ Returns the node, not the value inside it
        If list is empty, return None
        '''
        return self.header.next
        

    def get_last_node(self):
        '''
        Returns the last Node of the list
            ■ The tailers prev pointer should be pointing to this node
            ■ Returns the node, not the value inside it
        If list is empty, return None
        '''
        return self.tailer.prev
    
    def partition(self, low=None, high=None):
        '''
        Takes in two nodes from the list as a parameter
            ■ You can fetch these nodes with get_first_node and get_last_node
        Uses low as a pivot
            ■ Loops from low to high and moves all nodes smaller than low so they are
              ahead(left side) of the low node.
        Example:
            ■ List before partition: 10 7 7 14 10 15 1 8 2 4 13 7 11 8 8 13
                ● Low is 10 which is also a pivot
                ● High is 13
            ■ List after partition: 7 7 1 8 2 4 7 8 8 10 14 10 15 13 11 13
            ■ Note: The list is not sorted but all elements left of 10 are smaller then 10
              and all elements right of 10 are bigger(or equal)
                ● The order of elements above and below pivot doesn't matter, only
                  that they are on the correct side of the pivot
        After partitioning current position should point towards the pivot
        Partition will only be tested with valid low and high nodes
        '''
        if low is None:
            low = self.get_first_node()
        if high is None:
            high = self.get_last_node()
        
        pivot = low.data

        pass


        

        # while low != high:
        #     while low != high and high.data >= pivot:
        #         high = high.prev
    def sort(self):
        '''
        Order the items in the list with any method that uses only your DLL structure
            ■ No moving everything to another structure, sorting and then moving back!
        After sorting reset the current position to the beginning of the list
        5% Bonus for implementing sort using quicksort
            ■ Partition comes in handy when implementing quicksort
        '''
        pass

    def __len__(self):
        '''
        Returns the number of items in the list
        '''
        return self.size

    def __str__(self):
        '''
        Returns string with all the items
        in the list with a single space between them
        '''
        ret_str = ""
        node = self.header.next
        while node is not self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
    

if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()

    # Test insertion
    dll.insert(5)
    dll.insert(10)
    dll.insert(15)
    print("Doubly Linked List after insertion:", dll)

    # Test removal
    dll.remove()
    print("Doubly Linked List after removal:", dll)

    print(dll.get_value())
    dll.move_to_pos(0)
    print(dll.get_value())


    print(dll.get_first_node().data)
    print(len(dll))
    print(dll.size)
    
    print(dll.get_last_node())


    
