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

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_list = ArrayList()
    arr_list.insert(5, 1)
    print(str(arr_list))  # Output: 0, 5, 0, 0
