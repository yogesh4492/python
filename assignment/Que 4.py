#Que- 4 Conditional statement
"""
#Practical Example 5: Write a Python program to find greater and
#  less than a number using if_else. 
"""

num1=int(input("Enter number 1= "))
num2=int(input("Enter Number 2= "))
if num1>num2:
    print("Number 1 is Greter than number two")
else:
    print("Number 1 is less than Number two ")
#----------------------------------------------------------------------------------------
"""
 Practical Example 6: Write a Python program to check if a number is prime using if_else.
"""
def prime(num,divisor):
    if num<=1:
        return 0
    elif num==divisor:
        return 1
    elif num%divisor==0:
        return 0
    return prime(num,divisor+1)
num=int(input("Enter Number= "))
if prime(num,2):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")



#---------------------------------------------------------------------------------------- 
""" Practical Example 7: Write a Python program to calculate grades based on percentage using 
if-else ladder. """
percentage=int(input("Enter Your Percentage= "))
if percentage>=90:
    print("Grade:A+")
elif percentage>=75:
    print("Grade:A")
elif percentage>=55:
    print("Grade:B")
elif percentage>=35:
    print("Grade:C")
else:
    print("Grade:D")

#-----------------------------------------------------------------------------------------
""" Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
using a nested if"""

age=int(input("Enter Your Age= "))
weight=int(input("Enter Your Weight= "))

if age>=18:
    if weight>=50:
        print("You are eligible for Blood Donation")
    else:
        print("You are Not Eligible for Blood Donation Because Your weight is less than 50kg")
else:
    print("You are Not Eligible for Blood Donation Because Your age is less than 18 year")

#-----------------------------------------------------------------------------------------