
people = int(input("How many people : "))
my_dicto = {}
for i in range(people):
    keys = input("Enter a key : ")
    values = input("Enter a value : ")
    # my_dicto.update({keys : values})
    # my_dicto[keys] = values
    my_dicto.setdefault(keys, values)
print(my_dicto)