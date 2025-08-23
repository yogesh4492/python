#level 1=1,100 ,level 2=1,100 7 trys level =3 1,50 5 try
import random
# choice=0
# while choice!=4:
print("1. 1-100(no limit)")
print("2. 1-100(7 try only)")
print("3. 1-50(5 try only)")
# print("4.Exit")
choice=int(input("Enter your choice= "))
if choice==1:
    print("-------Welcome In level : 1 -----------")
    computer=random.randint(1,100)
    status=True
    while status:
        user=int(input("Enter Number= "))
        if user>computer:
            print("hint : guess lower number")
        elif user<computer:
            print("Hint: Guess Upeer Number")
        else:
            print("You win")
            print("-----Level 1 Completed try Next---------")
            status=False
elif choice==2:
    print("-------Welcome In level : 2 -----------")
    tr_y=0
    computer=random.randint(1,100)
    while tr_y!=7:
        tr_y+=1
        user=int(input("Enter Number= "))
        
        if user>computer:
            print("hint : guess lower number")
        elif user<computer:
            print("Hint: Guess Upeer Number")
        else:
            print("You win")
            print("-----Level 2 Completed try Next---------")
            tr_y=7
        
elif   choice==3:
    print("-------Welcome In level : 3 -----------")
    tr_y=0
    computer=random.randint(1,50)
    while tr_y!=5:
        tr_y+=1
        
        user=int(input("Enter Number= "))
        
        if user>computer:
            print("hint : guess lower number")
        elif user<computer:
            print("Hint: Guess Upeer Number")
        else:
            print("You win")
            print("-----Level 3  Completed ---------")
            tr_y=5
            
    # elif choice==4:
    #     print("----------Thank You For Playing--------------------")
else:
   print("Invalid Input")
    

