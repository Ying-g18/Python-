
# with open("Hi.txt", "a") as f:
#     my_char = input("Enter any char : ")
#     f.write(my_char)

#No.2

# try:
#     f = open("Hello.txt", "rt")
#     if f is None:
#         print("File not found")
# except FileNotFoundError as q:
#     print("File not found ")
#     print(q)

#No.3
#my_para = input("Enter any string: ")

#with open("Hi.txt", "r") as f:
#     f.write(my_para)

#No.4
    #my_text = f.read()
    #print(my_text)
#No.5
#my_name = input("Enter your name : ")
#my_phone = input("Enter your phone number : ")

#with open("Hi.txt", "r") as file:
    #file.write(f"name : {my_name}\n phone number : {my_phone}")

#No.6
    # my_line = file.readlines()
    # for line in my_line:
    #     no_of_line = len(my_line)
    # print(f"The number of line is {no_of_line}")
    # word = 0
    # for line in my_line:
    #     word += len(line.split())
    # print(f"Number of word is {word}")
    # character = 0
    # for line in my_line:
    #     character += len(line)
    # print(f"The number of character is {character}")
#No.7
#with open("Hi.txt", "r+") as f:
#     my_text = input("Enter any words :  ")
#     f.write(my_text + "\n")
#     f.seek(0)
#     temp = f.read()
#     print(temp)
#No.8
# with open("temp.txt", "a+") as file:
#     f = open("Hi.txt", "r")
#     temp = f.readlines()
#     for line in temp:
#          file.write(line)
#
#No.12
# with open("Hi.txt", "r") as f:
#     city = input("Enter the city name : ")
#     lines = f.readlines()
#     for line in lines:
#         if city.lower() in line:
#             break
#No.13
# with open("Hi.txt", "rb+") as f:
#     my_text = map(int, input("Enter a number : ").split(" "))
#     f.write(bytearray(my_text))
#     f.seek(0)
#     temp = f.read()
#     print(temp)


