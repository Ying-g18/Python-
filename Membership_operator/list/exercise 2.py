my_list = input("Enter a separated numbers for a list : ").split()
my_list = list(map(int , my_list))
temp = my_list[0]

for i in range(1,len(my_list)):
    if temp < my_list[i]:
        temp += my_list[i]
print(f"The sum of the numbers is : {temp}")