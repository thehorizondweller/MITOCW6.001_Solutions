# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
#Note that the original SCRABBLE_LETTER_VALUES has been altered to add "*" with value 0
SCRABBLE_LETTER_VALUES = {
    '*':0,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    #Initialising points to zero
    points = 0
    #Transforming the input to lowercase
    word = word.lower()
    wordlen = len(word)
    #If the string is empty return the score as zero.
    if wordlen == 0:
        return points
    #Iterate through a loop to generate the first part of the score.
    for x in word:
        points = points + SCRABBLE_LETTER_VALUES[x]
    #Generate the second part of the score
    second_part = 7*wordlen - 3*(n-wordlen)
    #Calculating the final score
    if second_part < 0:
        second_part = 1
    points = points * second_part
    return points

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(math.ceil(n / 3)) - 1 #The 1 is subtracted to generate a free slot for the asterik or wildcard input

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand["*"] = 1 #Feeding in the wildcard in the dealt hand

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand_keys = hand.keys()
    new_hand = hand.copy()
    word = word.lower()
    for x in word:
        if x in hand_keys:
            if new_hand[x] > 0:
                new_hand[x] = new_hand[x] - 1

    final_hand = new_hand.copy()
    for x in new_hand:
        if new_hand[x] == 0:
            final_hand.__delitem__(x)

    return final_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    hand_keys = hand.keys()
    word = word.lower()
    word_dict = get_frequency_dict(word)

    # if "*" not in word:
    #     word_dict["*"] = 0

    if "*" not in word:
        for x in word:
            #The letter must be in the hand and its frequency count in the word should be less than or equal to that of that in the hand
            if x in hand_keys:
                if word_dict[x] > hand[x]:
                    return False
            else:
                return False
        #To ensure that thw word is in the worldlist
        if word not in word_list:
            return False

    if "*" in word:
        new_word = word.replace("*","")
        #First assert that the rest of the letters are valid and from the hand
        for x in new_word:
            #The letter must be in the hand and its frequency count in the word should be less than or equal to that of that in the hand
            if x in hand_keys:
                if word_dict[x] > hand[x]:
                    return False
            else:
                return False
        cntr = 0
        for x in VOWELS:
            new_word = word.replace("*",x)
            if new_word in word_list:
                #Keeps count of words that can be formed by replacing the asterik with a vowel
                cntr += 1

        if cntr == 0:
            return False

    return True


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    handlen = 0
    for x in hand.keys():
        handlen += hand[x]

    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """
    # Keep track of the total score
    total_score = 0

    while(calculate_handlen(hand)):
        display_hand(hand)
        word = input("Enter your word (or '!!' to end the hand): ")
        if word == "!!":
            print("Current Hand Score: ", total_score, " points")
            print("-------------------------------------------------")
            return total_score
        else:
            if is_valid_word(word, hand, word_list):
                total_score += get_word_score(word, HAND_SIZE)
                print("{} earned {} points. Current Hand Score: {} points.".format(word, get_word_score(word, HAND_SIZE), total_score))
            else:
                print("This is not a valid word. Please choose another word.")
            hand = update_hand(hand, word)
        print("\n")

    print("The current hand has come to an end. Total Current Hand Score: {} points".format(total_score))
    print("---------------------------------------------------------------------------------------------")
    return total_score

#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    #Prepare a list of the remaining letters other than the hand
    alphabet = VOWELS + CONSONANTS
    remainder_alphabet = []
    for char in alphabet:
        if char not in hand.keys():
            remainder_alphabet.append(char)
    #Choosing the new letter
    new_letter = random.choice(remainder_alphabet)

    if letter in hand.keys():
        hand[new_letter] = hand[letter]
        hand.__delitem__(letter)

    return hand




def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    #total score
    total_score = 0
    #Counter for substitute and Replaying
    subs,replay = 0,0

    print("WELCOME TO SCRABBLE!")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
    hand_num = int(input("Enter the number of hands you wish to play: "))
    print("---------------------------------------------\n")
    hand_cntr = 1

    print("Hand Number: ", hand_cntr)
    dealt_hand = deal_hand(HAND_SIZE)
    print("Current Hand: ", end ='')
    display_hand(dealt_hand)
    subs_choice = input("Do you want to substitute a letter? Type yes or no: ")
    subs_choice = subs_choice.lower()
    if subs_choice == "yes":
        subs = 1
        letter = input("Which letter do you wish to substitute?: ")
        dealt_hand = substitute_hand(dealt_hand, letter)
    score_of_hand = play_hand(dealt_hand,word_list)
    total_score += score_of_hand
    print("Total Game Score: ", total_score)
    hand_num -= 1

    #Loop for hands
    while(hand_num):
        if replay < 1:
            replay_choice = input("Do you want to replay the last hand? Type yes or no: ")
            replay_choice = replay_choice.lower()
            if replay_choice == "yes":
                replay = 1
                print("Hand Number: ", hand_cntr)
                print("Current Hand: ", end ='')
                display_hand(dealt_hand)
                if subs < 1:
                    subs_choice = input("Do you want to substitute a letter? Type yes or no: ")
                    subs_choice = subs_choice.lower()
                    if subs_choice == "yes":
                        subs = 1
                        letter = input("Which letter do you wish to substitute?: ")
                        dealt_hand = substitute_hand(dealt_hand, letter)
                new_score_of_hand = play_hand(dealt_hand,word_list)
                if new_score_of_hand > score_of_hand:
                    total_score = total_score + (new_score_of_hand - score_of_hand)
                print("Total Game Score: ", total_score)

        hand_cntr += 1
        print("Hand Number: ", hand_cntr)
        dealt_hand = deal_hand(HAND_SIZE)
        print("Current Hand: ", end ="")
        display_hand(dealt_hand)
        if subs < 1:
            subs_choice = input("Do you want to substitute a letter? Type yes or no: ")
            subs_choice = subs_choice.lower()
            if subs_choice == "yes":
                subs = 1
                letter = input("Which letter do you wish to substitute?: ")
                dealt_hand = substitute_hand(dealt_hand, letter)
        score_of_hand = play_hand(dealt_hand, word_list)
        total_score += score_of_hand
        print("Total Game Score: ", total_score)

        hand_num -= 1

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
