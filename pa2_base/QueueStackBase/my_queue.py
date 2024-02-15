from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        self.container = LinkedList()
        #self.container = ArrayDeque()

    def add(self, data):
        '''
        Takes a parameter and adds its value 
        to the back of the queue
        '''
        return self.container.push_back(data)
    
    def remove(self):
        '''
        Removes the item off the front of the queue and 
        returns its value
            ■ If the queue is empty, return None
        '''
        return self.container.pop_front()

    def get_size(self):
        '''
        Returns the number of items 
        currently in the queue
        '''
        return self.container.size

    def __str__(self):
        return self.container.__str__()
