# https://github.com/pkoarmy/Learning-Python/blob/master/week1/indent1.py

import random

print("We are going to calculate season from given Month")
print("We call Spring if the month between March and May")
print("We call Jun - Aug as Summer")
print("We call Sep - Nov as Fall")
print("We call Dec - Feb as Winter")

month = random.randint(1, 12)

print("current month is ", month)
print("So it is")

# You remember this code what we learned on our class
'''
if month == 1:
   print("January")
elif month == 2:
   print("February")
elif month == 3:
   print("March")
'''

# please complete the Python code to print out what is the season from month
# hint : you can use logical operator with if clause
if month >= 3 and month <=5:
   print("Spring")
elif month >= 6 and month <= 8:
   print("Summer")
elif month >= 9 and month <= 11:
   print("Fall")
elif month == 12 or month < 3:
   print("Winter")
