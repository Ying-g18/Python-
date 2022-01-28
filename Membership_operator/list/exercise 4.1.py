tp = []

my_tuple = input("Enter a tuple : ").split()
my_tuple = tuple(map(int, my_tuple))
tp.append(my_tuple)
if my_tuple == ():
    print("Tuple is empty ")
else:
    print(my_tuple)




