'''Implement the following functions recursively.'''


class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def print_list(head):
    '''Prints all items in the Singly linked list starting at head'''
    if head == None:
        print(" ")
        return
    if head.next == None:
        print(head.data, end = "")    
    else:
        print(head.data, end =" ")
    print_list(head.next)

def add_zero_between_each_node(head):
    '''Adds a node with 0 between element in the original Singly linked list starting at head
        ○ There should not be a zero node at the end of the list(it is not between two items)'''
    if head == None:
        return
    old_next = head.next
    if old_next != None:
        head.next = SLL_Node(0, old_next)
    add_zero_between_each_node(old_next)
    return head

def to_arraylist_reverse(head):
    ''' Adds all values in the Singly linked list starting at head, reversed to an ArrayList'''
    ret_list = ArrayList()
    if head == None:
        return ret_list
    ret_list = to_arraylist_reverse(head.next)
    ret_list.append(head.data) # eftir á til þess að hafa reversed
    return ret_list

class ArrayList:
    '''Implement the following function inside ArrayList'''
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    def resize(self):
        if self.size == self.capacity:
            self.capacity *= 2
            temp_arr = [None] * self.capacity
            for i in range(self.size):
                temp_arr[i] = self.arr[i]
            self.arr = temp_arr

    def print_list(self):
        ''' Prints all items in the Arraylist'''
        for i in range(self.size - 1):
            print(self.arr[i], end = " ")
        print(self.arr[self.size - 1])

        


if __name__ == "__main__":
    head = SLL_Node(5, SLL_Node(7, SLL_Node(1, SLL_Node(9, SLL_Node(2, SLL_Node(4))))))
    print_list(head)
    print(type(head).__name__)
    print("")
    arr_list = to_arraylist_reverse(head)
    arr_list.print_list()
    print(type(arr_list).__name__)
    print("")
    add_zero_between_each_node(head)
    print_list(head)
    print(type(head).__name__)
    print("")
    arr_list = to_arraylist_reverse(head)
    arr_list.print_list()
    print(type(arr_list).__name__)
    print("")