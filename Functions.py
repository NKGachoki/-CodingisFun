
# A simple program that adds and multiplies 2 numbers

# Function to add 2 numbers
def add_numbers(number1, number2):
    sum = number1 + number2
    return sum

# Function to multiply 2 numbers
def multiply_numbers(number1, number2):
    product = number1 * number2
    return product

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

#Calling the add_numbers function
sum = add_numbers(number1, number2)
print("The sum of",number1,"and",number2,"is",sum)

#Calling the multiply_numbers function
product = multiply_numbers(number1, number2)
print("The product of",number1,"and",number2,"is",product)

