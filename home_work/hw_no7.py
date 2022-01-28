my_tuple = (1, 2, 3, 4, 5)
temp = list(my_tuple)

print(temp)
for item in my_tuple:
    location = temp.index(item)
    print(f"Location of {item} is {location}")
