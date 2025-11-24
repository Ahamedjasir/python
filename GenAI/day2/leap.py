year=int(input("enter the year"))
if year%400==0:
    print("leapyear",year)
elif year%100==0:
    print("not a leap year",year)
elif year%4==0:
    print("its a leap year",year)
else:
    print("not a leap year",year)



