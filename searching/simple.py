def Search(list, hay):
    for i in range (len(list)):
        if list[i] == hay:
            return i
    return -1


def Search2(list, hay):
    first = 0
    last = len(list)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if list[mid] == hay:
            index = mid
        else:
            if hay<list[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(Search([1,2,3,4,5,2,1], 2))

print(Search2([10,20,30,40,50], 30))


