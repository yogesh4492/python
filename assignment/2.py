
i=1
j=1
row=int(input("Enter number of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()  # Move to the next line after each row
 