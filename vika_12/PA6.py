import random

def pick_a_random_word():
    '''
    Picks a random word from the word_bank.txt file
    '''
    with open("vika_12/word_bank.txt", "r") as f:
        words = f.readlines()
        line_words = random.choice(words)
        word_list = line_words.split(" ")
        word = random.choice(word_list)
        
        return word

