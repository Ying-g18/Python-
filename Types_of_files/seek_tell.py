
f = open("Hi.txt", "rt")
while True:
    print(f.readline())
    if len(f.tell) == 0