num1=int(input("enter the first number"))
num2=int(input("second number "))
fun=input("enter the aritmetic function")
if fun=='s':
    u=num1-num2
elif fun=='a':
    u=num1+num2
elif fun=='m':
    u=num1*num2
elif fun=='d':
    u=num1/num2
else:
    print("enter the correct Aritmetic function")
    exit()
print("the arithmetic function is:",fun)
print("the answer is :",u)