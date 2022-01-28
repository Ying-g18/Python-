
no_of_player = int(input("Enter the number of player : "))

my_score = {}
for i in range(no_of_player):
    my_player = input("Enter player name : ")
    my_score[my_player] = int(input("Enter score : "))
    my_score.setdefault(my_player)
print(my_score)


