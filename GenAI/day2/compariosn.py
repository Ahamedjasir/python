num=int(input("enter the age"))
if num<16:
    print("you cant drive")
elif num>=16 and num<18:
    print("you can drive but no vote")
elif num>=18 and num<=24:
    print("you can vote but no rent a car")
else:
    print("you can do pretty much anything")
    