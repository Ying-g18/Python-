def triple(num):
    if num * 3 == 15 or num * 3 == 18:
        return num
    else:
        return num * 3

li = [1, 2, 3, 4, 5]
print(li)

li = list(map(triple, li))
print(li)
