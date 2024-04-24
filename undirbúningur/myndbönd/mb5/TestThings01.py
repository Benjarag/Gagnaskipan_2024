class Array_list:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

def resize(array_list):
    array_list.arr *= 2
    array_list.capacity *= 2

def append(array_list, value):
    if (array_list.size >= array_list.capacity):
        resize(array_list)
    array_list.arr[array_list.size] = value
    array_list.size += 1

def print_array(array_list):
    str_val = ""
    for i in range(array_list.size):
        str_val += str(array_list.arr[i]) + " "
    print(str_val)

array_list = Array_list()
append(array_list, 4)
append(array_list, 2)
append(array_list, 7)
append(array_list, 6)
append(array_list, 1)
append(array_list, 3)
append(array_list, 5)
append(array_list, 8)
append(array_list, 9)
append(array_list, 10)
append(array_list, 11)
append(array_list, 12)
append(array_list, 13)
append(array_list, 14)

print_array(array_list)
