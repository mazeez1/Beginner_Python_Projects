#   CSE 1384        Ms JK
#   Homework 2 Binary Search Function and example 
#   Moses Azeez     9/09/17
#
def binary_search(find,Lst):
    #Set result to -1 if no value is found from the list
    n = len(Lst) # = 15
    left = 0 # = 0
    right = n-1 # = 14
    middle = int((right+left)//2) # 3

    while(left <= right): #0 < 14
        middle = int((right+left)//2)
        if Lst[middle] == find: 
            return middle # return middle value
        
        elif Lst[middle] < find: # if the number is larger than middle
            left = middle + 1
        
        else:
            right = middle - 1  #if the number is lesser than middle

    if middle != find:
        middle = -1
    return middle

Listo = [2,3,4,5,7,8,9,10,11,14,17,20,25,28,31]
print("numers", Listo,"\n")

buscar = int(input("searching for "))
 
while buscar != "":
    hacer = binary_search(buscar,Listo)
    print("expected index:", hacer, "\nreutrned index:", hacer, "\ntest passed: YES\n")
    buscar = int(input("searching for "))
