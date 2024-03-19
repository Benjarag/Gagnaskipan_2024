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
        try:
            if node is None:
                self.size += 1
                new_node = SLL_node(key, value)
                return new_node
            elif node.key > key:
                node.next = self.recursive_insert(node.next, key, value)
            elif node.key < key:
                self.size += 1
                new_node = SLL_node(key, value)
                new_node.next = node
                return new_node
        except:
            raise ItemExistsException()
        return node

    def insert(self, key, data):
        '''
        ○ Adds this value pair to the collection
        ○ If equal key is already in the collection, raise ItemExistsException()
        '''
        if self.contains(key):
            raise ItemExistsException()
        self.head = self.recursive_insert(self.head, key, data)

    def insert_uptade(self, key, data):
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
                    return
                current = current.next
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
        current = self.head
        previous = None
        try:
            while current is not None:
                if current.key == key:
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next # finna afhverju previous.next = current.next en ekki current = current.next
                    self.size -= 1
                    return
                previous = current
                current = current.next
        except:
            raise NotFoundException()
            
    def __setitem__(self, key, data):
        '''
        ○ Override to allow this syntax:
            ■ some_hash_map[key] = data
        ○ If equal key is already in the collection, update its data value
            ■ Otherwise add the value pair to the collection
        '''
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)
    
    def __getitem__(self, key):
        '''

        ○ Override to allow this syntax:
            ■ my_data = some_bucket[key]
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        if self.contains(key):
            return self.find(key)
        else:
            raise NotFoundException()
    
    def __len__(self):
        '''
        ○ Override to allow this syntax:
            ■ length_of_structure = len(some_bucket)
        ○ Returns the number of items in the entire data structure
        '''
        return self.size


class HashMap:
    def __init__(self):
        self.bucket_count = 4
        self.build_bucket_list()

    def build_bucket_list(self):
        self.size = 0
        self.bucket_list = [Bucket() for _ in range(self.bucket_count)]

    def insert(self, key, data):
        '''
        ○ Adds this value pair to the collection
        ○ If equal key is already in the collection, raise ItemExistsException()
        '''
        self.rebuild()
        if self.contains(key):
            raise ItemExistsException()
        index = hash(key) % self.bucket_count
        self.bucket_list[index].insert(key, data)
        self.size += 1

    def update(self, key, data):
        '''
        ○ Sets the data value of the value pair with equal key to data
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        if not self.contains(key):
            raise NotFoundException()
        else:
            index = hash(key) % self.bucket_count
            self.bucket_list[index].insert_uptade(key, data)
            

    def find(self, key):
        '''
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        for bucket in self.bucket_list:
            if bucket.contains(key):
                return bucket.find(key)
        raise NotFoundException()
    
    def contains(self, key):
        '''
        ○ Returns True if equal key is found in the collection, otherwise False
        '''
        index = hash(key) % self.bucket_count
        if self.bucket_list[index].contains(key):
            return True
        else:
            return False

    def remove(self, key):
        '''
        ○ Removes the value pair with equal key from the collection
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        index = hash(key) % self.bucket_count
        try:
            if self.bucket_list[index].contains(key):
                self.bucket_list[index].remove(key)
                self.size -= 1
        except:
            raise NotFoundException()
    
    def __setitem__(self, key, data):
        '''
        ○ Override to allow this syntax:
            ■ some_hash_map[key] = data
        ○ If equal key is already in the collection, update its data value
            ■ Otherwise add the value pair to the collection
        '''
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)
    
    def __getitem__(self, key):
        '''

        ○ Override to allow this syntax:
            ■ my_data = some_hash_map[key]
        ○ Returns the data value of the value pair with equal key
        ○ If equal key is not in the collection, raise NotFoundException()
        '''
        if self.contains(key):
            return self.find(key)
        else:
            raise NotFoundException
    
    def __len__(self):
        '''
        ○ Override to allow this syntax:
            ■ length_of_structure = len(some_hash_map)
        ○ Returns the number of items in the entire data structure
        '''
        return self.size
    
    def rebuild(self):
        '''
        When the number of items in the HashMap has reached 120% of the number of buckets (length
        of array or list) it must rebuild(), doubling the number of buckets.
        '''
        if self.size >= self.bucket_count * 1.2:
            temp_bucket_list = self.bucket_list
            self.bucket_count *= 2
            self.build_bucket_list()
            for bucket in temp_bucket_list:
                current = bucket.head
                while current is not None:
                    self.insert(current.key, current.data)
                    current = current.next
                

                


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
    pass
