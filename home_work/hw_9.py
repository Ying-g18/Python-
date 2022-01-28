print("The given tuple is (1,2,3,4,5,6,7,8,9) ")
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_item = int(input("Enter a number : "))

for item in my_tuple:
    if item == my_item:
        print("Exist")
