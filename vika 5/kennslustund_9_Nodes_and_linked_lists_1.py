class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
def add_to_front(head, data):
    new_node = Node(data, head)
    head = new_node
    return head

def printing_nodes(head):
        try:
            node = head
            while node.data != None:
                print(node.data)
                node = node.next
        except AttributeError:
             return

def printing_nodes_recursive(head):
    if head is None:
        return
    print(head.data)
    printing_nodes_recursive(head.next)

def remove_first(head):
    if head is None:
         return None
    return head.next
     
def add_to_back(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    current = head
    
    while current.next:
        current = current.next
    current.next = new_node
    return head

def remove_from_back(head):
    if head is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


head = None

head = add_to_front(head, 5)
head = add_to_front(head, 7)
head = add_to_front(head, 9)
printing_nodes(head)
print("")
head = remove_from_back(head)
printing_nodes(head)
