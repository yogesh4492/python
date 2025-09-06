# except  5 number from user and store even in even list and odd number i

even_list=[]
odd_List=[]
for i in range(1,6):
    num=int(input("Enter Number= "))
    if num%2==0:
        even_list.append(num)
    else:
        odd_List.append(num)
print(f"Even number= {even_list}")
print(f"odd number= {odd_List}")
