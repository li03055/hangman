import sys

MAX_TRIES = 6   # number of failed guesses

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
    print(HANGMAN_ASCII_ART + "You have %d failed guesses" % MAX_TRIES)


def is_valid_input(letter_guessed):
    # check if letter_guessed is one letter in english
    if len(letter_guessed) != 1 or not letter_guessed.isalpha() :
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    # check if letter_guessed is valid and if in old_letters_guessed
    if is_valid_input(letter_guessed) == False:
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    # check if valid letter, if true then add to list, else print X and explain
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        if letter_guessed in old_letters_guessed:
            print("You already guessed that letter", ' -> '.join(sorted(old_letters_guessed)))
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
    3: "x-------x\n|\n|\n|\n|\n|\n-",
    4: "x-------x\n|       |\n|       0\n|       |\n|\n|",
    5: "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",
    6: "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",
    7: "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"}
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    # choose word from file and set the secret_word
    try:
        with open(file_path, 'r') as f:
            words = f.read().split()    # words.txt in list from file
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found")
        sys.exit(1)  # Exit program with error code 1
    unique_words = set(words)
    num_words = len(unique_words)   # num of unique_words
    word_index = (index - 1) % len(words)
    secret_word = words[word_index]
    return (num_words, secret_word)


def main():
    opening_screen()
    file_path = input("Enter file path: ")
    index = int(input("Enter random index: "))
    tuple_words = choose_word(file_path, index)
    secret_word = tuple_words[1]
    old_letters_guessed = []    # list of letters the player guesses
    num_of_tries = 0    # num of failed guesses
    while not check_win(secret_word,old_letters_guessed) and num_of_tries < MAX_TRIES:
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input("Enter a letter: ")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word and is_valid_input(letter_guessed):
                num_of_tries += 1
                print_hangman(num_of_tries)

    if check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("You won!")
    else:
        print_hangman(MAX_TRIES)
        print(f"You lost :( The word was '{secret_word}'")


if __name__ == "__main__":
    main()




