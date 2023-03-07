# A program to create a list comprised of 10 numerical values entered by the user.
# The program confirms that the values entered are indeed numbers, if not, the user will be prompted to enter the correct value afterwhich the user can continue to populate the list.
# The program then prints out the list and further prints out the smallest and largest value in the list.
# The program also calculates and prints out the sum of the values in the list and the average of those values.
  
number_list = [None]

# Code to take user input, check user input and store said input in the list
print("Please enter 10 numbers: ")

number1 = input()
if number1.isdigit() == True:
    number1 = int(number1)
    number_list[0] = number1
elif number1.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number1 = input()
        if number1.isdigit() == True:
            number1 = int(number1)
            number_list[0] = number1
            break

number2 = input()
if number2.isdigit() == True:
    number2 = int(number2)
    number_list.append(number2)
elif number2.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number2 = input()
        if number2.isdigit() == True:
            number2 = int(number2)
            number_list.append(number2)
            break

number3 = input()
if number3.isdigit() == True:
    number3 = int(number3)
    number_list.append(number3)
elif number3.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number3 = input()
        if number3.isdigit() == True:
            number3 = int(number3)
            number_list.append(number3)
            break

number4 = input()
if number4.isdigit() == True:
    number4 = int(number4)
    number_list.append(number4)
elif number4.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number4 = input()
        if number4.isdigit() == True:
            number4 = int(number4)
            number_list.append(number4)
            break

number5 = input()
if number5.isdigit() == True:
    number5 = int(number5)
    number_list.append(number5)
elif number5.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number5 = input()
        if number5.isdigit() == True:
            number5 = int(number5)
            number_list.append(number5)
            break

number6 = input()
if number6.isdigit() == True:
    number6 = int(number6)
    number_list.append(number6)
elif number6.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number6 = input()
        if number6.isdigit() == True:
            number6 = int(number6)
            number_list.append(number6)
            break

number7 = input()
if number7.isdigit() == True:
    number7 = int(number7)
    number_list.append(number7)
elif number7.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number7 = input()
        if number7.isdigit() == True:
            number7 = int(number7)
            number_list.append(number7)
            break

number8 = input()
if number8.isdigit() == True:
    number8 = int(number8)
    number_list.append(number8)
elif number8.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number8 = input()
        if number8.isdigit() == True:
            number8 = int(number8)
            number_list.append(number8)
            break

number9 = input()
if number9.isdigit() == True:
    number9 = int(number9)
    number_list.append(number9)
elif number9.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number9 = input()
        if number9.isdigit() == True:
            number9 = int(number9)
            number_list.append(number9)
            break

number10 = input()
if number10.isdigit() == True:
    number10 = int(number10)
    number_list.append(number10)
elif number10.isdigit() == False:
    while True:
        print("Wrong value entered, please enter a number")
        number10 = input()
        if number10.isdigit() == True:
            number10 = int(number10)
            number_list.append(number10)
            break

print(f"The number list entered is:\n{number_list}")

# Code to find the smallest value in the list provided by the user
smallest_number = number_list[0]

for number in number_list:
    if number < smallest_number:
        smallest_number = number

print(f"The smallest value in the list provided is {smallest_number}")

# Code to find the largest value in the list provided by the user
largest_number = number_list[0]

for number in number_list:
    if number > largest_number:
        largest_number = number

print(f"The largest value in the list provided is {largest_number}")

# Code to find the sum of the values entered by the user in the list
sum = 0

for number in number_list:
    sum = sum + number

print(f"The sum of the values entered in the list is {sum}")

# Code to find the average of the values entered by the user
count = 0 

for number in number_list:
    count = count + 1

average = sum / count
print(f"The average value of the list is {average}")




        
    