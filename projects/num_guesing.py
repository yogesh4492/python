import random
print(" \033[91m Note : There Are Only 5  Fixed Attempts For Guessing Number\033[0m ")
print(" \033[91m Note : If You Want To Choice Attempts By Yourself \033[92m Press 10  otherwise Press 0 .\033[0m")
ch=int(input("Enter choice= "))
print("1. Easy   (1-25)")
print("2. Medium (1-50)")
print("3. Hard   (1-100)")
i=1
choice=int(input("Enter Which Level Do You Want To Play= "))
if ch==10:
    Attemp=int(input("Enter Number of Attemp You Want To Take For Guess= "))
    if choice==1:
        print(" ---------Welcome to Easy Level --------- ")
        ran_num=random.randint(1,25)
        for i in range(1,Attemp+1):
            print(f"Number of Attemps:{i}/{Attemp}")
            num=int(input("Enter Number= "))
            if num>=1 and num<=25:
                if num>ran_num:
                    if i==Attemp:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To High ") 
                elif num<ran_num:
                    if i==Attemp:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To Low ") 
                elif num==ran_num:
                    print("You Won the Game")
                    break
            else:
                print("Your Range is 1-25 So Please Guess Between It To Won The Game ")
    elif choice==2:
        print(" ---------Welcome to Medium Level --------- ")
        ran_num=random.randint(1,50)
        for i in range(1,Attemp+1):
            print(f"Number of Attemps:{i}/{Attemp}")
            num=int(input("Enter Number= "))
            if num>=1 and num<=50:
                if num>ran_num:
                    if i==Attemp:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To High ") 
                elif num<ran_num:
                    if i==Attemp:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To Low ") 
                elif num==ran_num:
                    print("You Won the Game")
                    break
            else:
                print("Your Range is 1-50 So Please Guess Between It To Won The Game ")
    elif choice==3:
        print(" ---------Welcome to Hard Level --------- ")
        ran_num=random.randint(1,100)
        for i in range(1,Attemp+1):
            print(f"Number of Attemps:{i}/{Attemp}")
            num=int(input("Enter Number= "))
            if num>=1 and num<=100:
                if num>ran_num:
                    if i==Attemp:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To High ")
                elif num<ran_num:
                    if i==Attemp:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To Low ")   
                elif num==ran_num:
                    print("You Won the Game ")
                    break
            else:
                print("Your Range is 1-100 So Please Guess Between It To Won The Game ")        
    else:
        print("Invalid Input")
elif ch==0:
    if choice==1:
        print(" ---------Welcome to Easy Level --------- ")
        ran_num=random.randint(1,25)
        for i in range(1,6):
            print(f"Number of Attemps:{i}/5")
            num=int(input("Enter Number= "))
            if num>=1 and num<=25:
                if num>ran_num:
                    if i==5:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To High ")
                elif num<ran_num:
                    if i==5:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To Low ")
                elif num==ran_num:
                    print("You Won the Game")
                    break
            else:
                print("Your Range is 1-25 So Please Guess Between It To Won The Game ")
    elif choice==2:
        print(" ---------Welcome to Medium Level --------- ")
        ran_num=random.randint(1,50)
        for i in range(1,6):
            print(f"Number of Attemps:{i}/5")
            num=int(input("Enter Number= "))
            if num>=1 and num<=50:
                if num>ran_num:
                    if i==5:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To High ")
                elif num<ran_num:
                    if i==5:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To Low ")
                elif num==ran_num:
                    print("You Won the Game")
                    break
            else:
                print("Your Range is 1-50 So Please Guess Between It To Won The Game ")
    elif choice==3:
        print(" ---------Welcome to Hard Level --------- ")
        ran_num=random.randint(1,100)
        for i in range(1,6):
            print(f"Number of Attemps:{i}/5")
            num=int(input("Enter Number= "))
            if num>=1 and num<=100:
                if num>ran_num:
                    if i==5:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To High ")
                elif num<ran_num:
                    if i==5:
                        print("You Lose the Game")
                        print(f"Number is = {ran_num} Better Luck Next Time")
                    else:
                        print(" To Low ") 
                elif num==ran_num:
                    print("You Won the Game ")
                    break
            else:
                print("Your Range is 1-100 So Please Guess Between It To Won The Game ")        
    else:
        print("Invalid Input")
else:
    print("Enter Valid Choice")