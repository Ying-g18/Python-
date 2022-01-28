
input_string = 'p1=haru p2=kio p3=sara'
my_list = []
for item in input_string.split():
    temp = item.split("=")
    print(temp)
    my_list.append(temp)

my_dict = dict(my_list)
print(my_dict)
