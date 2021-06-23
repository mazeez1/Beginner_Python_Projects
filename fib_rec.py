# Fibonacci Sequence
# ======================



# function: fibonacci
# parameters: i - current term index or subscript
#             f_im2 - two terms back
#             f_im1 - one term back
# returns: nothing
#
# purpose: print the i'th Fibonacci term, up to the n-1'th term
#           where n is the desired number of terms, i starts at 2
def fibonacci( i, f_im2, f_im1 ):

    # stop when enough terms have been printed
    if i >= n:
        return

    # compute and print the current Fibonacci term
    f_i = f_im2 + f_im1
    print( f_i )

    # update the previous two terms
    f_im2 = f_im1
    f_im1 = f_i

    # recurse
    fibonacci( i+1, f_im2, f_im1 )

# ----------------------------------------------
# main program

# ask the user how many terms to compute
n = int( input( "How many Fibonacci terms do you want? " ) )

# first two terms of the Fibonacci sequence
F0 = 0
F1 = 1
print( "0\n1" )

# compute and print the rest of the Fibonacci sequence
F_im2 = F0
F_im1 = F1

fibonacci( 2, F_im2, F_im1 )

