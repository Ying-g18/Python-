
my_tuple = list(map(int, input("Enter a tuple : ").split()))
temp = my_tuple.copy()
print(temp)
result = []

for item in temp:
    print(temp.count(item))
    if temp.count(item) > 1 and item not in result:
        result.append(item)
print(f"The repeated item is {result}")
