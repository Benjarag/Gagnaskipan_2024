class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class SLL_node:
    def __init__(self, key=None, data=None, next=None):
        self.key = key
        self.data = data
        self.next = next


class Bucket:
    def __init__(self):
        self.head = None
        self.size = 0

    def recursive_insert(self, node, key, value):
        if node is None:
            self.size += 1
            new_node = SLL_node(key, value)
            print(new_node.data)
            return new_node
        elif node.key > key:
            print(node.key, key)
            node.next = self.recursive_insert(node.next, key, value)
            print(node.next.data)
        elif node.key < key:
            print(node.key, key) 
            self.size += 1
            new_node = SLL_node(key, value)
            new_node.next = node
            print(new_node.data, new_node.next.data)
            return new_node
        else:
            raise ItemExistsException()
        return node

    def insert(self, key, data):
        '''
        ○ Adds this value pair to the collection
        ○ If equal key is already in the collection, raise ItemExistsException()
        '''
        if self.contains(key) == key:
            raise ItemExistsException()
        else:
            self.head = self.recursive_insert(self.head, key, data)

    def update(self, key, data):
        '''
        ○ Sets the data value of the value pair with equal key to data
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        if self.contains(key):
            current = self.head
            while current is not None:
                if current.key == key:
                    current.data = data
                    self.head = current
                current = current.next
            else:
                raise NotFoundException()
        else:
            raise NotFoundException()

    def find(self, key):
        '''
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        current = self.head
        while current is not None:
            if current.key == key:
                return current.data
            current = current.next
        raise NotFoundException()

    def contains(self, key):
        '''
        ○ Returns True if equal key is found in the collection, otherwise False
        '''
        current = self.head
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False
    
    def remove(self, key):
        '''
        ○ Removes the value pair with equal key from the collection
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        # current = self.head
        # previous = None
        # while current is not None:
        #     if current.key == key:
        #         if previous is None:
        #             self.head = current.next
        #         else:
        #             previous.next = current.next
        #         self.size -= 1
        #         return
        #     previous = current
        #     current = current.next
        # raise NotFoundException()
            
    def __setitem__(self, key, data):
        '''
        ○ Override to allow this syntax:
            ■ some_hash_map[key] = data
        ○ If equal key is already in the collection, update its data value
            ■ Otherwise add the value pair to the collection
        '''
        pass
    
    def __getitem__(self, key):
        '''

        ○ Override to allow this syntax:
            ■ my_data = some_bucket[key]
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        pass
    
    def __len__(self):
        '''
        ○ Override to allow this syntax:
            ■ length_of_structure = len(some_bucket)
        ○ Returns the number of items in the entire data structure
        '''
        return self.size


class HashMap:
    def __init__(self):
        self.bucket_count = 10
        self.size = 0
        self.bucket_list = self.build_bucket_list()

        
    
    def build_bucket_list(self):
        return [Bucket() for _ in range(self.bucket_count)]

    def insert(self, key, data):
        '''
        ○ Adds this value pair to the collection
        ○ If equal key is already in the collection, raise ItemExistsException()
        '''
        if self.contains(key):
            raise ItemExistsException()
        else:
            hash = MyHashableKey()
            index = hash.__hash__() % self.size
            self.bucket_list[index].insert(key, data)
            self.size += 1

    def update(self, key, data):
        '''
        ○ Sets the data value of the value pair with equal key to data
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        pass

    def find(self, key):
        '''
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        hash = MyHashableKey()
        index = hash.__hash__() % self.size
        return self.bucket_list[index].find(key)
    
    def contains(self, key):
        '''
        ○ Returns True if equal key is found in the collection, otherwise False
        '''
        pass

    def remove(self, key):
        '''
        ○ Removes the value pair with equal key from the collection
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        index = self.hash(key) % self.size
        if self.bucket_list[index].find(key) == key:
            self.bucket_list[index].remove(key)
        else:
            raise NotFoundException()
    
    def __setitem__(self, key, data):
        '''
        ○ Override to allow this syntax:
            ■ some_hash_map[key] = data
        ○ If equal key is already in the collection, update its data value
            ■ Otherwise add the value pair to the collection
        '''
        pass
    
    def __getitem__(self, key):
        '''

        ○ Override to allow this syntax:
            ■ my_data = some_hash_map[key]
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        pass
    
    def __len__(self):
        '''
        ○ Override to allow this syntax:
            ■ length_of_structure = len(some_hash_map)
        ○ Returns the number of items in the entire data structure
        '''
        pass
    
    def rebuild(self):
        '''
        When the number of items in the HashMap has reached 120% of the number of buckets (length
        of array or list) it must rebuild(), doubling the number of buckets.
        '''
        pass


class MyHashableKey:
    def __init__(self, int_value, string_value):
        '''
        ○ A constructor that takes an integer value and a string value
        '''
        self.int_value = int_value
        self.string_value = string_value
    
    def __eq__(self, other):
        '''
        ○ Compares two instances of MyHashableKey and returns True if their values are
        equal, otherwise False.
        '''
        if self.int_value == other.int_value and self.string_value == other.string_value:
            return True
        else:
            return False   
    
    def __hash__(self):
        '''
        ○ Returns a positive integer
            ■ The integer value must be the same for instances that are equal
                ○ Otherwise can be any integer
        ○ Don’t use the built-in hash functions for integers and strings!
        ○ Full marks given if hash value gives fairly even distribution of values
        ○ Zero marks if all values end up in same bucket
        ○ Bonus 5% for 10% best (most even) distributions
            ■ Note that key values can sometimes be very close to each other, or
             similar, but in those cases may need particularly good distribution.
        '''
        hashmap = HashMap()
        return (self.int_value % hashmap.bucket_count)

if __name__ == "__main__":
    bucket = Bucket()
    bucket.insert(1, "one")
    print("after inserting 1, bucket.size: ",bucket.size)
    # outcome: 1
    bucket.insert(2, "two")
    print("after inserting 1 and 2, bucket.size): ",bucket.size)
    # outcome: 2
    bucket.insert(3, "three")
    print("after inserting 1, 2 and 3 bucket.size: ", bucket.size)
    # outcome: 3
    bucket.insert(4, "four")
    print("after inserting 1, 2, 3, 4 bucket.size: ", bucket.size)
    # outcome: 4

    print("")

    k1 = MyHashableKey(1, "one")
    print(hash(k1))
    # outcome: 1
    k2a = MyHashableKey(28, "twenty eight")
    print(hash(k2a))
    # outcome: 8
    k2b = MyHashableKey(2, "two")
    print(hash(k2b))
    # outcome: 2
    k3 = MyHashableKey(3, "three")
    print(hash(k3))
    # outcome: 3
    k4 = MyHashableKey(17, "seventeen")
    print(hash(k4))
    # outcome: 7

