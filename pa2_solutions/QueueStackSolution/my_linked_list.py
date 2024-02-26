
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
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
        self.size -= 1
        if self.head.next == None:
            temp = self.head
            self.head = None
            return temp.data
        node = self.head
        while True:
            if node.next.next == None:
                temp = node.next
                node.next = None
                return temp.data
            node = node.next
                
                

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

