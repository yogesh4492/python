p_list=[]
n_list=[]
for i in range(1,7):
    num=int(input("Enter Number= "))
    if num<0:
        n_list.append(num)
    else:
        p_list.append(num)
print("Negative number= ",n_list)
print("positive number= ",p_list)