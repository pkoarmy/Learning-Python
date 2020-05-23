def fib(num):
    # First two fibonacci numbers are 1
    if num == 1 or num == 2:
        return 1
    # Return the sum of the last two fibonacci numbers
    return fib(num-1) + fib(num-2)


# Output the first 10 numbers
for n in range(1, 31):
    print("fib(", n, ") =", fib(n))
