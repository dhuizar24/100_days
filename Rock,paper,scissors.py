from random import randint
rps = int(input("Let's play rock paper scissors, 0 for rock, 1 for paper, 2 for scissors"))

if rps == 0:
    print("You selected Rock")
elif rps == 1:
    print("You selected Paper")
elif rps == 2:
    print("You selected Scissors")
else:
    print("Please select numbers 0,1, or 2.")


computer_rps = randint(0, 2)

if computer_rps == 0:
    print("Computer selected Rock")
elif computer_rps == 1:
    print("Computer selected Paper")
else:
    print("Computer selected Scissors")

if rps == 0 and computer_rps == 1:
    print("You lose")
elif rps == 0 and computer_rps == 2:
    print("You win")
elif rps == 1 and computer_rps == 2:
    print("You Lose ")
elif rps == 1 and computer_rps == 0:
    print("You win")
elif rps == 2 and computer_rps == 0:
    print("You lose")
elif rps == 2 and computer_rps == 1:
    print("You win")
else:
    print("Tie Game")