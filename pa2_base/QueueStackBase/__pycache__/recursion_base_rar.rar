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
    '''
    Takes in the head of a list as a parameter
    Returns the size of the list
    '''
    temp_node = head
    if temp_node == None:
        return 0
    return 1 + get_size(temp_node.next)

def reverse_list(head):
    '''
    Takes in the head of a list as a parameter
    returns a node, the head of a list that has the same items as the previous
    list, but in reverse order.
    '''
    temp_node = head

    if temp_node == None or temp_node.next == None:
        return temp_node
    
    reversed = reverse_list(temp_node.next)

    temp_node.next.next = temp_node

    temp_node.next = None

    return reversed

def palindrome(head):
    '''
    ○ Takes in the head of a list as a parameter
    ○ Returns True if the list is a palindrome
        ■ A list is a palindrome if it is the same reading it forwards and backwards.
            ● Example: abba, level and radar are palindromes
            ● While adba is not a palindrome
        ■ Since we are using lists instead of strings imagine that every node in the
          list holds a single character
    ○ Otherwise returns False
    ○ This can be done with more than one separate recursive calls that may initialize
      new instances of Node, or move data around. As long as all runs through the
      list/lists are recursive, and the original list sent in is not broken in any way, full
      marks will be given.
    '''
    def is_palindrome_recursive(right):
        nonlocal left
        if right is None:
            return True
        
        is_pal = is_palindrome_recursive(right.next)
        
        is_pal = is_pal and left.data == right.data
        
        left = left.next
        
        return is_pal
    
    if head is None or head.next is None:
        return True
    
    left = head
    return is_palindrome_recursive(head)

if __name__ == "__main__":
    #
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


    #
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
