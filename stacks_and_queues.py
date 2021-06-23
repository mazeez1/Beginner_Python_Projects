# CSE 1384 Hwk 6 Stack and Queues
# Fall 2017
#
# Grading Program
#


# change the module name when grading

from hwk_6_MC3146_module import *


# ----------------------------------------
# show a question, return 'y' or 'n'
def get_yes_no( question ):

    msg = question + " (y/n): "

    answer = input( msg )
    answer = answer.lower()
    while answer != 'y' and answer != 'n':
        print( "please type y or n" )
        answer = input( msg )
        answer = answer.lower()

    return answer


# ========================================
# grading tests


score = 0

deductions = []


# ----------------------------------------
# create/print stack LL

print( "\n-----------------------------------" )
print( "create/print empty stack LL" )
worth = 0.25

try:
    stack = stack_LL_class()
    print( stack )
    print( "" )
    
    print( "passed" )
    score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to create/print empty stack LL"
    deductions.append( s )

# ----------------------------------------
# length of empty stack LL

print( "\n-----------------------------------" )
print( "length of empty stack LL" )
worth = 0.25

try:
    length = len( stack )
    print( "expect: 0" )
    print( "actual:", length, "\n" )

    if length == 0:
        print( "passed" )
        score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to get length of empty stack LL"
    deductions.append( s )

# ----------------------------------------
# pop empty stack LL

print( "\n-----------------------------------" )
print( "pop empty stack LL" )
print( "must have error message, no raising exceptions" )
print( "stack must remain valid after failed pop" )
worth = 0.25 # x2

try:
    print( "" )
    value = stack.pop()
    print( "" )

    part2 = True

except Exception as problem:
    print( "FAILED" )
    s = "-" + str(2*worth) + " exception occured during pop of empty stack LL"
    deductions.append( s )
    part2 = False

if part2:
  try:      
    answer = get_yes_no( "Did you see an error message?" )
    if answer != 'y':
        raise Exception
    score += worth
  except:
    print( "\nFAILED" )
    s = "-" + str(worth) + " error msg missing: pop of empty stack LL"
    deductions.append( s )

if part2:
  try:
    print( "\nexpect length: 0" )
    length = len( stack )
    print( "actual length:", length )
    if length != 0:
        raise Exception

    print( "\n", stack, "\n", sep="" )
    answer = get_yes_no( "Does the empty stack look valid?" )
    if answer == 'y':
        score += worth
    else:
        raise Exception
    print( "\npassed" )
    
  except Exception as problem:
    print( "\nFAILED", problem )
    s = "-" + str(worth) + " invalid stack after pop of empty stack LL"
    deductions.append( s )

# ----------------------------------------
# push 3 things onto empty stack LL

print( "\n-----------------------------------" )
print( "push 3 things onto new empty stack LL" )
worth = 0.5

try:
    part2 = False

    print( "creating new empty stack" )
    stack = stack_LL_class()

    print( "pushing 10, then 20, then 30" )
    stack.push( 10 )
    stack.push( 20 )
    stack.push( 30 )

    part2 = True

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " exception occurred while pushing onto new stack LL"
    deductions.append( s )

if part2:
    try:

        print( "" )
        print( "stack ends should be labeled top and bottom" )
        print( "10 should be at the bottom" )
        print( "20 should be in the middle" )
        print( "30 should be at the top" )
        print( "" )
        print( stack )
        print( "" )

        answer = get_yes_no( "Does the stack look valid?" )
        if answer != 'y':
            raise Exception
        else:
            score += worth
            print( "\npassed" )

    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " stack LL does not look valid after 3 pushes"
        deductions.append( s )

# ----------------------------------------
# stack LL length after 3 pushes

print( "\n-----------------------------------" )
print( "get length of stack LL after 3 pushes" )
worth = 0.5

try:

    length = len( stack )

    print( "\nexpect length: 3" )
    print( "actual length:", length )

    if length != 3:
        raise Exception
    else:
        score += worth
        print( "\npassed" )
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " wrong stack LL length after 3 pushes"
    deductions.append( s )

# ----------------------------------------
# pop values off a stack LL

print( "\n-----------------------------------" )
print( "pop values off a stack LL\n" )
worth = 0.5 # x3

try:
    error_msg = "exception during stack LL pop"

    print( "creating new stack LL" )
    stack = stack_LL_class()

    print( "push 5, push 6, push 7\n7 should be on top of the stack" )
    stack.push( 5 )  # btm
    stack.push( 6 )
    stack.push( 7 )  # top

    print( "popping value off stack" )
    value = stack.pop()

    print( "\nexpect value: 7", type(7) )
    print( "actual value:", value, type(value), "\n" )

    if value != 7:
        error_msg = "1 pop, wrong value popped off stack LL" 
        raise Exception

    print( "expect length: 2" )
    length = len( stack )
    print( "actual length:", length, "\n" )

    if length != 2:
        error_msg = "1 pop, incorrect length after popping stack LL"
        raise Exception

    print( "btm should be 5" )
    print( "top should be 6" )
    print( "there should be no 7\n" )
    print( stack )
    print( "" )

    answer = get_yes_no( "Does the stack look valid?" )
    if answer != 'y':
        error_msg = "invalid stack LL after pop"
        raise Exception

    print( "popping two more values" )

    value = stack.pop()
    value = stack.pop()

    print( "\nexpect value: 5" )
    print( "actual value:", value, "\n" )
    
    if value != 5:
        error_msg = "3 pops, wrong value popped off stack LL" 
        raise Exception

    print( "expect length: 0" )
    length = len( stack )
    print( "actual length:", length, "\n" )

    if length != 0:
        error_msg = "3 pops, incorrect length after popping stack LL"
        raise Exception

    print( "the stack should be empty\n" )
    print( stack )
    print( "" )

    answer = get_yes_no( "Does the stack look empty?" )
    if answer != 'y':
        error_msg = "invalid stack LL after 3 pops, should be empty"
        raise Exception    
    
    print( "\npassed" )
    score += 3*worth

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(3*worth) + " " + error_msg
    deductions.append( s )

# ========================================
# create/print queue LL

print( "\n-----------------------------------" )
print( "create/print empty queue LL" )
worth = 0.25

try:
    queue = queue_LL_class()
    print( queue )
    print( "" )
    
    print( "passed" )
    score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to create/print empty queue LL"
    deductions.append( s )

# ----------------------------------------
# length of empty queue LL

print( "\n-----------------------------------" )
print( "length of empty queue LL" )
worth = 0.25

try:
    length = len( queue )
    print( "expect: 0" )
    print( "actual:", length, "\n" )

    if length == 0:
        print( "passed" )
        score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to get length of empty queue LL"
    deductions.append( s )

# ----------------------------------------
# dequeue empty queue LL

print( "\n-----------------------------------" )
print( "dequeue empty queue LL" )
print( "must have error message, no raising exceptions" )
print( "queue must remain valid after failed dequeue" )
worth = 0.25 # x2

try:
    print( "" )
    value = queue.dequeue()
    print( "" )

    part2 = True

except Exception as problem:
    print( "FAILED" )
    s = "-" + str(2*worth) + " exception occured during dequeue of empty queue LL"
    deductions.append( s )
    part2 = False

if part2:
  try:      
    answer = get_yes_no( "Did you see an error message?" )
    if answer != 'y':
        raise Exception
    score += worth
  except:
    print( "\nFAILED" )
    s = "-" + str(worth) + " error msg missing: dequeue of empty queue LL"
    deductions.append( s )

if part2:
  try:
    print( "\nexpect length: 0" )
    length = len( queue )
    print( "actual length:", length )
    if length != 0:
        raise Exception

    print( "\n", queue, "\n", sep="" )
    answer = get_yes_no( "Does the empty queue look valid?" )
    if answer == 'y':
        score += worth
    else:
        raise Exception
    print( "\npassed" )
    
  except Exception as problem:
    print( "\nFAILED", problem )
    s = "-" + str(worth) + " invalid queue after dequeue of empty queue LL"
    deductions.append( s )

# ----------------------------------------
# enqueue 3 things onto empty queue LL

print( "\n-----------------------------------" )
print( "enqueue 3 things onto new empty queue LL" )
worth = 0.5

try:
    part2 = False

    print( "creating new empty queue" )
    queue = queue_LL_class()

    print( "enquing 10, then 20, then 30" )
    queue.enqueue( 10 )
    queue.enqueue( 20 )
    queue.enqueue( 30 )

    part2 = True

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " exception occurred while enquing onto new queue LL"
    deductions.append( s )

if part2:
    try:

        print( "" )
        print( "queue ends should be labeled front and back" )
        print( "10 should be at the front" )
        print( "20 should be in the middle" )
        print( "30 should be at the back" )
        print( "" )
        print( queue )
        print( "" )

        answer = get_yes_no( "Does the queue look valid?" )
        if answer != 'y':
            raise Exception
        else:
            score += worth
            print( "\npassed" )

    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " queue LL does not look valid after 3 enqueues"
        deductions.append( s )

# ----------------------------------------
# queue LL length after 3 enqueues

print( "\n-----------------------------------" )
print( "get length of queue LL after 3 enqueues" )
worth = 0.5

try:

    length = len( queue )

    print( "\nexpect length: 3" )
    print( "actual length:", length )

    if length != 3:
        raise Exception
    else:
        score += worth
        print( "\npassed" )
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " wrong queue LL length after 3 enqueues"
    deductions.append( s )

# ----------------------------------------
# dequeue values off a queue LL

print( "\n-----------------------------------" )
print( "dequeue values off a queue LL\n" )
worth = 0.5 # x3

try:
    error_msg = "exception during queue LL dequeue"

    print( "creating new queue LL" )
    queue = queue_LL_class()

    print( "enqueue 5, enqueue 6, enqueue 7\n5 should be front of the queue" )
    queue.enqueue( 5 )  # front
    queue.enqueue( 6 )
    queue.enqueue( 7 )  # back

    print( "dequing value from queue" )
    value = queue.dequeue()

    print( "\nexpect value: 5" )
    print( "actual value:", value, "\n" )

    if value != 5:
        error_msg = "1 pop, wrong value dequeued from queue LL" 
        raise Exception

    print( "expect length: 2" )
    length = len( queue )
    print( "actual length:", length, "\n" )

    if length != 2:
        error_msg = "1 pop, incorrect length after dequeue queue LL"
        raise Exception

    print( "front should be 6" )
    print( "back  should be 7" )
    print( "there should be no 5\n" )
    print( queue )
    print( "" )

    answer = get_yes_no( "Does the queue look valid?" )
    if answer != 'y':
        error_msg = "invalid queue LL after dequeue"
        raise Exception

    print( "dequeue two more values" )

    value = queue.dequeue()
    value = queue.dequeue()

    print( "\nexpect value: 7" )
    print( "actual value:", value, "\n" )
    
    if value != 7:
        error_msg = "3 pops, wrong value dequeued from queue LL" 
        raise Exception

    print( "expect length: 0" )
    length = len( queue )
    print( "actual length:", length, "\n" )

    if length != 0:
        error_msg = "3 dequeues, incorrect length after dequeue queue LL"
        raise Exception

    print( "the queue should be empty\n" )
    print( queue )
    print( "" )

    answer = get_yes_no( "Does the queue look empty?" )
    if answer != 'y':
        error_msg = "invalid queue LL after 3 dequeues, should be empty"
        raise Exception    
    
    print( "\npassed" )
    score += 3*worth

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(3*worth) + " " + error_msg
    deductions.append( s )

# ========================================
# create/print stack arr

print( "\n-----------------------------------" )
print( "create/print empty stack arr" )
worth = 0.25

try:
    stack = stack_array_class( 5 )
    print( stack )
    print( "" )
    
    print( "passed" )
    score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to create/print empty stack arr"
    deductions.append( s )

# ----------------------------------------
# length of empty stack arr

print( "\n-----------------------------------" )
print( "length of empty stack arr" )
worth = 0.25

try:
    length = len( stack )
    print( "expect: 0" )
    print( "actual:", length, "\n" )

    if length == 0:
        print( "passed" )
        score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to get length of empty stack arr"
    deductions.append( s )

# ----------------------------------------
# pop empty stack arr

print( "\n-----------------------------------" )
print( "pop empty stack arr" )
print( "must have error message, no raising exceptions" )
print( "stack must remain valid after failed pop" )
worth = 0.25 # x2

try:
    print( "" )
    value = stack.pop()
    print( "" )

    part2 = True

except Exception as problem:
    print( "FAILED" )
    s = "-" + str(2*worth) + " exception occured during pop of empty stack arr"
    deductions.append( s )
    part2 = False

if part2:
  try:      
    answer = get_yes_no( "Did you see an error message?" )
    if answer != 'y':
        raise Exception
    score += worth
  except:
    print( "\nFAILED" )
    s = "-" + str(worth) + " error msg missing: pop of empty stack arr"
    deductions.append( s )

if part2:
  try:
    print( "\nexpect length: 0" )
    length = len( stack )
    print( "actual length:", length )
    if length != 0:
        raise Exception

    print( "\n", stack, "\n", sep="" )
    answer = get_yes_no( "Does the empty stack look valid?" )
    if answer == 'y':
        score += worth
    else:
        raise Exception
    print( "\npassed" )
    
  except Exception as problem:
    print( "\nFAILED", problem )
    s = "-" + str(worth) + " invalid stack after pop of empty stack arr"
    deductions.append( s )

# ----------------------------------------
# push 3 things onto empty stack arr

print( "\n-----------------------------------" )
print( "push 3 things onto new empty stack arr" )
worth = 0.5

try:
    part2 = False

    print( "creating new size 3 empty stack" )
    stack = stack_array_class( 3 )

    print( "pushing 10, then 20, then 30" )
    stack.push( 10 )
    stack.push( 20 )
    stack.push( 30 )

    part2 = True

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " exception occurred while pushing onto new stack arr"
    deductions.append( s )

if part2:
    try:

        print( "" )
        print( "stack ends should be labeled top and bottom" )
        print( "10 should be at the bottom" )
        print( "20 should be in the middle" )
        print( "30 should be at the top" )
        print( "" )
        print( stack )
        print( "" )

        answer = get_yes_no( "Does the stack look valid?" )
        if answer != 'y':
            raise Exception
        else:
            score += worth
            print( "\npassed" )

    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " stack arr does not look valid after 3 pushes"
        deductions.append( s )

# ----------------------------------------
# stack arr length after 3 pushes

print( "\n-----------------------------------" )
print( "get length of stack arr after 3 pushes" )
worth = 0.5

try:

    length = len( stack )

    print( "\nexpect length: 3" )
    print( "actual length:", length )

    if length != 3:
        raise Exception
    else:
        score += worth
        print( "\npassed" )
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " wrong stack arr length after 3 pushes"
    deductions.append( s )

# ----------------------------------------
# push onto full stack arr

print( "\n-----------------------------------" )
print( "push onto full stack arr\n" )
worth = 0.5 # x2

try:
    part2 = False

    print( "creating new size 3 stack" )
    stack = stack_array_class( 3 )

    print( "pushing 11, then 22, then 33" )
    stack.push( 11 )
    stack.push( 22 )
    stack.push( 33 )

    print( "pushing 44, this should give an error\n" )
    stack.push( 44 )
    print( "" )

    score += worth
    part2 = True
    
except Exception as problem:
    print( "FAILED" )
    s = "-" + str(2*worth) + " exception during push onto full stack arr test"
    deductions.append( s )

if part2:
    try:
        answer = get_yes_no( "Did you see an error message?" )
        
        if answer != 'y':
            part2 = False
            raise Exception
        
    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " missing error msg when pushing onto full stack arr" 
        deductions.append( s )

if part2:
    try:

        length = len( stack )
        
        print( "\nexpect length: 3" )
        print( "actual length:", length )
        
        if length != 3:
            part2 = False
            raise Exception
        
    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " wrong length after push onto full stack arr"
        deductions.append( s )

if part2:
    try:

        print( "\nshould see valid stack" )
        print( "  btm 11" )
        print( "      22" )
        print( "  top 33" )
        print( "there should be no 44 at all\n" )

        print( stack )

        answer = get_yes_no( "\nDoes the stack look valid?" )
        if answer != 'y':
            raise Exception

        print( "\npassed" )
        score += worth
        
    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " invalid stack after push onto full stack arr test"
        deductions.append( s )

# ----------------------------------------
# pop values off a stack arr

print( "\n-----------------------------------" )
print( "pop values off a stack arr\n" )
worth = 0.5 # x3

try:
    error_msg = "exception during stack arr pop"

    print( "creating new size 5 stack arr" )
    stack = stack_array_class( 5 )

    print( "push 5, push 6, push 7\n7 should be on top of the stack" )
    stack.push( 5 )  # btm
    stack.push( 6 )
    stack.push( 7 )  # top

    print( "popping value off stack" )
    value = stack.pop()

    print( "\nexpect value: 7" )
    print( "actual value:", value, "\n" )

    if value != 7:
        error_msg = "1 pop, wrong value popped off stack arr" 
        raise Exception

    print( "expect length: 2" )
    length = len( stack )
    print( "actual length:", length, "\n" )

    if length != 2:
        error_msg = "1 pop, incorrect length after popping stack arr"
        raise Exception

    print( "btm should be 5" )
    print( "top should be 6" )
    print( "there should be no 7\n" )
    print( stack )
    print( "" )

    answer = get_yes_no( "Does the stack look valid?" )
    if answer != 'y':
        error_msg = "invalid stack arr after pop"
        raise Exception

    print( "popping two more values" )

    value = stack.pop()
    value = stack.pop()

    print( "\nexpect value: 5" )
    print( "actual value:", value, "\n" )
    
    if value != 5:
        error_msg = "3 pops, wrong value popped off stack arr" 
        raise Exception

    print( "expect length: 0" )
    length = len( stack )
    print( "actual length:", length, "\n" )

    if length != 0:
        error_msg = "3 pops, incorrect length after popping stack arr"
        raise Exception

    print( "the stack should be empty\n" )
    print( stack )
    print( "" )

    answer = get_yes_no( "Does the stack look empty?" )
    if answer != 'y':
        error_msg = "invalid stack arr after 3 pops, should be empty"
        raise Exception    
    
    print( "\npassed" )
    score += 3*worth

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(3*worth) + " " + error_msg
    deductions.append( s )

# ========================================
# create/print queue arr

print( "\n-----------------------------------" )
print( "create/print empty queue arr" )
worth = 0.25

try:
    queue = queue_array_class( 5 )
    print( queue )
    print( "" )
    
    print( "passed" )
    score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to create/print empty queue arr"
    deductions.append( s )


# ----------------------------------------
# length of empty queue arr

print( "\n-----------------------------------" )
print( "length of empty queue arr" )
worth = 0.25

try:
    length = len( queue )
    print( "expect: 0" )
    print( "actual:", length, "\n" )

    if length == 0:
        print( "passed" )
        score += worth
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " failed to get length of empty queue arr"
    deductions.append( s )

# ----------------------------------------
# dequeue empty queue arr

print( "\n-----------------------------------" )
print( "dequeue empty queue arr" )
print( "must have error message, no raising exceptions" )
print( "queue must remain valid after failed dequeue" )
worth = 0.25 # x2

try:
    print( "" )
    value = queue.dequeue()
    print( "" )

    part2 = True

except Exception as problem:
    print( "FAILED" )
    s = "-" + str(2*worth) + " exception occured during dequeue of empty queue arr"
    deductions.append( s )
    part2 = False

if part2:
  try:      
    answer = get_yes_no( "Did you see an error message?" )
    if answer != 'y':
        raise Exception
    score += worth
  except:
    print( "\nFAILED" )
    s = "-" + str(worth) + " error msg missing: dequeue of empty queue arr"
    deductions.append( s )

if part2:
  try:
    print( "\nexpect length: 0" )
    length = len( queue )
    print( "actual length:", length )
    if length != 0:
        raise Exception

    print( "\n", queue, "\n", sep="" )
    answer = get_yes_no( "Does the empty queue look valid?" )
    if answer == 'y':
        score += worth
    else:
        raise Exception
    print( "\npassed" )
    
  except Exception as problem:
    print( "\nFAILED", problem )
    s = "-" + str(worth) + " invalid queue after dequeue of empty queue arr"
    deductions.append( s )

# ----------------------------------------
# enqueue 3 things onto empty queue arr

print( "\n-----------------------------------" )
print( "enqueue 3 things onto new empty queue arr" )
worth = 0.5

try:
    part2 = False

    print( "creating new size 3 empty queue" )
    queue = queue_array_class( 3 )

    print( "enquing 10, then 20, then 30" )
    queue.enqueue( 10 )
    queue.enqueue( 20 )
    queue.enqueue( 30 )

    part2 = True

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " exception occurred while enquing onto new queue arr"
    deductions.append( s )

if part2:
    try:

        print( "" )
        print( "queue ends should be labeled front and back" )
        print( "10 should be at the front" )
        print( "20 should be in the middle" )
        print( "30 should be at the back" )
        print( "" )
        print( queue )
        print( "" )

        answer = get_yes_no( "Does the queue look valid?" )
        if answer != 'y':
            raise Exception
        else:
            score += worth
            print( "\npassed" )

    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " queue arr does not look valid after 3 enqueues"
        deductions.append( s )

# ----------------------------------------
# queue arr length after 3 enqueues

print( "\n-----------------------------------" )
print( "get length of queue arr after 3 enqueues" )
worth = 0.5

try:

    length = len( queue )

    print( "\nexpect length: 3" )
    print( "actual length:", length )

    if length != 3:
        raise Exception
    else:
        score += worth
        print( "\npassed" )
    
except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(worth) + " wrong queue arr length after 3 enqueues"
    deductions.append( s )

# ----------------------------------------
# enqueue onto full queue arr

print( "\n-----------------------------------" )
print( "enqueue onto full queue arr\n" )
worth = 0.5 # x2

try:
    part2 = False

    print( "creating new size 3 queue" )
    queue = queue_array_class( 3 )

    print( "enquing 11, then 22, then 33" )
    queue.enqueue( 11 )
    queue.enqueue( 22 )
    queue.enqueue( 33 )

    print( "enquing 44, this should give an error\n" )
    queue.enqueue( 44 )
    print( "" )

    score += worth
    part2 = True
    
except Exception as problem:
    print( "FAILED" )
    s = "-" + str(2*worth) + " exception during enqueue onto full queue arr test"
    deductions.append( s )

if part2:
    try:
        answer = get_yes_no( "Did you see an error message?" )
        
        if answer != 'y':
            part2 = False
            raise Exception
        
    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " missing error msg when enquing onto full queue arr" 
        deductions.append( s )

if part2:
    try:

        length = len( queue )
        
        print( "\nexpect length: 3" )
        print( "actual length:", length )
        
        if length != 3:
            part2 = False
            raise Exception
        
    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " wrong length after enqueue onto full queue arr"
        deductions.append( s )

if part2:
    try:

        print( "\nshould see valid queue" )
        print( "  frn 11" )
        print( "      22" )
        print( "  bck 33" )
        print( "there should be no 44 at all\n" )

        print( queue )

        answer = get_yes_no( "\nDoes the queue look valid?" )
        if answer != 'y':
            raise Exception

        print( "\npassed" )
        score += worth
        
    except Exception as problem:
        print( "\nFAILED" )
        s = "-" + str(worth) + " invalid queue after push onto full queue arr test"
        deductions.append( s )

# ----------------------------------------
# dequeue values off a queue arr

print( "\n-----------------------------------" )
print( "dequeue values off a queue arr\n" )
worth = 0.5 # x3

try:
    error_msg = "exception during queue arr dequeue"

    print( "creating new size 5 queue arr" )
    queue = queue_array_class( 5 )

    print( "enqueue 5, enqueue 6, enqueue 7\n5 should be front of the queue" )
    queue.enqueue( 5 )  # front
    queue.enqueue( 6 )
    queue.enqueue( 7 )  # back

    print( "dequing value from queue" )
    value = queue.dequeue()

    print( "\nexpect value: 5" )
    print( "actual value:", value, "\n" )

    if value != 5:
        error_msg = "1 pop, wrong value dequeued from queue arr" 
        raise Exception

    print( "expect length: 2" )
    length = len( queue )
    print( "actual length:", length, "\n" )

    if length != 2:
        error_msg = "1 pop, incorrect length after dequeue queue arr"
        raise Exception

    print( "front should be 6" )
    print( "back  should be 7" )
    print( "there should be no 5\n" )
    print( queue )
    print( "" )

    answer = get_yes_no( "Does the queue look valid?" )
    if answer != 'y':
        error_msg = "invalid queue arr after dequeue"
        raise Exception

    print( "dequeue two more values" )

    value = queue.dequeue()
    value = queue.dequeue()

    print( "\nexpect value: 7" )
    print( "actual value:", value, "\n" )
    
    if value != 7:
        error_msg = "3 pops, wrong value dequeued from queue arr" 
        raise Exception

    print( "expect length: 0" )
    length = len( queue )
    print( "actual length:", length, "\n" )

    if length != 0:
        error_msg = "3 dequeues, incorrect length after dequeue queue arr"
        raise Exception

    print( "the queue should be empty\n" )
    print( queue )
    print( "" )

    answer = get_yes_no( "Does the queue look empty?" )
    if answer != 'y':
        error_msg = "invalid queue arr after 3 dequeues, should be empty"
        raise Exception    
    
    print( "\npassed" )
    score += 3*worth

except Exception as problem:
    print( "\nFAILED" )
    s = "-" + str(3*worth) + " " + error_msg
    deductions.append( s )

# ------------------------------------------
# queue arr should be circular

print( "\n-----------------------------------" )
print( "queue arr should be circular\n" )

# +2 no crash, correct length
# +2 queue looks valid
worth = 4 # total 4 pts

try:
    error_msg = "problem while testing circular queue arr"
    part2 = True

    print( "creating new queue arr of size six" )
    queue = queue_array_class( 6 )

    print( "enqueue six values: 11, 22, 50, 60, 75, 99" )
    queue.enqueue( 11 )
    queue.enqueue( 22 )
    queue.enqueue( 50 )
    queue.enqueue( 60 )
    queue.enqueue( 75 )
    queue.enqueue( 99 )

    print( "dequeue two values: 11, 22" )
    value = queue.dequeue()
    value = queue.dequeue()

    print( "enqueue two values: 500, 800\nshould get wraparound" )
    queue.enqueue( 500 )
    queue.enqueue( 800 )

    print( "dequeue two values: 50, 60" )
    value = queue.dequeue()
    value = queue.dequeue()

    print( "\nexpect value: 60" )
    print( "actual value:", value )

    if value != 60:
        error_msg = "wrong value dequeued while testing circular queue arr"
        raise Exception

    print( "\nexpect length: 4" )
    length = len( queue )
    print( "actual length:", length )

    if length != 4:
        error_msg = "wrong queue length while testing circular queue arr"
        raise Exception

    score += worth // 2

except Exception as problem:
    part2 = False
    print( "\nFAILED" )
    s = "-" + str(worth) + " " + error_msg
    deductions.append( s )

if part2:
  try:

    print( "\ncircular queue should look like this" )
    print( "front 75, 99, 500, 800 back\n" )

    print( queue )
    print( "" )

    answer = get_yes_no( "Does the circular queue look valid?" )
    if answer != 'y':
        error_msg = "circular queue arr does not look valid"
        raise Exception

    print( "\nenqueue two more: 850, 900" )
    queue.enqueue( 850 )
    queue.enqueue( 900 )

    print( "try to enqueue 444, this should give an error message\n" )
    queue.enqueue( 444 )
    print( "" )

    answer = get_yes_no( "Do you see an error message?" )
    if answer != 'y':
        error_msg = "should not have allowed enqueue on full circular queue arr"
        raise Exception

    print( "\ncircular queue should look like this" )
    print( "there should be no 444 anywhere" )
    print( "front 75, 99, 500, 800, 850, 900 back\n" )

    print( queue )
    print( "" )

    answer = get_yes_no( "Does the circular queue look valid?" )
    if answer != 'y':
        error_msg = "circular queue arr does not look valid after further testing"
        raise Exception

    score += worth // 2
    print( "\npassed" )
      
  except:
    print( "\nFAILED" )
    s = "-" + str(worth//2) + " " + error_msg
    deductions.append( s )

# ==========================================
# inspect code, data structures build as required?

print( "\n===================================" )
print( "inspect the code, look at __init__\n" )
print( "LL classes should have contents that are a linked list" )
print( "array classes should have contents that are a python list" )
print( "ie: self.contents = self.size * [0]\n" )
worth = 4 # x4

answer = get_yes_no( "stack LL class contents are a linked list?" )
if answer != 'y':
    score -= worth
    s = "-" + str(worth) + " stack LL contents are not a linked list"
    deductions.append( s )

answer = get_yes_no( "queue LL class contents are a linked list?" )
if answer != 'y':
    score -= worth
    s = "-" + str(worth) + " queue LL contents are not a linked list"
    deductions.append( s )

answer = get_yes_no( "stack arr class contents are an array/list?" )
if answer != 'y':
    score -= worth
    s = "-" + str(worth) + " stack arr class contents are not an array/list"
    deductions.append( s )

answer = get_yes_no( "queue arr class contents are an array/list?" )
if answer != 'y':
    score -= worth
    s = "-" + str(worth) + " queue arr class contents are not an array/list"

if score < 0:
    print( "\nscore can't be less than zero, adjusting to zero\n" )
    score = 0

# ==========================================
# print score

print( "\n===================================" )
print( "\nTOTAL SCORE =", score, "\n" )

for item in deductions:
    print( item )

if len( deductions ) > 0:
    print( "" )

if score == 20:
    print( "A  Excellent!\n" )
    print( "You wrote completely correct data structures." )
    print( "Data structures must be completely correct to be useful." )
elif score >= 18:
    print( "B  Very good!\n" )
    print( "You wrote almost completely correct data structures." )
    print( "Remember, data structures must be completely correct to be useful." )
    print( "Yours just need some fixes." )
elif score >= 16:
    print( "C  needs debugging\n" )
elif score >= 14:
    print( "D  needs much debugging\n" )
else:
    print( "F  needs much debugging\n" )

if score < 18:
    print( "Remember, data structures must be completely correct to be useful." )
    print( "A stack must have push/pop, a queue must have enqueue/dequeue." )
    print( "They must work when empty, they must work when full." )
    print( "They must return correct length and display correctly." )
    print( "An array based queue must be circular." )
    print( "With only some of that, they're as useful as a car that" )
    print( "goes forward but not back or whose engine dies sometimes." )
    
print( "" )

