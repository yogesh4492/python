import random

while True:
    print("1. Level 1(1-100) Unlimited Chance")
    print("2. Level 2(1-100) You Chose Limit Of Chance ")
    print("3. Level 3(1-100) 10 Chance only")
    print("4. Level 4(1-100) 5 Chance Only")
    print("5. Level 5(1-50) 5 chance only")
    print("6. Level 6(1-50) 3 chance only")
    print("7. Exit ")
    choice=int(input("ENter Your choice= "))
    computer=random.randint(1,100)
    count=0
    if choice==1:
        print("-------Welcome to level  1------------")
        while True:
            user=int(input("Enter Number= "))
            if user>100 or user<=0:
                print("Invalid range guess please guess In your range For Winning")
            else:
                if user>computer:
                    print("Hint: To High")
                elif user<computer:
                    print("Hint: To Low")
                else:
                    print("You Win !!!")
                    print("--------Level 1 completed----------")
                    break
    elif choice==2:
        print("-----Welcome to level 2---------")
        limit=int(input("Enter Number of Chance= "))
        print()
        for i in range(1,limit+1):
            print(f"Current Chance= {i}/{limit}")
            user=int(input("Enter Number= "))
            if user>100 or user<=0:
                print("Invalid range please guess in your range to win")
            else:
                if user>computer:
                    print("Hint : To High")
                elif user<computer:
                    print("Hint: To Low")
                else:
                    print("You win")
                    print("--------Level 2 Completed-----------")
                    print()
                    break
    elif choice==3:
        print("-------Welcome to level 3---------")
        limit=10
        print()
        for i in range(1,limit+1):
            print(f"Current Chance= {i}/{limit}")
            user=int(input("Enter Number= "))
            if user>100 or user<=0:
                print("Invalid range please guess in your range to win")
            else:
                if user>computer:
                    print("Hint : To High")
                elif user<computer:
                    print("Hint: To Low")
                else:
                    print("You win")
                    print("--------Level 3 Completed-----------")
                    print()
                    break
    elif choice==4:
        print("-------Welcome to level 4-------")
        limit=5
        print()
        for i in range(1,limit+1):
            print(f"Current Chance= {i}/{limit}")
            user=int(input("Enter Number= "))
            if user>100 or user<=0:
                print("Invalid range please guess in your range to win")
            else:
                if user>computer:
                    print("Hint : To High")
                elif user<computer:
                    print("Hint: To Low")
                else:
                    print("You win")
                    print("--------Level 4 Completed-----------")
                    print()
                    break
    elif choice==5:
        print("-----Welcome to level 5------")
        computer=random.randint(1,50)
        limit=5
        for i in range(1,limit+1):
            print(f"Current Chance= {i}/{limit}")
            user=int(input("Enter number= "))
            if user>50 or user<=0:
                print("invalid Range please guess in range to win")
            else:
                if user>computer:
                    print("Hint: To High")
                elif user<computer:
                    print("Hint: To Low")
                else:
                    print("You Win!!!")
                    print("-------------level 5 completed-----")
                    break
    elif choice==6:
        print("-----Welcome to level 6---------")
        computer=random.randint(1,50)
        limit=3
        for i in range(1,limit+1):
            print(f"Current Chance= {i}/{limit}")
            user=int(input("Enter Number= "))
            if user>50 or user<=0:
                print("invalid range input")
            else:
                if user>computer:
                    print("Hint: To High ")
                elif user<computer:
                    print("Hint: To Low")
                else:
                    print("You win !!!")
                    print("Level 6 completed")
                    break   
    elif choice==7:
        print("--------Thank You For Playing------------")
        break         
    else:
        print("Invalid input")

 


