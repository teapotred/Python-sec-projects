##try to make a password encryption program(simple ig)

import random
import string

chars= " " + string.punctuation+ string.digits + string.ascii_letters

chars= list(chars)

key= chars.copy()

random.shuffle(key)


#ENCRYPT

plain_text= input("Enter a message: ")
cipher_text = ""

for i in plain_text:
    index=chars.index(i)
    cipher_text += key[index]

print(f"original message:{plain_text}")
print(f"encrypted message: {cipher_text}")


#DECYPHER
decrypted_text=""

for i in cipher_text:
    new_index=key.index(i)
    decrypted_text += chars[new_index]

print(f"decrypted message: {decrypted_text}")

