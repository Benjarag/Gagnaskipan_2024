import random

def pick_a_random_word(words, word_lenght):
    '''
    Picks a random word from the word_bank.txt file
    '''
    word = random.choice(words)
    while len(word) != word_lenght+1:
        word = random.choice(words)
    return word

def store_word_bank():
    with open("vika_12/word_bank_random.txt", "r") as f:
        words = f.readlines()
    return words

def add_word_to_word_bank(word):
    '''
    Allow words to be added to the word bank (and file) through the program itself
    '''
    with open("vika_12/word_bank_random.txt", "a") as f:
        f.write(word + "\n")            
    print("Word added to word bank")

def store_current_run(current_user, wins, losses, highscore, winstreak):
    '''
    Stores the current run in a file
    '''
    if current_user != "":
        with open("vika_12/game_history.txt", "a") as f:
            f.write("\n" + current_user + ", " + str(wins) + ", " + str(losses) + ", " + str(highscore) + ", " + str(winstreak))
        print("Run saved")

def get_game_history(name):
    '''
    Reads the highscore file and returns the highest highscore
    '''
    list_of_highscores = []
    with open("vika_12/game_history.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if name in line:
            name_list = []
            for word in line.split(", "):
                name_list.append(word)
            list_of_highscores.append(name_list)
    if list_of_highscores == []:
        print("No game history found")
    else:
        return print_game_history(list_of_highscores)
        
def print_game_history(list_of_highscores):
    '''
    Prints the game history
    '''
    for list in list_of_highscores:
        print(f"Name: {list[0]}, Wins: {list[1]}, Losses: {list[2]}, Highscore: {list[3]}, Win streak: {list[4]}")
    
        






    

