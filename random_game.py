
def correct_num(c):
    import random
    correct_number = random.randint(1, 100)

    while True:
        guess = int(input("Enter your guess : "))
        if guess < correct_number:
            print(f"Enter greater than {guess}")
            return False
        elif guess > correct_number:
            print(f"Enter less than {guess}")
            return False
        elif guess == correct_number:
            return True
            break
def main():
    player = int(input("Enter the number of player : "))
    i = 0
    while correct_num(i) is False:
        i += 1
        if correct_num(i) is True:
            break
    print(f"Congrats ! You guessed with {i} trials ")

if __name__ == "__main__":
    main()



