##########################################################################
#Programmed By:
#Moses Azez - MMA348
##########################################################################
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    
    result = []
    indA = 0
    indB = 0
    while (len(result) < len(left) + len(right)):
        if left[indA] < right[indB]:
            result.append(left[indA])
            indA+= 1
     
        else:
            result.append(right[indB])
            indB+= 1
          
        if indA == len(left) or indB == len(right):
            result.extend(left[indA:] or right[indB:])
            break
        
    return result

def mergesort(list):
    if len(list) < 2:
        return list

    middle = int(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    print(left)
    print(right)
    return merge(left, right)

###FOR TESTING###
from time import time

lst =[ 20, 12, 3, 8, 11, 5, 17, 6, 30, 1, 4 ]
print('unsorted list',lst)
print('sorted list',mergesort(lst))
###END TESTING###
