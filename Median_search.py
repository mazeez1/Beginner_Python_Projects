 
#Moses Azeez
 

def leftmostPivotSelection(list):
	leftmostPivot = list[0]
	return(leftmostPivot)


def bestofThreePivotSelection(list):
	lengthOfList = len(list)
	tripleOfList = lengthOfList / 3
	leftmostPivot = list[0]
	middlePivot = list[int(lengthOfList / 2)]
	rightmostPivot = list[lengthOfList-1]
	if (leftmostPivot > middlePivot and leftmostPivot < rightmostPivot) or (leftmostPivot > rightmostPivot and leftmostPivot < middlePivot):
		return leftmostPivot
	if (middlePivot > leftmostPivot and middlePivot < rightmostPivot) or (middlePivot > rightmostPivot and middlePivot < leftmostPivot):
		return middlePivot
	else:
		return rightmostPivot
#first < Second < third

def tripleValueMedian(x, y, z):
	if (x < y < z) or (x > y > z):
		return y
	if (y < x < z) or (y > x > z):
		return x
	return z

def nintherPivotSelection(list):
	lengthOfList = len(list)
	nintherOfList  = lengthOfList / 9
	leftmost = list[0]
	rightmost = list[int(lengthOfList-1)]
	first = nintherOfList * 1
	second = nintherOfList * 2
	third = nintherOfList * 3 
	fourth = nintherOfList * 4
	fifth = nintherOfList * 5
	sixth = nintherOfList * 6
	seventh = nintherOfList * 7
	groupOne = tripleValueMedian(leftmost, first, second)
	groupTwo = tripleValueMedian(third, fourth, fifth)
	groupThree = tripleValueMedian(sixth, seventh, rightmost)
	return int(tripleValueMedian(groupOne, groupTwo, groupThree))
	#finding list values

def quick_sort(lst, right, left, pivot):
    if pivot not in lst:
        raise ValueError('Given pivot doesn\'t exist in the list')
    rightList = []
    leftList = []

    # if start and end are the same, then for 1 element list it is sorted
    if right == left:
        return lst
    
    # if current list has more than 1 element, sort it into the bins
    if (len(lst) > 0):
        for i in range(left, right + 1):
            if lst[i] < pivot:
                leftList.append(lst[i])
            if lst[i] > pivot:
                rightList.append(lst[i])
                
    # recursively sort the bins

        if len(rightList) > 0:
            rightList = quick_sort(rightList, len(rightList)-1, 1, rightList[0])

        if len(leftList) > 0:
            leftList = quick_sort(leftList, len(leftList)-1, 0,leftList[0])
    # join the lists together with the pivot
    return leftList + [pivot] + rightList

    #Random numbers from 1-6

test1 =[ 20, 12, 3, 8, 11, 5, 17, 6, 30, 1, 4 ]



pivot9er = nintherPivotSelection(test1)
 







###Time testing#####
from time import time
from math import *
print('unsorted list',test1)

print("best of 9 pivot: ", pivot9er)

n = len(test1)
print("Length of list(n):", n)

# run the program this many times
repetition_count = int(input("Input rep count: "))

# start timer
time_start = time()

# loop with run time f(n) = Clog(n)
for rep in range( repetition_count ):

    hacer = quick_sort(test1,len(test1)-1,0,pivot9er)

# stop timer
time_end = time()

# time to run the program many times
time_many = time_end - time_start

# time to run the program once
time_once = time_many / repetition_count

# time to print a star (and newline)
C = time_once / log2( n )


print("")
print("")
print("total time:", time_many )
print( "n    ", n )
print( "time once ", format( time_once, ".3g" ) )
print( "C est", format( C, ".3g" ) )

Quick_C =6.10e-06
theory = (Quick_C * log2(n) * rep)
print("theory time", theory)

print('sorted list',hacer)



 
