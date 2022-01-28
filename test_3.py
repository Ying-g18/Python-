
my_list = input("Enter a list : ").split()
temp = list(my_list)
rotate = int(input("Enter the number of time : "))

tp = []
for i in range(1,rotate+1):
    tp.append(temp[-i])
for j in range(len(my_list)-rotate):
    tp.append(temp[j])

print(tp)
