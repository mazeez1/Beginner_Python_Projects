# purpose: time both the functions

from math import*
# import time function
from time import time
repetition_count = int(input("Enter your n value: "))
print("")

#Create the list
python_list=[]
for i in range(0,5000):
    python_list.append(i)

#-----------------------------------------------------------------
#sequential search function

def sequential_Search( value, python_list):  

    for i in range( len( python_list ) ):    

        if python_list [ i ] == value:    
                                        
            return i

    return -1
#-------------------------------------------------------------------
# binary search function

def binary_search(val, python_list):
       l = 0
       r = (len(python_list)) - 1
       while l <= r: 
            m = int((l + r)/2)
            if python_list[m] == val:  
                     return m
            elif val < python_list[m]:
                 r = m - 1
            else:
             
             l = m + 1

   
       return (-1)

# ---------------------------------------------------------------------
# time the binary search

time_start = time()

for rep in range(repetition_count):

    index_of_val = binary_search(4999, python_list)

end_time = time()

time_all_reps = end_time - time_start
                     
print("time total(binary):", format(time_all_reps, ".3g"))
print("C est(Bin):", (time_all_reps)/(log(2)*repetition_count*5000))

print("")

#-----------------------------------------------------------------------
# time sequential search

time_start = time()

for rep in range(repetition_count):

    ind = sequential_Search(4999, python_list)
    
end_time = time()

time_all_reps = end_time - time_start
                     
print("time(sequential):", format(time_all_reps,".3g"))
print("C est(Seq):", ((time_all_reps/repetition_count)/5000))
print("")
#-------------------------------------------------------------------------
# time the python search function

time_start = time()

for rep in range(repetition_count):
     python_list.index(4999)
    
end_time = time()

time_all_reps = end_time - time_start
                     
print("time(python search):", format(time_all_reps, ".3g"))
print("C est(Py):",((time_all_reps/repetition_count)/5000))
print("")


