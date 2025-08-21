""" 
Que-5.Loops (For,While)
"""

#Practical Example 1: Write a Python program to print each fruit in a list using a simple for 
#loop. List1 = ['apple', 'banana', 'mango'] 

list1=['apple','banana','mango']
for i in list1:
    print(i)

"""-------------------------------------------------------------------------------------------------------"""
# Practical Example 2: Write a Python program to find the length of each string in List1. 

list1=['apple','banana','mango']
for i in list1:
    print(f"{i} {len(i)}")

"""--------------------------------------------------------------------------------------------------------"""
# Practical Example 3: Write a Python program to find a specific string in the list using a simple 
#for loop and if condition. 

list1=['apple','banana','mango']

search_str=input("Enter Searching String Name= ")
if search_str in list1:
    print("String Found")
else:
    print("String not found")
    
"""--------------------------------------------------------------------------------------------------------"""
""" Practical Example 4: Print this pattern using nested for loop: 
 
markdown 
Copy code 
* 
** 
*** 
**** 
*****
"""
row=int(input("Enter Row = "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print()



"""----------------------------------------------------------------------------------------------------------"""