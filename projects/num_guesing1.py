import random
while True:
    print(" \033[91m Note : There Are Only 5  Fixed Attempts For Guessing Number\033[0m ")
    print(" \033[91m Note : If You Want To Choice Attempts By Yourself \033[92m Press 10 Othrwise Press Any Number .\033[0m")
    ch=int(input("Enter choice= "))
    Attemp=5
    if ch==10:
        Attemp=int(input("Enter Number of Attemp You Want To Take For Guess= "))
    print("1. Easy   (1-25)")
    print("2. Medium (1-50)")
    print("3. Hard   (1-100)")
    i=1
    choice=int(input("Enter Which Level Do You Want To Play= "))
    if choice==1:
        max_val=25
        print("---------Welcome to Easy Level---------")
    elif choice==2:
        max_val=50
        print("---------Welcome to Medium Level---------")
    elif choice==3:
        max_val=100
        print("---------Welcome to Hard Level---------")
    else:
        print("Invalid Input")
        exit()

    ran_num=random.randint(1,max_val)

    for i in range(1,Attemp+1):
                print(f"Number of Attemps:{i}/{Attemp}")
                num=int(input("Enter Number= "))
                if num>=1 and num<=max_val:
                    if num>ran_num:
                        if i==Attemp:
                            print("You Lose the Game")
                            print(f"Number is = {ran_num} Better Luck Next Time")
                        else:
                            print(" Too High ") 
                    elif num<ran_num:
                        if i==Attemp:
                            print("You Lose the Game")
                            print(f"Number is = {ran_num} Better Luck Next Time")
                        else:
                            print(" Too Low ") 
                    elif num==ran_num:
                        print("You Won the Game")
                        break
                else:
                    print(f"Your Range is 1-{max_val} So Please Guess Between It To Won The Game ")
    again=input("Do You Want To Play Again.(y/n)=")
    if again=='n' or again=='N':
      print(" Thank You For Playing ")
      break
     
