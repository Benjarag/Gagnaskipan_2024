import sys

from random import Random

rand = Random()
rand.seed(742983798423)

def create_insert(fake_length):
    num = rand.randint(10, 29)
    print("insert " + str(num))

def create_remove():
    print("remove")

def create_move_to_next():
    print("move_to_next")

def create_move_to_prev():
    print("move_to_prev")

def create_move_to_pos(fake_length):
    pos = rand.randint(-2, fake_length)
    print("move_to_pos " + str(pos))

def create_clear():
    print("clear")

def create_sort():
    print("sort")

def create_get_first_node():
    print("get_first_node")

def create_get_last_node():
    print("get_last_node")

def create_partition():
    print("partition")

def create_dll(complex = False):
    fake_length = 1

    print("new")

    for _ in range(100):
        if complex:
            choice = rand.randint(1, 10)
        else:
            choice = rand.randint(1, 5)
        if choice == 1:
            for _ in range(rand.randint(1, 10)):
                fake_length += 1
                create_insert(fake_length)
        elif choice == 2:
            for _ in range(rand.randint(1, 11)):
                if fake_length > 1:
                    fake_length -= 1
                create_remove()
        elif choice == 3:
            for _ in range(rand.randint(1, max(1, fake_length // 3))):
                create_move_to_next()
        elif choice == 4:
            for _ in range(rand.randint(1, max(1, fake_length // 3))):
                create_move_to_prev()
        elif choice == 5:
            create_move_to_pos(fake_length)
        elif choice == 6:
            create_clear()
        elif choice == 7:
            create_sort()
        elif choice == 8:
            create_partition()
        elif choice == 9:
            create_get_first_node()
        elif choice == 10:
            create_get_last_node()

def main():
    orig_stdout = sys.stdout
    fout = open('tests.txt', 'w+')
    # sys.stdout = fout

    for _ in range(30):
        create_dll()
    
    for _ in range(30):
        create_dll(True)

    # sys.stdout = orig_stdout
    fout.close()


if __name__ == "__main__":
    main()


