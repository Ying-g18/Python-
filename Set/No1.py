# # #
# # #my_list = input("Enter a list : ").split()
# # #my_set = set(map(int, my_list))
# # # item = int(input("Enter what you want to remove : "))
# # # print(my_set)
# # #
# # # if item in my_set:
# # #     my_set.remove(item)
# # #     print(my_set)
# #
# #
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 4, 5, 6}
# #
# # #set_a = set_1 & set_2
# # #if set_1.issubset(set_2):
# #     #print("Yes")
# #
# # set_r = set_1.copy()
# # set_f = frozenset(set_1)
# #
# # print(set_f)
# #
# #
# if len(set_1 & set_2) > 0:
#     print("common")

#if set_2.issuperset(set_1):
    #print("Yes")
result = set_1 & set_2
print(set_1.difference(result))
