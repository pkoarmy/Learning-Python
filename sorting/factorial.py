# Factorial in Python

def factorial(n):
   fac = 1
   for index in range(1, n + 1):
    #    print(index)
       fac = fac * index
       print(fac)

factorial(100)
