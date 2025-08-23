import random

while True:
    print("1. Level 1(1-100) Unlimited Chance")
    print("2. Level 2(1-100) You Chose Limit Of Chance ")
    print("3. Level 3(1-100) 10 Chance only")
    print("4. Level 4(1-100) 5 Chance Only")
    print("5. Level 5(1-50) 5 chance only")
    print("6. Level 6(1-50) 3 chance only")
    # print("if you won all level then you called a genius")
    choice=int(input("ENter Your choice= "))
    computer=random.randint(1,100)
    if choice==1:
        print("-------Welcome to level  1------------")
        while True:
            user=int(input("Enter Number= "))
            if user>100 or user<0:
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
        for i in range(0,limit):
            print(f"Current Chance= {i+1}/{limit}")
            user=int(input("Enter Number= "))
            if user>100 or user<0:
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
            
    
    else:
        print("Invalid input")

 


