char=input("enter the letter ")
match char.lower():
  case "a"|"e"|"i"|"o"|"u":
    print("vowels")
  case _:
    print("consonant")