
f = open("Hi.txt", "w+")
choice = input("True of False[t/f] : ")
length = int(input("How many lines : "))
if choice.lower() == "t":
    for i in range(1, length+1):
        for j in range(i):
            f.write("* ")
        f.write("\n")
if choice.lower() == "f":
    for i in range(length, 0, -1):
        for j in range(i):
            f.write("* ")
        f.write("\n")