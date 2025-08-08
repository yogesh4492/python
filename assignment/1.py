# Que-1-Introduction to Python
# i):- Write a Python program that prints "Hello, World!!
print("Hello World !!")
# ii):- Set up Python on your local machine and write a program to display your name
print("Good Morning, My Name is Yogesh Patel")

#----------------------------------------------------------------------------------------------------------------------------------

# 2. Programming Style

"""i):-Write a Python program that demonstrates the correct use of indentation, comments, and 
 variables following PEP 8 guidelines.
 
 """
name="Yogesh"
print(name)


#-------------------------------------------------------------------------------------------------------------------------------------

# Que-3:Core Python Concepts

# i):-Write a Python program to demonstrate the creation of variables and different data types. 

roll=101
name='yogesh'
percentage=89.98
fees=1000000

print(type(roll))
print(type(name))
print(type(percentage))
print(type(fees))



# ii):- Practical Example 1: How does the Python code structure work? 
"""
Understanding Python Code Structure
Python has a very simple, readable, and indentation-based structure.
Unlike C, C++, or Java — there are no curly braces {} to mark blocks.
Instead, indentation (spaces or tabs) decides the code structure.

Basic Components of Python Structure
Comments – start with # (for documentation or notes).

# This is a comment
Docstrings – multi-line documentation using triple quotes.

#This program demonstrates Python structure.

Import Statements – to use external or built-in modules.

import math
from datetime import datetime

Function & Class Definitions – reusable blocks of code.


def greet(name):
    print(f"Hello, {name}")

class Person:
    def __init__(self, name):
        self.name = name


Main Code Block – executed when the file runs directly.
if __name__ == "__main__":
    greet("Yogesh")"""

# iii):- Practical Example 2: How to create variables in Python? 

"""
Variable: A name which can  store a value of different data type

Rules For Variable Declaration:

1)we can not use any keyword or reserved word as variable name
  ex. int,float

2)we can use a-z,A-z ,underscore and 0-9 in variable name declaration.
ex. name1,number,sum

3)we can not use white in variable name also use camel case or underscore.

ex. first name  X
    firstName  # lower camel case valid
    FirstName  # Uppercamel case valid
    First_name # underscore valid

4) we can't use digit as first letter of variable.

ex 1num   X
   2num   X

   num1 #valid
   num2 # valid

5)Python is case sensitive language so AGE and age Are different

name='yogesh'   # string variable
num=10          # int  variable
percentage=89.98 # float variable

flag=true   # boolean variable

we can also declare multiple  varible

x,y,z=10,20,30


We can also assign same value to differnt variable using assignment operator

a=b=c='Python'

"""
 
# iv):- Practical Example 3: How to take user input using the input() function. 
"""
input(): input is function that can accept user input we can use it to take dynamic value from user


syntax 

input("Prompt message")


by default input function convert input data into string

so,when we want to  use some calculation we are need to type convertion.

Type conversion: Type casting use to convert one type data into another type data

syntax

variable_name=int(input("prompt message"))



"""
name=input("Enter your name= ")

R_num=int(input("Enter Your Roll Number= "))

print(name)
print(R_num)


# v):- Practical Example 4: How to check the type of a variable dynamically using type()

"""  
Type(): By using type function we can check what type of data variable can hold or store
syntax

type(varible_name)

"""


num=10

print(type(num))
#-------------------------------------------------------------------------------------------------------------------------