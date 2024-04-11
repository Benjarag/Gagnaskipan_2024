
from PA6 import *
class wordle:
    wins = 0
    losses = 0
    highscore = None
    winstreak = 0

    def __init__(self, word_lenght=5, guesses=5):  
        self.word_lenght = word_lenght
        self.guesses = guesses
        self.word = pick_a_random_word(words, word_lenght)
        self.guessed_word = ""
        self.guesses_left = guesses
        self.guessed_letters = ""
        self.wrong_guessed_letters = ""
        self.right_guessed_letters = ""
        self.half_right_guessed_letters = ""
    
    def build_ret_str(self):
        '''
        Builds a string so the user will see the hints
        for the word correctly under the guessed word
        '''
        ret_str = "                                 "
        if self.guesses_left >= 10:
            ret_str += " "
        if self.guesses_left >= 100:
            ret_str += " "
        return ret_str

    def get_hints(self):
        '''
        Builds the hints for the user
        such as C, c, - and prints them
        '''
        ret_str = self.build_ret_str()
        for i in range(self.word_lenght):
            if self.word.lower()[i] == self.guessed_word.lower()[i]:
                ret_str += "C"
                self.right_guessed_letters += self.guessed_word.lower()[i]
            elif (self.guessed_word.lower()[i] in self.right_guessed_letters) and (self.word.lower().count(self.guessed_word.lower()[i]) == 1):
            # else if letter is already guessed correctly at the correct position and the word does not have any more of the particular letter add a "-" to the return string
                ret_str += "-"
            elif self.guessed_word.lower()[i] in self.word.lower():
                ret_str += "c"
                self.half_right_guessed_letters += self.guessed_word.lower()[i]
            else:
                ret_str += "-"
                self.wrong_guessed_letters += self.guessed_word.lower()[i]
        print(ret_str)
        return ret_str
                
    def get_guessed_word(self):
        '''
        Lets user know if wrong format and doesn't crash
        '''
        guessed_word = input(f"you have {self.guesses_left} guesses left, guess : ")
        while len(guessed_word) != self.word_lenght or guessed_word.isalpha() == False:
            print(f"Please enter a {self.word_lenght} letter word")
            guessed_word = input(f"you have {self.guesses_left} guesses left, guess : ")
        return guessed_word

    def get_game_history(self):
        '''
        ● Allow user to see their history of games/scores
        '''
        print("\nThis is your game history this round:")
        print(f"\nwins: {wordle.wins}")
        print(f"losses: {wordle.losses}")
        print(f"highscore: {wordle.highscore}")
        print(f"winstreak: {wordle.winstreak}\n")
        if current_user != "":
            print(f"Game history for {current_user}:\n")
            get_game_history(current_user)

    def play_game(self):
        '''
        Detect loss when guesses are finished
        Detect victory when a guess is correct
        '''
        while self.guesses_left > 0:
            self.guessed_word = self.get_guessed_word()
            self.get_hints()
            print(self.print_keyboard_state())
            if self.guessed_word.strip().lower() == self.word.strip().lower():
                print("You guessed the word!")
                wordle.wins += 1
                wordle.winstreak += 1
                if wordle.highscore == None or (self.guesses - self.guesses_left) < wordle.highscore:
                    wordle.highscore = (self.guesses+1 - self.guesses_left)
                store_current_run(current_user, wordle.wins, wordle.losses, wordle.highscore, wordle.winstreak)
                break
            self.guesses_left -= 1
        if self.guesses_left == 0:
            print("You lost! The word was", self.word)
            wordle.losses += 1
            wordle.winstreak = 0
            store_current_run(current_user, wordle.wins, wordle.losses, wordle.highscore, wordle.winstreak)

    def print_keyboard_state(self):
        '''
        takes a list of letters and prints the keyboard state with "#" for the letters that are in the list
        '''
        keyboard = "q w e r t y u i o p\n a s d f g h j k l\n  z x c v b n m\n"
        for letter in self.wrong_guessed_letters:
            keyboard = keyboard.replace(letter, "#")
        for letter in self.right_guessed_letters:
            keyboard = keyboard.replace(letter, letter.upper())
        for letter in self.half_right_guessed_letters:
            keyboard = keyboard.replace(letter, letter.upper())
        return keyboard

def main_menu():
    '''
    Prints the main menu
    '''
    print("\nWelcome to Wordle")
    print(f"username: {current_user}") # shows current user    
    print("\n   [Play game] : p")
    print("\n   [Change user] : c")
    print("\n   [Add word to word bank] : a")
    print("\n   [Quit] : q")

def game_menu():
    '''
    Prints the game menu
    '''
    print("\n[Return to main menu] : r")
    print("\n[See game history] : h")
    print("\n[Play another game] : y")
    print("\n[Quit] : any other key")

def play_game():
    '''
    Starts the game and asks the user for the word length and number of guesses.
    When the game is over the user is returned to the game menu
    '''
    # input validation for word length
    while True:
        length = input("Enter the length of the word you would like: ")
        if length.isdigit() and 1 <= int(length) <= 14:
            break
        print("Please enter a number between 1 and 14.")

    # input validation for number of guesses
    while True:
        guesses = input("Enter the number of guesses you would like: ")
        if guesses.isdigit() and 1 <= int(guesses) <= 100:
            break
        print("Please choose a number between 1 and 100.")

    print(f"\nYou have {int(guesses)} guesses to guess a {int(length)} letter word")
    print("Good luck\n")

    game = wordle(int(length), int(guesses))
    game.play_game()
    game_menu_choice()

def game_menu_choice():
    '''
    Asks the user if they want to return to the main menu, see the game history, play another game or quit
    '''
    game = wordle(int(), int())
    game_menu()
    choice = input("\nEnter your choice: ")
    if choice.lower() == "r":
        main_menu_choice()
    elif choice.lower() == "h":
        game.get_game_history()
        game_menu_choice()
    elif choice.lower() == "y":
        play_game()
        game_menu_choice()
    else:
        print("quitting...")
        exit()

def main_menu_choice(choice=""):
    '''
    Here the user can choose to play the game, add a word to the word bank, change user or quit
    '''
    global current_user

    game = wordle()
    main_menu()
    choice = input("\nEnter your choice: ")
    if choice == "p":
        play_game()
        game_menu_choice()
    elif choice == "a":
        word = input("Enter the word to add to the word bank: ")
        add_word_to_word_bank(word)
        main_menu_choice()
    elif choice == "q":
        exit()
    elif choice == "c":
        current_user = input("Enter your name: ")
        # reset the scores
        wordle.wins = 0
        wordle.losses = 0
        wordle.highscore = None
        wordle.winstreak = 0
        main_menu_choice()
    else:
        print("Invalid choice")
        main_menu_choice()


if __name__ == '__main__':
    words = store_word_bank()
    current_user = ""
    while True:
        main_menu_choice()

