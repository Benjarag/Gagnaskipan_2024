
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL_Deque:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def is_empty(self):
        return self.head.next == self.tail
    
    def get_size(self):
        return self.size
    
    def push_front(self, value):
        node = Node(value, self.head, self.head.next)
        node.next.prev = node
        self.head.next = node
        self.size += 1
    
    def push_back(self, value):
        node = Node(value, self.tail.prev, self.tail)
        node.prev.next = node
        self.tail.prev = node
        self.size += 1

    def get_front(self):
        return self.head.next.data

    def get_back(self):
        return self.tail.prev.data

    def pop_front(self):
        if not self.is_empty():
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            self.size -= 1

    def pop_back(self):
        if not self.is_empty():
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.size -= 1

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node != self.tail:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
    
    def string_backwards(self):
        ret_str = ""
        node = self.tail.prev
        while node != self.head:
            ret_str += str(node.data) + " "
            node = node.prev
        return ret_str


class DLL_PosList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.pos = 0
        self.size = 0
    
    def is_empty(self):
        return self.head.next == self.tail
    
    def get_size(self):
        return self.size
    
    def insert(self, value):
        node = Node(value, self.curr.prev, self.curr)
        node.prev.next = node
        node.next.prev = node
        self.curr = node

    def move_to_next(self):
        if self.curr != self.tail:
            self.curr = self.curr.next
            self.pos += 1

    def move_to_prev(self):
        if self.curr != self.head.next:
            self.curr = self.curr.prev
            self.pos -= 1
    
    def get_value(self):
        return self.curr.data
    
    def remove(self):
        if not self.is_empty() and self.curr != self.tail:
            self.curr.prev.next = self.curr.next
            self.curr.next.prev = self.curr.prev
            self.curr = self.curr.next

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node != self.tail:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
    
    def string_backwards(self):
        ret_str = ""
        node = self.tail.prev
        while node != self.head:
            ret_str += str(node.data) + " "
            node = node.prev
        return ret_str




if __name__ == "__main__":

    print("TESTING DLL_DEQUE\n")
    deque = DLL_Deque()
    deque.push_back("item4")
    deque.push_back("item5")
    deque.push_back("item6")
    deque.push_front("item3")
    deque.push_front("item2")
    deque.push_front("item1")
    print(deque)
    print(deque.string_backwards())
    print("        size: " + str(deque.get_size()))
    print("  front item: " + str(deque.get_front()))
    print("   back item: " + str(deque.get_back()))
    deque.pop_front()
    deque.pop_front()
    print(deque)
    print(deque.string_backwards())
    print("        size: " + str(deque.get_size()))
    print("  front item: " + str(deque.get_front()))
    print("   back item: " + str(deque.get_back()))
    deque.pop_back()
    deque.pop_back()
    print(deque)
    print(deque.string_backwards())
    print("        size: " + str(deque.get_size()))
    print("  front item: " + str(deque.get_front()))
    print("   back item: " + str(deque.get_back()))
    deque.pop_front()
    print(deque)
    print(deque.string_backwards())
    print("        size: " + str(deque.get_size()))
    print("  front item: " + str(deque.get_front()))
    print("   back item: " + str(deque.get_back()))
    deque.pop_back()
    print(deque)
    print(deque.string_backwards())
    print("        size: " + str(deque.get_size()))
    print("  front item: " + str(deque.get_front()))
    print("   back item: " + str(deque.get_back()))
    deque.pop_front()
    deque.pop_back()
    print(deque)
    print(deque.string_backwards())
    print("        size: " + str(deque.get_size()))
    print("  front item: " + str(deque.get_front()))
    print("   back item: " + str(deque.get_back()))


    print("TESTING DLL_POSLIS\n")
    poslis = DLL_PosList()
    poslis.insert("A")
    poslis.insert("B")
    poslis.move_to_next()
    poslis.insert("C")
    poslis.move_to_prev()
    poslis.insert("D")
    print("  current value: " + str(poslis.get_value()))
    print(poslis)
    #print(poslis.string_backwards())
    print("  current value: " + str(poslis.get_value()))
    poslis.move_to_next()
    print("  current value: " + str(poslis.get_value()))
    poslis.remove()
    print(poslis)
    print("  current value: " + str(poslis.get_value()))
    poslis.move_to_next()
    print("  current value: " + str(poslis.get_value()))
    poslis.remove()
    print(poslis)
    print("  current value: " + str(poslis.get_value()))
    poslis.remove()
    print(poslis)
    print("  current value: " + str(poslis.get_value()))
    poslis.move_to_prev()
    print("  current value: " + str(poslis.get_value()))
    poslis.move_to_prev()
    print("  current value: " + str(poslis.get_value()))
    poslis.remove()
    print(poslis)
    poslis.remove()
    print(poslis)
    poslis.remove()
    print(poslis)
    print("  current value: " + str(poslis.get_value()))
