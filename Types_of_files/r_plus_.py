
my_file = open("Hi.txt", "r+")
my_text = my_file.read()
print(my_text)
tx = input("Write something : ")
my_file.write(tx)
my_file.close()

