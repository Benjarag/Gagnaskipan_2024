'''
ATH!!
Það var ekki hægt að testa stronger_tests en þetta er þessi kóði er réttur fyrir weaker_tests, vegna þess ég copyaði testin frá weaker_tests.py
Það væri fínt að fá annaðhvort hjálp við að laga þetta hjá mér vegna þess að þetta er buið að gerast í öllum verkefnunum eða að þið gerið test sem er alltaf hægt að copya
reyndi að fá hjálp með því að senda email á kennrann og æi gegnum piazza en það gekk ekki

'''

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
        if self.current and self.current.prev and self.current.next:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.next
            self.size -= 1
        # if self.current != self.header and self.current != self.tailer:
        #     self.current.next.prev = self.current.prev
        #     self.current.prev.next = self.current.next

        #     self.current = self.current.next

        #     self.size -= 1

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
        if self.current.prev == None:
            
            if self.header.next:
                self.current = self.header.next
                return
            else:
                return
        else:
            self.current = self.current.prev
            if self.current.prev == None:
                self.current = self.header.next
            return
        
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
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.current = self.tailer

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
        self.current = low

        node = self.header
        length = len(self)
        while node is not None and length > 0:
            self.move_to_next()
            pos_val = self.get_value()
            if pos_val is None:
                return
            elif pos_val < pivot:
                self.insert(pos_val)
            else:
                self.move_to_next()
                self.insert(pos_val)
                self.remove()
        self.current = low
        return
       
    

    def sort(self):
        self.quick_sort(self.get_first_node(), self.get_last_node())
        self.current = self.head
        
        # while low != high:
        #     while low != high and high.data >= pivot:
        #         high = high.prev

    def quick_sort(self, low, high):
        '''
        Takes in two nodes from the list as a parameter
            ■ You can fetch these nodes with get_first_node and get_last_node
        Sorts the list using the quicksort algorithm
        After sorting reset the current position to the beginning of the list
        Quick sort will only be tested with valid low and high nodes
        '''
        if low is None:
            low = self.get_first_node()
        if high is None:
            high = self.get_last_node()


        if low != high and low.prev != high:
            self.partition(low, high)
            self.quick_sort(low, low.prev)
            self.quick_sort(low.next, high)
        self.current = self.get_first_node()
        return

    def sort(self):
        '''
        Order the items in the list with any method that uses only your DLL structure
            ■ No moving everything to another structure, sorting and then moving back!
        After sorting reset the current position to the beginning of the list
        5% Bonus for implementing sort using quicksort
            ■ Partition comes in handy when implementing quicksort
        '''
        self.quick_sort(self.get_first_node(), self.get_last_node())
        return
    

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
    pass
    #create tests here if you want
    # print("\n\nTESTING MORE COMPLEX STUFF\n")

    # ■ List before partition: 10 7 7 14 10 15 1 8 2 4 13 7 11 8 8 13
    # ● Low is 10 which is also a pivot
    # ● High is 13
    # ■ List after partition: 7 7 1 8 2 4 7 8 8 10 14 10 15 13 11 13
    # ---
    dll = DLL()
    print("TESTING\n")
    dll.insert("13")
    dll.insert("8")
    dll.insert("8")
    dll.insert("11")
    dll.insert("7")
    dll.insert("13")
    dll.insert("4")
    dll.insert("2")
    dll.insert("8")
    dll.insert("1")
    dll.insert("15")
    dll.insert("10")
    dll.insert("14")
    dll.insert("7")
    dll.insert("7")
    dll.insert("10")
    print("before partition: \n" + str(dll) + "  -1   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)) + "\n")
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print("after partition: \n" + str(dll) + " after partition  -2   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)) + "\n")
    dll.clear()
    print("")
    
    print("\n\nTESTING THE BASIC STUFF\n")
    
    dll = DLL()
    print(str(dll) + "   -1   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -2   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -3   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -4   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -5   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("E")
    print(str(dll) + "   -6   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -7   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -8   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("1")
    print(str(dll) + "   -9   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("2")
    print(str(dll) + "   -10   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -11   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("3")
    print(str(dll) + "   -12   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("4")
    print(str(dll) + "   -13   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -14   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("VALUE")
    print(str(dll) + "   -15   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(8)
    print(str(dll) + "   -16   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -17   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -18   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -19   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(2)
    print(str(dll) + "   -20   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -21   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -22   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -23   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -24   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -25   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -26   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -27   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -28   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -29   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -30   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -31   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -32   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -33   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -34   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -35   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -36   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(-1)
    print(str(dll) + "   -37   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(18)
    print(str(dll) + "   -38   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(0)
    print(str(dll) + "   -39   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -40   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -41   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -42   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -43   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


    print("\n\nTESTING MORE COMPLEX STUFF\n")


    dll = DLL()
    print(str(dll) + "   -1   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -2   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B1")
    print(str(dll) + "   -3   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -4   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -5   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B2")
    print(str(dll) + "   -6   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print(str(dll) + "   -7   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -8   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -9   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_first_node()
    if result != None:
        result = result.data
    print("first node: ", str(result))
    print(str(dll) + "   -10   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B3")
    print(str(dll) + "   -11   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -12   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_last_node()
    if result != None:
        result = result.data
    print("last node: ", str(result))
    print(str(dll) + "   -13   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(0)
    print(str(dll) + "   -14   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B5")
    print(str(dll) + "   -15   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(4)
    print(str(dll) + "   -16   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print(str(dll) + "   -17   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.sort()
    print(str(dll) + "   -18   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.clear()
    print(str(dll) + "   -19   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    

    dll.insert("B")
    print(str(dll) + "   -20   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -21   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("G")
    print(str(dll) + "   -22   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("T")
    print(str(dll) + "   -23   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -24   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -25   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -26   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -27   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -28   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -29   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -30   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -31   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_first_node()
    if result != None:
        result = result.data
    print("first node: ", str(result))
    print(str(dll) + "   -32   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -33   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -34   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -35   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_last_node()
    if result != None:
        result = result.data
    print("last node: ", str(result))
    print(str(dll) + "   -36   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.clear()
    print(str(dll) + "   -37   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
