
my_file = open("Hi.txt", "a")

#my_text = my_file.read()
#my_text = my_file.readline()
my_text = input("Enter a line : ")
#my_text = input("Enter a line : ").split(",")
#w_line = my_file.writelines(my_text)
w_line = my_file.write("\n" +my_text + "\n")

my_file.close()
