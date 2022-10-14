import random
from random import sample
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

rand_up = random.choice(uppercase)
rand_lo = random.choice(lowercase)
rand_num = random.choice(numbers)
rand_sy = random.choice(symbols)


print("\n\n\t\tWelcome to Password Generator!\n\n")
len_of_pass = int(input("Enter the length of the password: "))

len_of_4 = uppercase+lowercase+numbers+symbols
four = rand_up + rand_lo + rand_num + rand_sy

store_here = random.sample(len_of_4+four, len_of_pass)
password = "".join(store_here)

x = 30
y = 4

if len(password) <= x and len(password) >= y:
    print("\nPassword: ", password)
    print('\n')

elif len(password) < y:
    print("\nPassword length should be greater than 4\n")

else:
    print("\nPassword length should be lesser than 30\n")
