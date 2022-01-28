
my_dict = {'p2': 'Alice','p1': 'Kio', 'p3' : 'John'}

my_dicti = sorted(my_dict.items(), key=lambda x: x[0])
temp = dict(my_dicti)
print(temp)
