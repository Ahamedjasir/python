#  f=open("example.txt","w")
#  f.write("Hello!World")
#  f.close()

# with open("example.txt","r") as f:
 #     content=f.read()
 # print(content)

 # f=open("example.txt","a")
 # f.write("\n Iam!Jasir")
 # f.close()

# f=open("example.txt","r")
# for line in f:
#     print(line,end="")
# f.close()

# line=["NAME=Ahamed\n","AGE=22\n","From=Thittuvilai\n","Eduction=BE CSE\n"]
# f=open("example.txt","w",)
# f.writelines(line)
# f.close()

# import os
# if os.path.exists("example.txt"):
#     print("file Exist")
# else:
#     print("not exist")
# print(os.getcwd())

# import os
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("file deleted")
# else:
#     print("file not found")

# import os
# if not os.path.exists("example.txt"):
#     f=open("example.txt","w")
#     f.write("file created successfully.\n")
#     f.close()

# import shutil
# shutil.copy("example.txt","copy_example.txt")
# student=[{"name":"jasir","age":22,"cource":"cse"},
#          {"name":"hari","age":22,"cource":"cse"}]
# print(student[0])
# print(student[1]["name"])
# # print(student["age"])


# try:
#     a=int(input("enter the first number"))
#     b=int(input("enter the second number"))
#     result=a/b
#     print("result",result)
# except ZeroDivisionError:
#     print("cannot divided by zero")
# except ValueError:
#     print("plzz enter the correct value")
# finally:
#     print("program done correctly")

try:
    age=int(input("enter your age"))
    if age<18:
        raise Exception("age must be 18 or above")
    print("elligible")

except Exception as e:
    print("Error",e)