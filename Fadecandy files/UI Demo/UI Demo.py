value = input("Welcome to the menu. Options are listed below: \n\t 1. Roll \n\t 2. Sweep \n\t 3. Scroll \n Type the number of your choice and press enter:") #\n - newline; \t - tab


def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val


while True:
    if value.isdigit() == True: # .isdigit()
         value = int(value)
         if value > 3 or value < 1: #value is outside our range
             value = input("please input a number between 1 and 3.")
             continue #skip rest of loop, start from isdigit() check again.
         else:
             break # on correct value datatype: exit the loop
    else:
        value = input("invalid input, please provide an integer:") #ask for a new value


#compare numeric value to choices available, perform associated function or sequence
if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))


