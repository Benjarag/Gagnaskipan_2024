class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    if head == None:
        return 0
    return 1 + get_size(head.next)

# def copy_list(head):
#     if head == None:
#         return None
#     return Node(head.data, copy_list(head.next))

def reverse_list(head):
    if head == None or head.next == None:
        return head
    node = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return node

##def compare_lists(head1, head2):
##    if head1 == None and head2 == None:
##        return True
##    if head1.data != head2.data:
##        return False
##    return compare_lists(head1.next, head2.next)


# def palindrome(head):
#     head2 = copy_list(head)
#     head2 = reverse_list(head2)
#     return compare_lists(head, head2)

# ONE PASS RECURSIVE SOLUTION - NO REALLOCATION
# SOLUTION FROM VIDEO
class Palindrome:
    def __init__(self, head):
        self.head = head
    
    def palindrome(self, tail):
        if tail == None:
            return True
        if self.palindrome(tail.next):
            if self.head.data == tail.data:
                self.head = self.head.next
                return True
        return False

def palindrome(head):
    pal = Palindrome(head)
    return pal.palindrome(head)

# # ONE PASS RECURSIVE SOLUTION - NO REALLOCATION
# def palindrome_recur(node1, node2):
#     if node2 == None:
#         return True
#     if palindrome_recur(node1, node2.next):
#         if node1[0].data == node2.data:
#             node1[0] = node1[0].next
#             return True
#     return False

# def palindrome(head):
#     if head == None or head.next == None:
#         return True
#     return palindrome_recur([head], head)

if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

