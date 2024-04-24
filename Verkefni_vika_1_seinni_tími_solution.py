import random
from random import *

class rand:
    gen = Random()

#Time complexity: O(n) - linear time in value of exponent
def power(base, exp):
    ret_val = 1
    for _ in range(exp):
        ret_val *= base
    return ret_val

#Time complexity: O(n) - linear time in value of b
def multiply(a, b):
    ret_val = 0
    for _ in range(b):
        ret_val = ret_val + a
    return ret_val

#Time complexity: O(n) - linear time in size of list
def create_random_list_v1(length):
    lis = []
    for _ in range(length):
        lis.append(rand.gen.randint(1, 6))
    return lis

#Time complexity: O(n) - linear time in size of list
def create_random_list_v2(length):
    lis = [0] * length
    for i in range(length):
        lis[i] = rand.gen.randint(1, 6)
    return lis

#Time complexity: O(n) - linear time in size of list
def print_list(lis):
    if(len(lis) > 0):
        str_val = str(lis[0])
    for i in range(1, len(lis)):
        str_val += ", " + str(lis[i])
    print(str_val)

#Time complexity: O(1) - constant time
def increase_at_random_index(lis):
    index = rand.gen.randint(0, len(lis) - 1)
    lis[index] += 1
    #print("increased at index: " + str(index))

#Time complexity: O(1) - constant time
def switch_random_adjacent(lis):
    index = rand.gen.randint(0, len(lis) - 2)
    tmp = lis[index]
    lis[index] = lis[index + 1]
    lis[index + 1] = tmp
    #print("switched at indices: " + str(index) + " and " + str(index + 1))

#Time complexity: O(1) - constant time
def switch_random(lis):
    index1 = rand.gen.randint(0, len(lis) - 1)
    index2 = rand.gen.randint(0, len(lis) - 1)
    tmp = lis[index1]
    lis[index1] = lis[index2]
    lis[index2] = tmp
    #print("switched at indices: " + str(index1) + " and " + str(index2))

#Time complexity: O(1) - constant time
def switch_adjacent(lis, index):
    tmp = lis[index]
    lis[index] = lis[index + 1]
    lis[index + 1] = tmp
    #print("switched at indices: " + str(index) + " and " + str(index + 1))

#Time complexity: O(n) - linear time in size of list
def insert_ordered(lis, value):
    index = len(lis) - 1
    lis.append(value)
    while index >= 0 and lis[index] > value:
        switch_adjacent(lis, index)
        index -= 1
    #print("inserted value: " + str(value))

#Time complexity: O(n^2) - quadratic time in size of list
# because there's a loop over length that calls
# a function that also has a loop over length
def create_ordered_list(length):
    lis = []
    for _ in range(length):
        insert_ordered(lis, rand.gen.randint(1, 6))
    return lis

#Time complexity: O(n^2) - quadratic time in size of list
# because there's a loop over length that calls
# a function that also has a loop over length
def order_list_v1(lis):
    ret_lis = []
    for i in range(len(lis)):
        insert_ordered(ret_lis, lis[i])
    return ret_lis

#Time complexity: O(n^2) - quadratic time in size of list
# because there's a loop over length and an
# inner loop over a linear function of length
def order_list_v2(lis):
    for i in range(1, len(lis)):
        index = i - 1
        while index >= 0 and lis[index] > lis[index + 1]:
            switch_adjacent(lis, index)
            index -= 1


print(power(2, 2))
print(power(2, 8))
print(power(3, 2))
print(power(4, 3))

print(multiply(2, 3))
print(multiply(5, 5))
print(multiply(7, 2))
print(multiply(8, 3))
print(multiply(6, 13))

lislis = create_random_list_v2(5)
print_list(lislis)
increase_at_random_index(lislis)
print_list(lislis)

for _ in range(18):
    switch_random_adjacent(lislis)
    print_list(lislis)

for _ in range(18):
    switch_random(lislis)
    print_list(lislis)

lislis = []
for _ in range(18):
    insert_ordered(lislis, rand.gen.randint(1, 6))
    print_list(lislis)

lislis = create_ordered_list(10)
print_list(lislis)

lislis = create_random_list_v1(20)
print_list(lislis)
lislis = order_list_v1(lislis)
print_list(lislis)

lislis = create_random_list_v2(24)
print_list(lislis)
order_list_v2(lislis)
print_list(lislis)
