
my_input = input("Enter a string : ")

my_palindrome = my_input[::-1]
if my_palindrome == my_input:
    print("It is  a palindrome ")
else:
    print("It is not a palindrome ")
