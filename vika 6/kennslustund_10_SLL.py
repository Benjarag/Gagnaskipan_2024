
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class SingleLinkedList():
    def __init__(self):
        self.front = None
        self.size = 0
    
    def lenght_of_list(self):
        '''
        ○ Can you do it both iteratively and recursively?
            ■ Which is better?
        ○ Does your implementation work if the node that is 
          sent in is None (empty list)?
        ○ How much is changed so that the function returns 
          the sum of the lists values?
        '''
        # Iteratively
        temp_node = self.front
        counter = 0
        while temp_node != None:
            counter += 1
            temp_node = temp_node.next
        return counter


    def __str__(self):
        ret_str = ""
        node = self.front

        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
            return ret_str



singlelist = SingleLinkedList()	

singlelist.front = Node(1)
singlelist.front.next = Node(2)
singlelist.front.next.next = Node(3)
singlelist.front.next.next.next = Node(4)
print(singlelist.lenght_of_list())