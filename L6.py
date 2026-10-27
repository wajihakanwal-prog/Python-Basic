day=input("what day is it ")
weather=input("what is the weather ")
homework=input("do you have homework ")
if day=="monday" and weather=="rainy" and homework=="yes":
    print("you should stay home")
elif day=="monday" and weather=="rainy" and homework=="no":
    print("you should go to school")
elif day=="monday" and weather=="sunny" and homework=="yes":
    print("you should stay home")
if day in ("Saturday","Sunday"):
    print("you should stay home")
if weather =="sunday" and homework=="no":
    print("you should go to school")
if weather=="sunny" and homework=="yes":
    print("you should go to school")
if weather=="rainy" or  weather=="cloudly":
    print("Weather tip : pack your umbrella")
if homework=="yes":
    print("homework tip : study hard")
else:
    print("homework tip : relax")
    