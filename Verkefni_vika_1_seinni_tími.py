def power(first_inp, second_inp):
    while second_inp < 0:
        second_inp = int(input("Only positive numbers\n"))
    return first_inp**second_inp
# print(power(int(input()), int(input())))
# O(1)

def multiplication_of_positive_integers(first_inp, second_inp):
    # check for special cases (0 or 1)
    if first_inp == 0 or second_inp == 0:
        return 0
    elif first_inp == 1:
        return second_inp
    elif second_inp == 1:
        return first_inp

    result = 0

    smaller, larger = min(first_inp, second_inp), max(first_inp, second_inp)
    for i in range(smaller):
        result += larger

    return result

# print(multiplication_of_positive_integers(8, 3))
# O(n)

import random
def random_number_insertion(size):
    lis = [0] * size
    for i in range(size):
        lis[i] = random.randint(1, 6)
    return lis
# print(random_number_insertion(int(input("input size "))))
# O(n)

def print_your_list_to_the_screen(lis):
    i = 0
    for num in lis:
        i += 1
        if len(lis) == i:
            print(num)
        else:
            print(num, end=', ') 
# print_your_list_to_the_screen([3, 6, 1, 8, 3])
# O(n)            

def increase_numbers_at_random_index(lis):
    for i in range(len(lis)):
        random_number = random.randint(0, len(lis)-1)
    lis[random_number] = random_number
    return lis
print(increase_numbers_at_random_index([3, 6, 1, 8, 3]))
# O(n)

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