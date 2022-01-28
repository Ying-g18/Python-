
while True:
    in_char = input("Enter a char : ")
    if in_char.isalpha():
        break
in_char = in_char.lower()

if in_char == 'a' or in_char == 'e' or in_char == 'i' or in_char == 'o' or in_char == 'u':
    print("It is a vowel")
else:
    print("It is a consonant")
