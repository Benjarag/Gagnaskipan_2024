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
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
    
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        i = 0
        while i < self.size:
            if i == self.size - 1:
                return_string += str(self.arr[i])
            else:
                return_string += str(self.arr[i]) + ", "
            i += 1
        return return_string
    
    #Time complexity: O(n) - linear time in size of list

    def prepend(self, value):
        '''
        Inserts an item into the list before the first item 
        '''
        self.insert(value, 0)
        # return
        
    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        '''
        Inserts an item into the list at a specific location, not overwriting other items
        If the index is not within the current list, raise IndexOutOfBounds()
        It should be possible to add to the front and back of the list, and anywhere in between
        '''
        try:
            if index < 0 or index > self.size:
                raise IndexOutOfBounds("the index is out of bounds")
            
            self.resize()

            for i in range(self.size - 1, index - 1, -1):
                self.arr[i + 1] = self.arr[i]

            self.arr[index] = value
            self.size += 1

        except IndexOutOfBounds as e:
            raise e
        
    #Time complexity: O(1) - constant time
    def append(self, value):
        '''
        Adds an item to the list after the last item
        '''
        self.resize()

        if self.size == 0:
            self.arr[0] = value
        else:
            self.arr[self.size] = value
        
        self.size += 1
        
    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        '''
        ○ Sets the value at a specific location to a specific value
            ■ Overwrites the current value there
            ■ If the index is not within the current list, raise IndexOutOfBounds()
        '''
        try:
            if index < 0 or index > self.size - 1:
                raise IndexOutOfBounds("index out of bounds")
        
            self.arr[index] = value
        
            return self.arr

        except IndexOutOfBounds as e:
            raise e
    #Time complexity: O(1) - constant time
    def get_first(self):
        '''
        Returns the first value in the list
        If there are no items in the list, raise Empty()
        '''
        try:
            if not self.arr:
                raise Empty("There are no items in the list")
            else:
                return self.arr[0]

        except Empty as e:
            raise e

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        '''
        Returns the value at a specific location in the list
        If the index is not within the current list, raise IndexOutOfBounds()
        '''

        try:
            if index < 0 or index > self.size:
                raise IndexOutOfBounds("the index is not within the current list")

            return self.arr[index]            

        except IndexOutOfBounds as e:
            raise e
        
    #Time complexity: O(1) - constant time
    def get_last(self):
        '''
        Returns the last value in the list
        If there are no items in the list, raise Empty()
        '''
        try:
            if self.size == 0 or self.size is None:
                raise Empty("There are no items in the list")
            else:
                return self.arr[self.size - 1]

        except Empty as e:
            raise e

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        '''
        Re-allocates memory for a larger array and populates it with the original array’s items
        '''
        if self.size == self.capacity:
            
            self.capacity *= 2
            temp_arr = [None] * self.capacity

            for i in range(self.size):
                temp_arr[i] = self.arr[i]
            
            self.arr = temp_arr

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        '''
        Removes from the list an item at a specific location
        If the index is not within the current list, raise IndexOutOfBounds()
        '''
        # try:
        if index < 0 or index > self.size - 1:
            raise IndexOutOfBounds("the index is not within the current list")
        
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        
        self.size -= 1
        # except IndexOutOfBounds:
        #     raise IndexOutOfBounds("the index is not within the current list")        

    #Time complexity: O(1) - constant time
    def clear(self):
        '''
        Removes all items from the list
        '''
        # for i in range(0, self.size - 1):
        #     self.arr[i] = None
        
        self.size = 0
    
    def is_ordered(self):
        '''
        Checks if the ArrayList instance is in an ordered state
        '''
        for i in range(self.size - 1):
            if self.arr[i] >= self.arr[i + 1]:
                return False
        return True


    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        '''
        insert a value so that the list retains ordering
        ○ If the ArrayList instance is not in an ordered state, raise NotOrdered()
        '''
        if not self.is_ordered():
            raise NotOrdered("the ArrayList instance is not in an ordered state")

        inserted = False
        for i in range(self.size):  
            if self.arr[i] > value:
                self.insert(value, i)
                inserted = True
                break
        if not inserted:
            self.append(value)

    def binary_search(self, value):
        '''
        finds a value and returns the index
        '''
        min, max = 0, self.size - 1
        while min <= max:
            mid = (min + max) // 2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] < value:
                min = mid + 1
            else:
                max = mid - 1
        return False # return none if it is not found

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        '''
        Returns the index of a specific value
        If the instance of ArrayList is in an ordered state, use recursive binary search
        If the ArrayList instance is not ordered, use linear search
        If the value is not found in the list, raise NotFound()
        '''
        # try:
        if self.is_ordered():
            index = self.binary_search(value)
            if index is not None:
                return index
                
        for i in range(self.size):
            if self.arr[i] == value:
                return i
            
        raise NotFound("the value is not found in the list")
        
        # except NotFound:
        #     raise NotFound("the value is not found in the list")

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        '''
        Removes from the list an item with a specific value
        Can you use only helper functions that have already been implemented?
        If the value is not found in the list, raise NotFound()
        '''
        # try:
        if self.is_ordered():
            index = self.binary_search(value)
            if index is not None:
                self.remove_at(index)
            else:
                raise NotFound("the value is not found in the list")
        
        else:
            found = False
            for index in range(0, self.size - 1):
                if self.arr[index] == value:
                    self.remove_at(index)
                    found = True
                    break
            if not found:
                raise NotFound("the value is not found in the list")
        # except NotFound:
        #     raise NotFound("the value is not found in the list")
        
def modulus(a, b):
    '''
    ● Write the recursive operation modulus that calculates the modulus of two integers without using
    the mathematical operators *, / or %
    ○ e.g.
    ■ modulus(13, 4) == 1
    ■ modulus(12, 3) == 0
    ■ modulus(14, 3) == 2
    '''
    if a > b:
        return modulus(a - b, b)
    else:
        return a
        
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
    if not lis1:
        return 0
    else:
        counter = how_many(lis1[1:], lis2)
        if lis1[0] in lis2:
            counter += 1
        return counter


if __name__ == "__main__":
    '''
    ATH!!! 
    Ég náði ekki að keyra main_test.py skrána af einhverjum ástæðum.
    Ég hannaði mín eigin test í staðinn hér.
    '''
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    # try:
        # arr_list = ArrayList()
        # # Test Case: Inserting a value into an empty list
        # arr_list.append(3)
        # print(arr_list)  # Output: 5 0 0 0 0

        # # Test Case: Inserting a value at index 2
        # arr_list.append(7)
        # arr_list.append(54)
        # print(arr_list)  

        # arr_list.set_at(3, 1)
        # print(arr_list)

        # print(arr_list.get_first())
        
        # print(arr_list.get_at(1))

        # print(arr_list)
        # arr_list.remove_at(1)
        # print(arr_list)

        # arr_list.append(57)
        # print(arr_list)
        # arr_list.append(67)
        # print(arr_list)
        # arr_list.insert_ordered(55)
        # print(arr_list)
        # print(arr_list.find(55))
        # arr_list.remove_value(55)
        # print(arr_list)
        # arr_list.insert(5, 0)
        # print(arr_list)
        # arr_list.append(5)
        # print(arr_list)
        # print(arr_list.find(5))
    
    # except Exception as e:
    #     print(e)

