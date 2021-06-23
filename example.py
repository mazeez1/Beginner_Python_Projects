from time import time
from math import log2

# print the powers of 2, starting with 2^1

n = int( input( "enter power of 2, n: " ) )

# run the program this many times
repetition_count = 100

# start timer
time_start = time()

# loop with run time f(n) = Clog(n)
for rep in range( repetition_count ):

    first_value = n;
    value = first_value

    while value >= 2:
        print( "*" )
        value = value / 2

# stop timer
time_end = time()

# time to run the program many times
time_many = time_end - time_start

# time to run the program once
time_once = time_many / repetition_count

# time to print a star (and newline)
C = time_once / log2( n )

print( "n    ", n )
print( "time ", format( time_once, ".3g" ) )
print( "C est", format( C, ".3g" ) )
