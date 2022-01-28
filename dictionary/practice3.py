
my_dict = {'Myan': int(input('Myanmar marks: ')), 'Eng': int(input('English marks : ')), 'Maths': int(input('Mathematics mark : '))}
sum = 0
for values in my_dict.values():
    sum += values

print(f"Total : {sum}")
