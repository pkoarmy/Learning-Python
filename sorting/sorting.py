# Sort in Python

def sort(array):
   # run loops two times: one for walking through the array
   # and the other for comparison
   for i in range(len(array)):
       for j in range(0, len(array) - i - 1):

           # To sort in descending order, change > to < in this line.
           if array[j] > array[j + 1]:
              
               # swap if greater is at the rear position
               (array[j], array[j + 1]) = (array[j + 1], array[j])


data = [7, 3, 22, 11, 17, 5, 19]
sort(data)
print('Sorted List in Ascending Order:')
print(data)


# Sort in Python

data = [7, 3, 22, 11, 17, 5, 19]
print(data)
print('Sorted List in Ascending Order:')
data.sort()
print(data)
