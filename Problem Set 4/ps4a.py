# Problem Set 4A
# Name: KSHITIJ ANAND
# Collaborators: NILS
# Time Spent: x:xx

def get_permutations(seq):
    '''
    Enumerate all permutations of a given string

    seq (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of seq

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    seq_length = len(seq)
    #The list container for the final result
    permutations_list = []
    #Base Cases when seq Length is 0 or 1
    if seq_length <= 1:
        permutations_list.append(seq)
        return permutations_list
    #The recursive definition
    else:
        remainder_seq = seq[1:] #Stripping off the first letter
        permutations_of_rem_seq = get_permutations(remainder_seq) #Call the function recursively
        for x in  permutations_of_rem_seq:
            x_len = len(x)
            first_letter = seq[0]
            for y in range(x_len+1):
                new_permutation_added = x[:y] + first_letter + x[y:] #Placing the first letter at different locations
                permutations_list.append(new_permutation_added)
        return permutations_list




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    seq of length n)

    # example_input_1 = 'cat'
    # print('Input: ', example_input_1)
    # print('Expected Output: ', ['cat', 'act', 'atc', 'cta', 'tca', 'tac'] )
    # print('Actual Output: ', get_permutations('cat'))
    #
    # example_input_2 = 'dog'
    # print('Input :', example_input_2)
    # print("Expected Output : ", ['dog', 'odg', 'ogd', 'dgo', 'gdo', 'god'] )
    # print("Actual Output: ", get_permutations("dog"))
    #
    # example_input_3 = "myth"
    # print("Input: ", example_input_3)
    # print("Expected Output: ", ['myth', 'ymth', 'ytmh', 'ythm', 'mtyh', 'tmyh', 'tymh', 'tyhm', 'mthy', 'tmhy', 'thmy', 'thym', 'myht', 'ymht', 'yhmt', 'yhtm', 'mhyt', 'hmyt', 'hymt', 'hytm', 'mhty', 'hmty', 'htmy', 'htym'])
    # print("Actual Output: ". get_permutations("myth"))

    list = get_permutations('myth')
    print(list)
