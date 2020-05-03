# Indentation example

# import
import time
import random

print("Tell even/odd number")

for index in range(0, 10):
    random_number = random.randint(0, 10)
    print(random_number)
    random_number = random_number % 2
    if random_number > 0:
        print("Odd number")
    else:
        print("Even number")
    time.sleep(1)
