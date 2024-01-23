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
# print(increase_numbers_at_random_index([3, 6, 1, 8, 3]))
# O(n)

def switch_items_in_list():
