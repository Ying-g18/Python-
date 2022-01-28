
def check_fun(x):
    if x % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number : "))

if check_fun(num) is True:
    print(f"It is an even number ")
else:
    print(f"It is an odd number")
