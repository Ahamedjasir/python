numbers = [12, -5, 7, -19, 0, 25, -3]

positive = []
negative = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
