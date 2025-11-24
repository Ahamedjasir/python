score=int(input("enter the score of student"))
if score>=85:
    print(" A grade",score)
elif score<85 and score>=65:
    print("B grade",score)
elif score<65 and score>=45:
    print(" C grade",score)
else:
    print("fail",score)