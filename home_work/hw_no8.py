
my_tuple = input("Enter a tuple [ must be more than 5] :").split()
my_tuple = tuple(map(int, my_tuple))
print(my_tuple)
if len(my_tuple) >= 5:
    print(my_tuple[3])
    print(my_tuple[-4])
else:
    print("Enter again")
