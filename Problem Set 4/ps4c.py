# Problem Set 4C
# Name: Kshitij Anand
# Collaborators: NIL
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
WORD_LIST = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = WORD_LIST

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        #To ensure a smooth mapping
        upper_vowel_permutation = vowels_permutation.upper()
        lower_vowel_permutation = vowels_permutation.lower()

        transpose_dict = {}
        lower_i = 0
        for x in VOWELS_LOWER:
            transpose_dict[x] = lower_vowel_permutation[lower_i]
            lower_i += 1

        upper_i = 0
        for x in VOWELS_UPPER:
            transpose_dict[x] = upper_vowel_permutation[upper_i]
            upper_i += 1

        consonant_i = 0
        CONSONANTS = CONSONANTS_LOWER+CONSONANTS_UPPER
        for x in CONSONANTS:
            transpose_dict[x] = CONSONANTS[consonant_i]
            consonant_i += 1

        return transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''
        message_text_copy = self.message_text[:]
        #We use enumeration in place of str.replace because replace changes all instances at once.
        message_enu_list = list(enumerate(message_text_copy)) # COntains position information
        return_list =[] #helps in creating a final list since tuples are immutable
        VOWELS = VOWELS_LOWER + VOWELS_UPPER

        for x,y in message_enu_list:
            if y in VOWELS:
                return_tuple = (x, transpose_dict[y])
                return_list.append(return_tuple)
            else:
                return_tuple = (x, y)
                return_list.append(return_tuple)

        final_encrypted_message = ''
        for x in return_list:
            final_encrypted_message += x[1]

        return final_encrypted_message






class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        '''
        #generating all permutations possible with vowels in lowercase letters
        possible_vowel_permutation = get_permutations("aeiou")

        #Counter for maxiumum valid Words
        maximum_valid_words = 0
        final_deciphered_message = ''

        for perm in possible_vowel_permutation:
            #Construct a transpose dictionary for each permutation
            dict_for_perm = SubMessage.build_transpose_dict(self, perm)
            #Derived a decrypted form
            decrypted_message_for_perm = SubMessage.apply_transpose(self, dict_for_perm)
            #Generating a list of words
            decrypted_message_list = decrypted_message_for_perm.split(' ')
            temp = 0
            for word in decrypted_message_list:
                if is_word(WORD_LIST, word):
                    temp += 1
            #Updating maximum valid words
            if maximum_valid_words < temp:
                maximum_valid_words = temp
                final_deciphered_message = decrypted_message_for_perm

        if maximum_valid_words < 1:
            return self.message_text
        else:
            return final_deciphered_message





if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
