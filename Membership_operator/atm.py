
b = 10000
print(f"choose :")
choice = int(input("1.deposit\n2.withdraw\n3.balance inquiries\n4.quit\n:"))
if choice==1:
    a = int(input("Enter amount of deposit : "))
    print(f"deposit = {a}")
elif choice==2:
    w = int(input("Enter withdraw amount : "))
    k=b-w
    if b-w >=100:
        print(f"withdraw : {w}\n remain balance : {k}")
    else:
        print(f"insufficient balance")
elif choice==3:
    print(f"available balance: {b}")
elif choice==4:
    print("Thanks")

