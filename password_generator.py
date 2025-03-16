import random
import string

len = int(input("Enter the length of the password: "))

chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(len):
    password += random.choice(chars)

print(f"Your password is {password}")