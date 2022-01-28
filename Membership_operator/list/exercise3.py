my_list = input("Enter a separated numbers for a list : ").split()
my_list = list(map(int , my_list))
temp = my_list[0]

for i in range(len(my_list),1):
    if temp > my_list[i]:
        temp = my_list[i]
print(f"The minimum of the numbers is : {temp}")