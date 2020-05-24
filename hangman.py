# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_set = set(secret_word)
    secret_word_set_len = len(secret_word_set)
    counter = 0
    for char in secret_word_set:
        if char in letters_guessed:
            counter += 1
        else: pass
    if counter == secret_word_set_len:
        return True
    else:
        return False





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guess_list =[]
    for char in secret_word:
        if char in letters_guessed:
            guess_list.append(char)
        else:
            guess_list.append("_ ")
    guessed_so_far = ''.join(guess_list)
    return guessed_so_far



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    all_letters_list = list(all_letters)
    for char in letters_guessed:
        all_letters_list.remove(char)
    return ''.join(all_letters_list)

def valid_input_checker(guessed_letter):
    all_letters = string.ascii_lowercase
    all_letters_caps = string.ascii_uppercase
    all = all_letters + all_letters_caps
    if len(guessed_letter)==1 :
        if guessed_letter in all:
            return True
        else:
            return False
    else:
        return False



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    print("***************************************************************")
    print("Welcome to the Hangman Game.")
    print("You start with 6 guesses and 3 warnings.")
    print("You loose 1 guess for a consonant guessed not present in the secret word and 2 guesses for a vowel not present in the secret word.")
    print("You loose 1 warning in case you enter an invalid input i.e. which is not a letter or more than one letter, and if you guess an already guessed letter.")
    print("On losing all warnings, you shall loose 1 guess additionally henceforth.")
    print("Let's begin the game!")
    print("I am thinking of a {} letter long word.".format(len(secret_word)))
    print("****************************************************************")
    letters_guessed = []
    while (not is_word_guessed(secret_word,letters_guessed) and guesses>0):
        print("You have {} guesses and {} warnings left.".format(guesses, warnings))
        print("Available Letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter:")
        if valid_input_checker(guessed_letter):
            guessed_letter = guessed_letter.lower()
            if guessed_letter not in letters_guessed:
                letters_guessed.append(guessed_letter)
                if guessed_letter in secret_word:
                    print("Good Guess.")
                    print("Your progress:", get_guessed_word(secret_word,letters_guessed))
                else:
                    print("Oops! Your guessed letter is not in the word.")
                    if guessed_letter in 'aeiou':
                        guesses -= 2
                    else:
                        guesses -= 1

            else:
                if warnings > 0:
                    warnings -= 1
                    print("Oops! That was a repeated attempt, and you lost a warning.")


        else :
            if warnings > 0:
                warnings -= 1
                print("Oops! That was an invalid input, and you lost a warning.")
            else:
                guesses -= 1
                print("Oops! That was an invalid input, and you ran out of warnings and now you lost a guess.")
        print("-----------------------------------------------------------------")

    result = is_word_guessed(secret_word, letters_guessed)
    if result and guesses>0:
        print("Congratulations! You have guessed the word correctly and the word is ",secret_word," .")
        print("Your total score is {}.".format(guesses*len(set(secret_word))))
    else:
        print("Oops! GAME OVER! Better Luck Next Time! :-) ")
        print("The word was {}.".format(secret_word))





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word_new = ''.join(my_word.split()) #Removes all white spaces
    my_word_len = len(my_word_new)
    other_word_len = len(other_word)

    if my_word_len == other_word_len :
        my_word_new_2 = my_word_new.replace("_","")
        counter = 0;
        position = 0;
        my_word_new_2_len = len(my_word_new_2)
        for char in my_word_new:
            if char == "_":
                skipped_char = other_word[position]
                if skipped_char in my_word_new:
                    return False
            else:
                if char ==  other_word[position]:
                    counter += 1
                else:
                    pass
            position += 1

        if counter == my_word_new_2_len:
            return True

        else :
            return False
    else :
        return False




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end = "  ")

    return None



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    print("***************************************************************")
    print("Welcome to the Hangman Game.")
    print("You start with 6 guesses and 3 warnings.")
    print("You loose 1 guess for a consonant guessed not present in the secret word and 2 guesses for a vowel not present in the secret word.")
    print("You loose 1 warning in case you enter an invalid input i.e. which is not a letter or more than one letter, and if you guess an already guessed letter.")
    print("On losing all warnings, you shall loose 1 guess additionally henceforth.")
    print("For Hints: You can enter an asterik to get a list of probable words. You can use this power only twice.")
    print("Let's begin the game!")
    print("I am thinking of a {} letter long word.".format(len(secret_word)))
    print("****************************************************************")
    letters_guessed = []
    asterik_counter = 0
    while (not is_word_guessed(secret_word,letters_guessed) and guesses>0):
        print("You have {} guesses and {} warnings left.".format(guesses, warnings))
        print("Available Letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter:")
        if guessed_letter == "*":
            asterik_counter += 1
            if asterik_counter <= 2:
                my_word = get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(my_word)
                print("\n")
                print("-------------------------------------------------------------")
            else :
                print("Sorry! You have already taken hints twice. Try again!")
                print("--------------------------------------------------------------")
                continue

        else:
            if valid_input_checker(guessed_letter):
                guessed_letter = guessed_letter.lower()
                if guessed_letter not in letters_guessed:
                    letters_guessed.append(guessed_letter)
                    if guessed_letter in secret_word:
                        print("Good Guess.")
                        print("Your progress:", get_guessed_word(secret_word,letters_guessed))
                    else:
                        print("Oops! Your guessed letter is not in the word.")
                        if guessed_letter in 'aeiou':
                            guesses -= 2
                        else:
                            guesses -= 1

                else:
                    if warnings > 0:
                        warnings -= 1
                        print("Oops! That was a repeated attempt, and you lost a warning.")

            else :
                if warnings > 0:
                    warnings -= 1
                    print("Oops! That was an invalid input, and you lost a warning.")
                else:
                    guesses -= 1
                    print("Oops! That was an invalid input, and you ran out of warnings and now you lost a guess.")
            print("-----------------------------------------------------------------")

    result = is_word_guessed(secret_word, letters_guessed)
    if result and guesses>0:
        print("Congratulations! You have guessed the word correctly and the word is ",secret_word," .")
        print("Your total score is {}.".format(guesses*len(set(secret_word))))
    else:
        print("Oops! GAME OVER! Better Luck Next Time! :-) ")
        print("The word was {}.".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
