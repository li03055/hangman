

def opening_screen():
    # print opening screen
    HANGMAN_ASCII_ART = '''Welcome to the game Hangman \n  _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/ \n'''
    MAX_TRIES = 6   # number of failed guesses
    print(HANGMAN_ASCII_ART + "You have %d failed guesses" % MAX_TRIES)


def is_valid_input(letter_guessed):
    # check if letter_guessed is one letter in english
    if len(letter_guessed) > 1 or (not letter_guessed.isalpha()) or (
            ord(letter_guessed.lower()) < 97 or ord(letter_guessed.lower()) > 122):
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    # check if letter_guessed is valid and if in old_letters_guessed
    if is_valid_input(letter_guessed) == False and letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # check if valid letter, if true then add to list, else print X and explain
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += letter_guessed
        return True
    else:
        print("X")
        sorted_letters = sorted(old_letters_guessed)
        sorted_letters = ' -> '.join(sorted_letters)
        print(sorted_letters)
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    # show if letters from list are in the secret_word
    space = "_ "
    after_guesses = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            after_guesses.append(letter)
        else:
            after_guesses.append(space)
    return ' '.join(after_guesses)      # turn list to str


def check_win(secret_word, old_letters_guessed):
    # check if player guessed the word correctly
    count_letters = 0   # count letters guessed, and if equals secret_word's length, return true
    for letter in secret_word:
        if letter in old_letters_guessed:
            count_letters += 1
    if count_letters == len(secret_word):
        return True
    else:
        return False


def print_hangman(num_of_tries):
    # print from dictionary, photos of hangman
    HANGMAN_PHOTOS = {1: "x-------x",
    2: "x-------x\n|\n|\n|\n|\n|",
    3: "x-------x\n|\n|\n|\n|\n|\n",
    4: "x-------x\n|       |\n|       0\n|       |\n|\n|",
    5: "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",
    6: "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",
    7: "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"}
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()    # words.txt in list from file
    num = len(words)    # num of words.txt in file
    unique_words = set(words)
    num_words = len(unique_words)   # num of unique_words
    if index > num_words:   # loop back to the beginning of the list of words.txt
        index = (index - 1) % num + 1
    secret_word = words[index]
    return (num_words, secret_word)




print(choose_word("words.txt", 10))
us = input("enter letter")
print(is_valid_input(us))
user_guess2 = input("Please enter a word: ")    # user's word



