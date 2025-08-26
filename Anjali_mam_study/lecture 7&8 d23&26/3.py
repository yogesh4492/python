import random
status=True
while status:
    level1=random.randint(1,100)
    level_complete=True
    # print(level1)
    while level_complete:
        num=int(input("Enter Number= "))
        if num>level1:
            print("hint : to high")
        elif num<level1:
            print("Hint: To Low ")
        else:
            print("You Win!!")
            status=False
            level1_complete=True
            level_complete=False
if status==False and level1_complete==True:
    print("Level 1 completed")
    print("Welcome In level 2 ")
    print("You HAve Only 7 Trys for guessing\n")
    level2=random.randint(1,100)
    level2_complete=False
    tri=0
    # print(level2)
    for i in range(7,0,-1):
         tri+=1
         num=int(input("Enter Number= "))
         if num>level2:
             print("Hint: To High")
         elif num<level2:
             print("Hint: To Low")
         else:
             print("You Win!!")
             level2_complete=True
             break
    if tri==7:
        print(f"num is {level2} Your Try Is Completed ")
        status=False
if  level2_complete:
    print("Level 2 completed")
    print("Welcome In level 3 ")
    print("You HAve Only 5 Trys for guessing\n")
    level3=random.randint(1,100)
    level3_complete=False
    tri=0
    # print(level3)
    for i in range(5,0,-1):
         tri+=1
         num=int(input("Enter Number= "))
         if num>level3:
             print("Hint: To High")
         elif num<level3:
             print("Hint: To Low")
         else:
             print("You Win!!")
             level3_complete=True
             break
    if tri==5:
        print(f"num is {level3} Your Try Is Completed ")
        status=False
if level1_complete and level2_complete and level3_complete:
    print("Congratulation !!!You Won All Levels ")