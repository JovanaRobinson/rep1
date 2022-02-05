
value = input("Let's play Simon! Type in 1 and press enter to begin playing:") 


while True:
    if value.isdigit() == True: 
         value = int(value)
         if value > 1 or value < 1: 
             value = input("please input the number required.")
             continue 
         else:
             break 
    else:
        value = input("invalid input, please provide an integer:") 


answer = input("sequence3456")
if answer == '3456':
    print('Correct!')
else:
    print("Incorrect!")


answer = input("sequence8907")
if answer == '8907':
    print('Correct!')
else:
    print("Incorrect!")

answer = input("sequence1111")
if answer == '1111':
    print('Correct!')
else:
    print("Incorrect!")

print("Thank you for playing!")


    
