from datetime import date
import sys

# Birth Year Input 
while True:
    try:
        birth_year=int(input("Enter the Birthday.\nBirth Year : "))
        break
    except ValueError:
        print("Sorry, Integer Required!")
        print("\n")

if birth_year==0: # Check the Is the user entered value and Creation of Error for it.
    raise Exception("Sorry, You didn't Enter the Year. You Entered 0. Please Try agin,.")

# Birth Month Input
while True:
    try:
        birth_month=int(input("Birth Month : "))
        break
    except ValueError:
        print("Sorry, Integer Required!") 
        print("\n")

if birth_month < 1 or birth_month > 12: # Limitation of months 
    raise Exception("Sorry, Invalid Month. Try Again.")

# Birth Day Input
while True:
    try:
        birth_day=int(input("Birth Day : "))
        break
    except ValueError:
        print("Sorry, Integer Required!")
        print("\n")

if birth_month == 2:
    if birth_day >29 or birth_day <1: # February day limitation and error making
        raise Exception("Sorry, February has only maximum 29 days. Please Try again.")
else:
    if birth_day >31 or birth_day<1: # Normal Months day limitation and error making
        raise Exception("Sorry, Invalid Date. The Month has only maximum 31 days. Please Try again.")

# Age Owner's Gender Input    
while True:
    try:
        gender = int(input("\nEnter the gender of the owner this birthday.\n\n1. Male or Boy. \n2. Female or Girl \n3. Other. \n\nEnter Number Here : "))
        break
    except ValueError:
        print("Sorry, Integer Required!")


current_year = date.today().year # Take Current year from system

age = current_year-birth_year # Calculation of the Age

next_celebration_year = current_year + 1 # Calculation of next celebration year


# Check the gender and Display the sutable output
if gender==1:
    print("\n")
    print("He is", age,"years old.")
    print("Wish him to",birth_day,"/",birth_month,"/",next_celebration_year)
elif gender==2:
    print("\n")
    print("She is", age,"years old.")
    print("Wish her to",birth_day,"/",birth_month,"/",next_celebration_year)
else:
    print("\n")
    print("That CREATURE is", age,"years old.")
    print("Wish that CREATURE to",birth_day,"/",birth_month,"/",next_celebration_year)