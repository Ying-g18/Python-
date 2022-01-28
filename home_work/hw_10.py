my_tuple = input("Enter a tuple : ").split()
my_tuple = tuple(map(int, my_tuple))
my_tuple = my_tuple[::-1]
print(my_tuple)