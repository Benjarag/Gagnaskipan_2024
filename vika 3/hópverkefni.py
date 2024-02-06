class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.size = 4
        self.arr = [0] * self.size
    
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        i = 0
        while i < self.size:
            return_string += str(self.arr[i]) + " "
            i += 1
        return return_string
    
    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.arr = [value] + self.arr

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        '''
        Inserts an item into the list at a specific location, not overwriting other items
        If the index is not within the current list, raise IndexOutOfBounds()
        It should be possible to add to the front and back of the list, and anywhere in between
        '''
        try:
            if index < 0 or index > self.size:
                raise ValueError("index out of bounds")
            
            for i in range(self.size - 1, index, -1):
                self.arr[i] = self.arr[i - 1]

            self.arr[index] = value

        except ValueError:
            raise IndexOutOfBounds("Index is out of bounds")
    # ekki alveg rétt því þetta er O(n) en ekki O(1)
        
    #Time complexity: O(1) - constant time
    def append(self, value):
        '''
        Adds an item to the list after the last item
        '''
        if self.size:
            self.arr[self.size] = value
            self.size += 1
        else:
            raise IndexError("Cannot append, list is full")

        return self.arr
        
     
    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        '''
        ○ Sets the value at a specific location to a specific value
            ■ Overwrites the current value there
            ■ If the index is not within the current list, raise IndexOutOfBounds()
        '''
        try:
            if index < 0 or index > self.size:
                raise ValueError("index out of bounds")
        except ValueError:
            raise IndexOutOfBounds("Index is out of bounds")    

    #Time complexity: O(1) - constant time
    def get_first(self):
        '''
        Returns the first value in the list
        If there are no items in the list, raise Empty()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        '''
        Returns the value at a specific location in the list
        If the index is not within the current list, raise IndexOutOfBounds()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        '''
        Returns the last value in the list
        If there are no items in the list, raise Empty()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        '''
        Re-allocates memory for a larger array and populates it with the original array’s items
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        '''
        Removes from the list an item at a specific location
        If the index is not within the current list, raise IndexOutOfBounds()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        '''
        Removes all items from the list
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        '''
        nsert a value so that the list retains ordering
        ○ If the ArrayList instance is not in an ordered state, raise NotOrdered()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        '''
        Returns the index of a specific value
        If the instance of ArrayList is in an ordered state, use recursive binary search
        If the ArrayList instance is not ordered, use linear search
        If the value is not found in the list, raise NotFound()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        '''
        Removes from the list an item with a specific value
        Can you use only helper functions that have already been implemented?
        If the value is not found in the list, raise NotFound()
        '''
        # TODO: remove 'pass' and implement functionality
        pass

    def modulus(a, b):
        '''
        ● Write the recursive operation modulus that calculates the modulus of two integers without using
        the mathematical operators *, / or %
        ○ e.g.
        ■ modulus(13, 4) == 1
        ■ modulus(12, 3) == 0
        ■ modulus(14, 3) == 2
        '''
        pass

    def how_many(lis1, lis2):
        '''
        ● Write the recursive operation how_many that takes two lists and returns an integer the value of
        which is how many of the items in lis1 are also in lis2.
        ○ e.g.
        ■ how_many([a,f,d,t], [a,b,c,d,e]) == 2
        ○ If two items in lis1 have the same value, they are each counted
        ■ E.g.
        ● how_many([a,b,f,g,a,t,c], [a,b,c,d,e]) == 4
        '''
        pass





if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_list = ArrayList()
    arr_list.insert(5, 1)
    print(arr_list)
    # Output: 0, 5, 0, 0
