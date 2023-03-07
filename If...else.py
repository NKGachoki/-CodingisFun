'''
A program to do the following, namely: 
1. Determine the grades of students based on their final examination scores and indicate whether the students have passed and can proceed to the next semester, 
2. Determine the amount of fees discount to be awarded to each student on the basis of their score, and
3. Calculate the amount of fees to be paid for the next semester.
'''
# This program is meant to demonstrate the use of if ... else statements and arithmetic, boolean, comparison and logical operators in  Python.

name = input("Please enter your name: ")
score = int(input("Please enter your score: "))
fee = 2500

if score < 0 or score > 100:
    print("Invalid score entered, please try again.")

elif score <= 100 and score >= 70:
    print(f"Congratulations {name}, you have gotten an A in your finals!")
    if score <= 100 and score >= 91:
        print("You have qualified for a 50% discount towards your fee for the next semester.")
        discount1 = fee * 50/100
        total_fee1 = fee - discount1
        print(f"Your fee for the next semester is {total_fee1}$")
    elif score <= 90 and score >= 81:
        print("You have qualified for a 40% discount towards your fee for the next semester.")
        discount2 = fee * 40/100
        total_fee2 = fee - discount2
        print(f"Your fee for the next semester is {total_fee2}$")
    else:
        print("You have qualified for a 30% discount towards your fee for the next semester.")
        discount3 = fee * 30/100
        total_fee3 = fee - discount3
        print(f"Your fee for the next semester is {total_fee3}$")
        
elif score <= 69 and score >= 60:
    print(f"Congratulations {name}, you have gotten a B in your finals!")
    if score <= 69 and score >= 65:
        print("You have qualified for a 20% discount towards your fee for the next semester.")
        discount4 = fee * 20/100
        total_fee4 = fee - discount4
        print(f"Your fee for the next semester is {total_fee4}$")
    else:
        print("You have qualified for a 10% discount towards your fee for the next semester.")
        discount5 = fee * 10/100
        total_fee5 = fee - discount5
        print(f"Your fee for the next semester is {total_fee5}$")
        
elif score <= 59 and score >= 50:
    print(f"{name}, you have gotten a C in your finals.")
    print(f"Your fee for the next semester is {fee}$")
    
elif score <= 49 and score >= 40:
    print(f"{name}, you have gotten a D in your finals.")
    print(f"Your fee for the next semester is {fee}$")
    
else:
    print(f"{name}, you have failed your finals.")
    print("You will have to repeat the semester before proceeding to the next one.")
