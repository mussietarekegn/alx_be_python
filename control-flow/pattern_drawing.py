size = int(input("Enter the size of the pattern: "))
n = size
while size > 0:
    for i in range(n):
        print("*", end="")
    print()
    size-=1

