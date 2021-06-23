# Fibonacci Sequence
# ======================

# ask the user how many terms to compute
n = int( input( "How many Fibonacci terms do you want? " ) )

# first two terms of the Fib sequence
f0 = 0
f1 = 1
print( "0\n1" )

# compute the rest of the Fib sequence
f_im2 = f0
f_im1 = f1

for i in range( 2, n, 1 ):

    # compute and print current Fib term
    f_i = f_im2 + f_im1
    print( f_i )

    # update previous two Fib terms
    f_im2 = f_im1
    f_im1 = f_i
