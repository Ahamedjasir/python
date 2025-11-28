size = 5

for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()


rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()


rows = 5

# upper part
for i in range(1, rows + 1):
    for s in range(rows - i):
        print(" ", end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()

# lower part
for i in range(rows - 1, 0, -1):
    for s in range(rows - i):
        print(" ", end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()
