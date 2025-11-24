# def hello(name):
#     return f"hello!{name}"
# print(hello("praveen"))

# def add(a,b):
#     return a+b
# print(add(5,8))

# def mul(a,b):
#     return a*b
# print(mul(5,5))

# def div(a,b):
#     return a/b
# print(div(25,5))

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print("Factorial of 3 is:", factorial(3))
# print("Factorial of 5 is:", factorial(5))
# print("Factorial of 7 is:", factorial(7))


# def square(a):
#     return a*a
# print("square of the :", square(3))
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
