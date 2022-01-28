n = int(input("Enter a positive integer : "))
if_prime = True
counter = 0
while if_prime is True:
    for i in range(2, n, 1):
        counter += 1
        k = n % i
        if k != 0:
            if_prime = False
        elif counter == n - 1:
            if_prime = True
    break

if if_prime is False:
    print("It is a prime number")
else:
    print("It is not a prime number")












