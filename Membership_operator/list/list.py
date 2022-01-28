
my_list = input("Enter a separated numbers : ").split()
list_1 = list(map(int, my_list))
temp = my_list[0]

for i in range(1, len(my_list), 1):
    if temp < my_list[i]:
        temp = my_list[i] 
print(f"The maximum number is {temp}")











