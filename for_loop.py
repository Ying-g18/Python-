n = int(input("Enter number of time while it is >1 and <=5 : "))
if (n > 1) & (n <= 5):
    i = 1
    for i in range(1, 11, 1):
        for j in range(1, n+1, 1):
            print(f"{j} * {i} = {i*j}\t", end="")
        print()
else:
    print(f"Please enter again")
