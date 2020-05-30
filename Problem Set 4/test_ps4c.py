from ps4c import *
import sys

#GLOBALLY DEFINED VOWEL permutations
vowels_permutation = "eioua"
vowels_permutation_upper = "EIOUA"

#Test for build_transpose_dict
print("Testing build_transpose_dict(): ")
my_message_1 = SubMessage('')
transpose_dict = my_message_1.build_transpose_dict(vowels_permutation)
print("The transpose dictionary formed is: ")
print(transpose_dict)
cntr = 0
for x in VOWELS_LOWER:
    if transpose_dict[x] != vowels_permutation[cntr]:
        print("FAILURE")
        sys.exit()
    cntr += 1

upper_cntr = 0
for x in VOWELS_UPPER:
    if transpose_dict[x] != vowels_permutation_upper[upper_cntr]:
        print("FAILURE")
        sys.exit()
    upper_cntr += 1

print("SUCCESS")
print("_________________________________________________________________________")

#Test for apply_transpose()
print("Test for apply_transpose() function: ")
my_message_1 = "Tyler will be delivering the mail with Miss Evergarden today. She is very excited!"
sub_message_1 = SubMessage(my_message_1)
transpose_dict_1 = sub_message_1.build_transpose_dict(vowels_permutation)
transposed_message = sub_message_1.apply_transpose(transpose_dict_1)
expected_transposed_message = "Tylir woll bi dilovirong thi meol woth Moss Ivirgerdin tudey. Shi os viry ixcotid!"
print(transpose_dict_1)
print(transposed_message)
if transposed_message == expected_transposed_message:
    print("SUCCESS")
else:
    print("FAILURE")

print("__________________________________________________________________________")

#Test for decryption
print("Testing for decryption: ")
encrypted_message = EncryptedSubMessage(expected_transposed_message)
decrypted_message = encrypted_message.decrypt_message()
print("The best decrypted message is: ")
print(decrypted_message)
print("__________________________________________________________________________")
