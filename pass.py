import random
import string

def generate_password(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(character)
    return password

print(generate_password(6))


"""
To be fixed

"""