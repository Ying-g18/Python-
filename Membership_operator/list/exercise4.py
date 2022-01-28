result = []
want = int(input("How many tuple do you need in a list :"))

for i in range(want):
    tup = tuple(map(int, input("Enter numbers : ").split()))
    result.append(tup)

print(result)
temp_list = result.copy()

ans = []
for j in range(len(temp_list)):
    max = temp_list[0]
    for i in range(len(temp_list)):
        if temp_list[i][-1] > max[-1]:
            max = temp_list[i]
    ans.append(max)
    temp_list.remove(max)
print(ans)


