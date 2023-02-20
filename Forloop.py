# This program creates a multiplication table in ascending or descending order based on user preference
# This program demonstrates the use of a for loop to repeat a codeblock a certain number of times
# This program makes use of the range() function in the for loop


multiplicand = int(input("Please enter a multiplicand: "))
multipliers = int(input("Please enter a multiplier: "))
answer1 = "Yes"
answer2 = "yes"
answer3 = "No"
answer4 = "no"
answer = input("Would you like the multiplication table to be in descending order? Please enter Yes or No: ")

if answer == answer1 or answer == answer2:
    for multiplier in range(multipliers,0,-1):
        product = multiplicand * multiplier
        print(multiplicand,"x",multiplier,"=",product)
        
if answer == answer3 or answer == answer4:
    for multiplier in range(1,(multipliers - 1)):
        product = multiplicand * multiplier
        print(multiplicand,"x",multiplier,"=",product)

