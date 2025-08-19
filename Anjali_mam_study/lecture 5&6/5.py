#accept 5 number 
k=0
j=0

for i in range(1,6):
    num=int(input("Enter number= "))
    if num%2==0:
        k=k+1
    else:
        j=j+1

print("total even number= ",k)
print("total odd number= ",j)