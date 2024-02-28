class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)
    
def sum_even_numbers(node):
    '''
    ○ Takes in the parameter node which is the head of a singly linked list
    ○ Returns the sum of all even numbers in the singly linked list
        ■ Use % operator to find if a number is even
    '''
    sum = 0
    while node is not None:
        # if node.data:
        if node.data % 2 == 0:
            sum += node.data
        node = node.next
    return sum


def remove_even_numbers(node):
    '''
    ○ Takes in the parameter node which is the head of a singly linked list
    ○ Removes all even numbers from the list
    ○ Returns the head of the new list(without the even numbers) from the function
    '''

    if node is None:
        return None
    nd = node
    nd_nxt = node.next
    while nd_nxt is not None:
        if nd_nxt.data % 2 == 0:
            nd.next = nd_nxt.next
        else:
            nd = nd_nxt
        nd_nxt = nd_nxt.next
    return node

# head = SLL_Node(1, SLL_Node(8, SLL_Node(4, SLL_Node(2, SLL_Node(3, SLL_Node(5, None))))))
# print(remove_even_numbers(head))
class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = DLL_Node("header node")
        self.tailer = DLL_Node("tailer node")
        self.header.next = self.tailer
        self.tailer.prev = self.header

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
    
    def push_back(self, value):
        new_node = DLL_Node(value)
        new_node.prev = self.tailer.prev
        new_node.next = self.tailer
        new_node.prev.next = new_node
        new_node.next.prev = new_node
    
    def remove_negative_values(self):
        '''
        Finds and removes all negative values (x<0) from the doubly linked list
        '''
        if self.header.next == None:
            return
        node = self.header.next
        while node != self.tailer:
            if node.data < 0:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next


if __name__ == "__main__":
    print("testing sll recursion")
    head = SLL_Node(5, SLL_Node(7, SLL_Node(2, SLL_Node(6, SLL_Node(8, SLL_Node(1, SLL_Node(5)))))))
    print(head)
    print("sum", sum_even_numbers(head))
    head = remove_even_numbers(head)
    print("removed even numbers")
    print(head)
    print("sum", sum_even_numbers(head))
    print("testing dll")
    dll = DLL()
    dll.push_back(-7)
    dll.push_back(5)
    dll.push_back(-5)
    dll.push_back(3)
    dll.push_back(-2)
    dll.push_back(-8)
    dll.push_back(-15)
    dll.push_back(4)
    dll.push_back(6)
    dll.push_back(-1)
    print(dll)
    print("removing negatives")
    dll.remove_negative_values()
    print(dll)
