#take temparature from user check its value between 0 and 100 its called water if above 100 air and less than 0 cold
temparature=int(input("Enter Temparature= "))
if temparature>=0 and temparature<=100:
    print("water")
elif temparature>100:
    print("Air")
else:
    print("cold")