#@title Random Password Generator

import random
import hashlib

def generate_list_in_character(min, max):
    temp = []
    for i in range(min, max):
        temp.append(chr(i))
    
    return temp

# please complete whole character list or generate it smartly
upper_char = generate_list_in_character(65, 91)
lower_char = generate_list_in_character(97, 123)
number_char = generate_list_in_character(48, 58)
special_char = generate_list_in_character(40, 47)

print(upper_char)
print(lower_char)
print(number_char)
print(special_char)

len_upper = len(upper_char)
len_lower = len(lower_char)
len_number = len(number_char)
len_special = len(special_char)
total_size_of_list = len_upper + len_lower + len_number + len_special
strong_password = []

def generate_password_randomly(index):
    temp = upper_char + lower_char + number_char + special_char

    return temp[index]

# using loop to generate 13 different index with random password
for i in range(13):
  index = random.randint(0, total_size_of_list - 1)
  strong_password.append(generate_password_randomly(index))

print( strong_password )

hash_ojb = hashlib.md5(str(strong_password).encode())
print(hash_ojb.hexdigest())
