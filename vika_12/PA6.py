import random

def pick_a_random_word(word_lenght):
    '''
    Picks a random word from the word_bank.txt file
    '''
    with open("vika_12/word_bank_random.txt", "r") as f:
        words = f.readlines()
        word = random.choice(words)
        while len(word) != word_lenght+1:
            word = random.choice(words)
        return word

