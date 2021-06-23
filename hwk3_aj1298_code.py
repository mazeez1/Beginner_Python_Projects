from time import time
from random import randint

alist = []
for i in range (0, 5000):
    alist.append(randint(0, 5000))
n=len(alist)


def insertionsort(alist):
    flag = False
    sorted_list = [alist[0]]
    for index in range(1, len(alist)):# changed numbers here
 
        value = alist[index]
        
        for ind in range(0, len(sorted_list)):
            if value < sorted_list[ind]:
                sorted_list.insert(ind, value)
                flag = True
                break

        if not flag:    
            sorted_list.append(value)

        flag = False
    return sorted_list

        

#-----------------timing------------------

repetition_count = 1

time_start = time()

for index in range ( repetition_count ):
    insertionsort(alist)

time_end = time()
time_all_reps = time_end - time_start
time_one_rep = time_all_reps / repetition_count
C= 2.73e-08
theory = (C * n*n * repetition_count)
print("total time:", time_all_reps)
print('time once:', format(time_one_rep, '.3g'))
print('C est:', format (C, '.3g'))
print('theory time:', theory)

#----------------------------------------------------------------------
# list length       single sort time     comparison time (C estimate)     
#    12000               2.2                         1.53e-08 
#    14000               2.51                        1.28e-08           
#    16000               3.18                        1.24e-08                      
#    18000               4.07                        1.26e-08           
#    20000               6.02                        1.51e-08

                                              #C average: 1.4e-08






