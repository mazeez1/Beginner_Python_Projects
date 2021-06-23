#Add two numbers (all of these functions are akin to pivot choices)
def addStuff(num1, num2):
    print("Adding numbers!")
    return num1 + num2

#Subtract two numbers
def subStuff(num1, num2):
    print("Subtracting numbers!")
    return num1 - num2

#Multiply two numbers
def multStuff(num1, num2):
    print("Multiplying numbers!")
    return num1 * num2

#Divide two numbers 
def divStuff(num1, num2):
    print("Dividing numbers!")
    return num1 / num2

#Driver function (akin to your quicksort function)
#Has the main functionality
def doMaths(num1, num2, functionName):

    print("Performing maths!")

    #Calling functionName will call whichever action
    #was specified by the user
    #i.e. add, subtract, multiply, divide
    result = functionName(num1, num2)

    return result


#The user interface portion
def main():

    #A variable with (functionName).(variableName) will remain
    #the same between multiple function calls
    #Think static variables
    if not main.sameNumbers:
        
        #Greet the user
        print("Welcome please input two numbers separated by a space!")

        #The while loop is necessary for the try/except case here
        #If the except is called, we want to try again so we loop
        while True:
            #Get the user input store in x and y
            #
            #
            #.split() splits a string or list at whatever character is specified
            #The default is a space
            #Example "Hello World!".split() returns ["Hello","World!"]
            #Whereas "Hello World!".split("o") returns ["Hell"," W", "rld!"]
            #
            #
            #The map() function maps every list element to the type specified
            #map(int, ["5","531","120"]) returns [5, 531, 120]
            #map(str, [5, 12, 13]) returns ["5","12","13"]
            #
            #
            #The try/except block catches any errors (i.e. a user inputs
            #letters or inputs a different amount than two numbers)
            #Try/Except blocks are useful for error proofing your program

            try:
                main.x, main.y = map(int, input("Enter 2 numbers in format 'Num1 Num2': ").split())
                break
            except:
                print("Enter two numbers separated by a space please.")
                continue
    
    #List of options the user has
    options = ["Add","Subtract","Divide","Multiply"]

    #Whitespace between user input and next question
    print("\n\nWhich operation would you like to do on those two numbers?")

    #Print all the options
    for i in range(len(options)):

        #Format the options in an easy to read list
        print(str( i + 1) + ": " + options[i])

    #Newline
    print()

    #Error proofing
    while True:
        try:
            #Get the user's choice
            choice = int(input("Enter the number of your choice: "))

            #Put checks for the variable in the try portion for further
            #Error checking
            if not 0 < choice < 5:
                print("Please make sure your choice is in the range 1-4")
                print()

                #Make sure to continue or it won't loop again
                continue
            
            break
        
        except:
            print("Please input one number")
            print()
            continue

    print()

    #*********************************************
    #*THESE FUNCTION CALLS ARE THE IMPORTANT PART*
    #*********************************************
    #If 1 perform addition
    if choice == 1:

        #Pass in the addStuff function for addition as a parameter
        print("Your result is", doMaths(main.x, main.y, addStuff))

    #If 2 perform subtraction
    if choice == 2:

        #Pass in subStuff function for subtraction as a parameter
        print("Your result is", doMaths(main.x, main.y, subStuff))

    #You get the idea
    if choice == 3:

        print("Your result is", doMaths(main.x, main.y, divStuff))

    if choice == 4:

        print("Your result is", doMaths(main.x, main.y, multStuff))

    #Newline
    print()

    #Ask the user if they'd like to continue
    cont = input("Would you like to do another operation? (y/n): ").lower()

    if 'y' in cont:

        #Ask the user if they want to use the same numbers
        same = input("Would you like to use the same numbers? (y/n): ").lower()

        #Check if they want to use the same numbers
        if 'y' in same:
            #If so change sameNumbers to True
            main.sameNumbers = True
        else:
            #Else make sure it is False
            main.sameNumbers = False

        #Return True so main gets called again
        return True

    else:

        #Return false so it breaks the loop
        return False


#Initialize main.sameNumbers
main.sameNumbers = False

#Call the function and loop as long as the user wants to
while main():
    continue

print("Goodbye")
