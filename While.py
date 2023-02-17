# Program to create a multiplication table.
# The multiplicand and multiplier will be determined by user input.
# If the user enters "5" as the multiplicand and "10" as the multiplier, then the program will create a multiplication table ranging from "5 x 10" to "5 x 1".
# This program is a practical demonstration of the use of 'while loops' to repeat tasks upon the establishment of certain conditions.
    
multiplicand = int(input("Please enter a multiplicand: "))
multiplier = int(input("Please enter a multiplier: "))

while multiplier >= 1:
    product = multiplicand * multiplier
    print(multiplicand,"x",multiplier,"=",product)
    multiplier = multiplier - 1
