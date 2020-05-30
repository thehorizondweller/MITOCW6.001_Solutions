from ps4b import *

#test for build_shift_dict
print("Testing for build_shift_dict: \n")
my_message = Message("KSHITIJ")
shifted_dict = my_message.build_shift_dict(1)
print(shifted_dict)
print("SUCCESS")
print("-------------------------")

print("Testing for apply_shift(): ")
my_message = Message("AbC")
shift = 2
encoded_message = my_message.apply_shift(shift)
if encoded_message == "CdE":
    print("SUCCESS")
else:
    print("FAILURE")
print("---------------------------")

print("Testing for the functions of PlanetextMessage: ")
my_message = PlaintextMessage("AbC", 2)
shift = my_message.get_shift()
encry_dict = my_message.get_encryption_dict()
encry_message = my_message.get_message_text_encrypted()
print("Shift is :" ,shift)
print("Encryption Dictionary is: ",encry_dict)
print("Encrypted Message is: ", encry_message)
my_message.change_shift(1)
shift = my_message.get_shift()
encry_dict = my_message.get_encryption_dict()
encry_message = my_message.get_message_text_encrypted()
if shift == 1 :
    print("Shift is :" ,shift)
    print("Encryption Dictionary is: ",encry_dict)
    print("Encrypted Message is: ", encry_message)
    print("SUCCESS")
else:
    print("FAILURE")
print("__________________________________________")

print("Testinf for CiphertextMessage:")
encrypted_message = CiphertextMessage("Nz obnf jt Hpe.")
s , m = encrypted_message.decrypt_message()
if s == 1:
    print("The best shift value is {} and the decrypted message is - {}.".format(s,m))
else:
    print("FAILURE.")
print("_________________________________________________")
