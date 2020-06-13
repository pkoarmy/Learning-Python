grade = 6
if grade == 3 or 4 or 5:
    print("Elementary")
elif grade == 6 or 7 or 8:
    print("Middle")


A = True

B = False

print( not(A and B))


# 1..10
# I want to sum of 1 to 10
# what loop command is the best to implement this?

sum = 0
for i in range(1, 10):
    sum += i

print(sum)