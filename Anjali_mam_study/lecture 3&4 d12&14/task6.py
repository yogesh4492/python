#accept three number
#accept three number from user and check smaller number
num1=int(input("Enter Number1= "))
num2=int(input("Enter Number 2= "))
num3=int(input("Enter Number 3= "))

if num1<num2:
    if num1<num3:
       print(f"{num1} is smallest number")
    else:
       print(f"{num3} is smallest number")
else:
    if num2<num3:
       print(f"{num2} is smalest number")
    else:
       print(f"{num3} is smallest number")
    