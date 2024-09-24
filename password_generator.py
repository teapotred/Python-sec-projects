import random
import string


def password_generator(length: int=10):
    alphabet = string.ascii_letters+string.digits+string.punctuation
    password = "".join(random.choice(alphabet) for i in range(length))
    return password

print(f"password: {password_generator()}")