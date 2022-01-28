my_tuple = input("Enter a tuple : ").split()
my_tuple = list(map(int, my_tuple))

if len(my_tuple) >= 9:
    my_tuple.remove(my_tuple[0])
    my_tuple.remove(my_tuple[4])
    my_tuple.remove(my_tuple[5])
    print(my_tuple)
else:
    print("Please enter again ")



