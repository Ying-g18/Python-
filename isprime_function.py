
def check_prime(num):
    for i in range(2, int(num/2)+1, 1):
        if num % i == 0:
            return False
    return True

def main():
        start = int(input("Enter the starting point : "))
        stop = int(input("Enter the end point : "))

        for i in range(start, stop+1, 1):
            if check_prime(i) is True:
                print(i, end=" ")
        print()


if __name__ == "__main__":
    main()
