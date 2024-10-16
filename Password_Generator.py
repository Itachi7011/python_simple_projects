import random

import string


def generate_password(length):

    all_characters = string.ascii_letters + string.digits + string.punctuation

    if length < 8:

        print("Password length should be at least 8 characters.")

        return None

    password = ''.join(random.choice(all_characters) for i in range(length))

    return password


length = int(input("Enter The Length Of The Password (Atleast 8): "))

print("Unique Generated Password : ", generate_password(length))