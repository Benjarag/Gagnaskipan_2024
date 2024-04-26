class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def add_to_front(head, data):
    return Node(data, head)

#iterative version
# def print_to_screen(head):
#     while head != None:
#         print(head.data, end=" ")
#         head = head.next
#     print("")

#recursive version
def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def remove_from_front(head):
    if head == None:
        return None
    return head.next

def add_to_back(head, data):
    if head == None:
        return Node(data, None)
    head.next = add_to_back(head.next, data)
    return head

def remove_from_back(head):
    if head == None or head.next == None:
        return None
    head.next = remove_from_back(head.next)
    return head

#iterative version
# def length_of_list(head):
#     ret_val = 0
#     while head != None:
#         ret_val += 1
#         head = head.next
#     return ret_val

#recursive version
def length_of_list(head):
    if head == None:
        return 0
    return 1 + length_of_list(head.next)

# only change 1 to head.data if data is integers,
# otherwise need extra base case
def sum_of_list(head):
    if head == None:
        return None
    elif head.next == None:
        return head.data
    return head.data + sum_of_list(head.next)

# if I've passed the smaller data
#   I insert at the front of this item
# otherwise continue
def insert_ordered(head, data):
    if head == None or head.data > data:
        return Node(data, head)
    head.next = insert_ordered(head.next, data)
    return head

#iterative version
# def insert_ordered(head, data):
#     if head == None or head.data >= data:
#         return Node(data, head)
#     node = head
#     while node.next != None and node.next.data < data:
#         node = node.next
#     node.next = Node(data, node.next)
#     return head

def reverse_list(head):
    if head == None or head.next == None:
        return head
    node = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return node

def merge_lists(head1, head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1
    elif head1.data < head2.data:
        head1.next = merge_lists(head1.next, head2)
        return head1
    else:
        head2.next = merge_lists(head1, head2.next)
        return head2

def merge_sort(head):
    if head == None or head.next == None:
        return head
    node_half = head
    node = head.next
    while node != None and node.next != None:
        node_half = node_half.next
        node = node.next.next
    node = node_half.next
    node_half.next = None
    return merge_lists(merge_sort(head), merge_sort(node))

test = Node("A", Node("B", Node("C", Node("D", Node("E")))))
print(reverse_list(test))

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1
    
    def pop(self):
        if self.top == None:
            return None
        ret_val = self.top.data
        self.top = self.top.next
        self.size -= 1
        return ret_val

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.top
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.head == None:
            self.head = self.tail = Node(data, None)
        else:
            self.tail.next = Node(data, None)
            self.tail = self.tail.next
        self.size += 1
    
    def remove(self):
        if self.head == None:
            return None
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head == None:
            self.tail = self.head
        return ret_val
    
    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        self.head = Node(data, self.head)
        if self.tail == None:
            self.tail = self.head
        self.size += 1
    
    def pop_front(self):
        if self.head == None:
            return None
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head == None:
            self.tail = self.head
        return ret_val
    
    def push_back(self, data):
        if self.head == None:
            self.head = self.tail = Node(data, None)
        else:
            self.tail.next = Node(data, None)
            self.tail = self.tail.next
        self.size += 1
    
    def pop_back(self):
        if self.head == None:
            return None
        ret_val = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            self.tail = node
            self.tail.next = None
        self.size -= 1
        return ret_val
    
    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str



if __name__ == "__main__":

    head = None

    head = add_to_back(head, "A")
    head = add_to_back(head, "B")
    head = add_to_back(head, "C")
    head = add_to_back(head, "D")
    head = add_to_back(head, "E")

    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    print("sum of list: " + str(sum_of_list(head)))

    head = add_to_front(head, "1")
    head = add_to_front(head, "2")
    head = add_to_front(head, "3")
    head = add_to_front(head, "4")
    head = add_to_front(head, "5")

    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    print("sum of list: " + str(sum_of_list(head)))

    head = remove_from_front(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_back(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_front(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_back(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_front(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_back(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_front(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    print("sum of list: " + str(sum_of_list(head)))
    head = remove_from_back(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_front(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_back(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_front(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    head = remove_from_back(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    print("sum of list: " + str(sum_of_list(head)))


    head = None
    head = insert_ordered(head, "K")
    print_to_screen(head)
    head = insert_ordered(head, "M")
    print_to_screen(head)
    head = insert_ordered(head, "O")
    print_to_screen(head)
    head = insert_ordered(head, "B")
    print_to_screen(head)
    head = insert_ordered(head, "L")
    print_to_screen(head)
    head = insert_ordered(head, "A")
    print_to_screen(head)
    head = insert_ordered(head, "D")
    print_to_screen(head)
    head = insert_ordered(head, "R")
    print_to_screen(head)

    head = reverse_list(head)
    print_to_screen(head)
    print("length of list: " + str(length_of_list(head)))
    print("sum of list: " + str(sum_of_list(head)))
    head = reverse_list(head)
    print_to_screen(head)
    head2 = None
    head2 = insert_ordered(head2, "E")
    head2 = insert_ordered(head2, "F")
    head2 = insert_ordered(head2, "C")
    head2 = insert_ordered(head2, "J")
    head2 = insert_ordered(head2, "I")
    head2 = insert_ordered(head2, "G")
    head2 = insert_ordered(head2, "S")
    head2 = insert_ordered(head2, "P")

    print_to_screen(head2)
    head = merge_lists(head, head2)
    print_to_screen(head)


    head = None
    head = add_to_front(head, "K")
    head = add_to_front(head, "M")
    head = add_to_front(head, "O")
    head = add_to_front(head, "B")
    head = add_to_front(head, "L")
    head = add_to_front(head, "A")
    head = add_to_front(head, "D")
    head = add_to_front(head, "R")
    head = add_to_front(head, "E")
    head = add_to_front(head, "F")
    head = add_to_front(head, "C")
    head = add_to_front(head, "J")
    head = add_to_front(head, "I")
    head = add_to_front(head, "G")
    head = add_to_front(head, "S")
    head = add_to_front(head, "P")

    print_to_screen(head)

    head = merge_sort(head)

    print_to_screen(head)

    stack = Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    stack.push("4")
    stack.push("5")
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))
    print("value off top of stack: " + str(stack.pop()))
    print("stack: " + str(stack))
    print("size of stack: " + str(stack.get_size()))


    queue = Queue()
    queue.add("1")
    queue.add("2")
    queue.add("3")
    queue.add("4")
    queue.add("5")
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))
    print("value from front of queue: " + str(queue.remove()))
    print("queue: " + str(queue))
    print("size of queue: " + str(queue.get_size()))


    linked_list = LinkedList()
    linked_list.push_front("1")
    linked_list.push_back("2")
    linked_list.push_front("3")
    linked_list.push_front("4")
    linked_list.push_back("5")
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from front of list: " + str(linked_list.pop_front()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from back of list: " + str(linked_list.pop_back()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from front of list: " + str(linked_list.pop_front()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from back of list: " + str(linked_list.pop_back()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from front of list: " + str(linked_list.pop_front()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from back of list: " + str(linked_list.pop_back()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from front of list: " + str(linked_list.pop_front()))
    print("list: " + str(linked_list))
    print("size of list: " + str(linked_list.get_size()))
    print("value from back of list: " + str(linked_list.pop_back()))
