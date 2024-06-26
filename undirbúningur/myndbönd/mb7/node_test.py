class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)
        if self.head == None: # er listinn tomur
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
    def __str__(self):
        ret_str = ""
        node = self.head
        while node != None:
            ret_str += str(node.data) + "\n"
            node = node.next
        return ret_str



# listinn = LinkedList()
# for i in range(1, 6):
#     listinn.push_back("string " + str(i))

# print(listinn)

def push_front(head, data):
    new_node = Node(data, head)
    return new_node

def print_list(head):
    if head != None:
        print(head.data)
        print_list(head.next)

head = Node()
head.data = "string 1"
for i in range(2, 6):
    head = push_front(head, "string " + str(i))
    

print_list(head)

# node = head
# while node != None:
#     print(node.data)
#     node = node.next