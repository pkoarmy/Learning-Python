def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r

month=1
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")



if month > 0 and month < 4:
    print("Spring")

names = ['Ray', 'Chris', 'Amy', 'Mary', 'Human']
scores = []
scores.append(97)
scores.append(98)
print(names)
print(scores)
print(scores[1])

for name in names:
    print("Hi", name)

for index in range(0, 2):
    print(index)

names = ['Chris', 'Susan', ]
index = 0
while index < len(names):
    print(names[index])
    index = index + 1

def say(name):
    print("hi", name)

say("Ray")
say("Chris")


# # game level 1
# clear the screen
# goto (x, y)
# print("hi")
# print("welcome to level1")

# # game level 2
# clear the screen
# goto (x, y)
# print("hi")
# print("welcome to level2")

# # game level 3
# clear the screen
# goto (x, y)
# print("hi")
# print("welcome to level3")

# def level(index):
#     clean the screen
#     goto(x, y)
#     print ( "hi")
#     print("welcome to level")
#     if current_level == 1:
#         print("1:)
        

# level(1)
# level(2)
# level(3)


def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your initiail are: ' + get_initial(first_name) + get_initial(last_name) )