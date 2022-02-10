with open("Hi.txt", "a+") as f:
    choice = input("Enter what do you want to do [read, borrow, return]: ")

    if choice.lower() == "borrow":
        book = input("Enter the name of book you want to borrow : ")
        f.seek(0)
        available = f.readlines()
        temp = []
        for item in available:
            temp.append(item.split("-"))
        for i in range(len(temp)):
            if book.lower() == temp[i][0]:
                temp.pop(i)
        print(temp)
    elif choice.lower() == "return":
        book = input("Enter the name of book you want to return : ")
        author = input("Enter the book's author : ")
        f.write("\n")
        f.write(f"{book} , {author}")

    elif choice.lower() == "read":
        book = input("Enter the name of book you want to read : ")
        f.seek(0)
        available = f.readlines()
        temp = []
        for item in available:
            temp.append(item.split("-"))
        for i in range(len(temp)):
            if book.lower() in temp[i][0]:
                print(f"{book} written by {temp[i][1]}")




