"""  
remove duplicate elements from the list
"""


l1=[2,4,2,6,8,4]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
    