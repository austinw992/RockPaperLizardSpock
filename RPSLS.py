import random

#Scissors Cuts Paper
#Paper Covers Rock
#Rock crushes Lizard
#Lizard Poisons Spock
#Spock smashes Scissors
#Scissors decaptitates Lizard
#Lizard eats Paper
#Paper idsproves Spock
#Spock Vaporizes Rock
#Rock crushes Scissors

Options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
Computer = random.choice(Options)
Player = False

Computer_Score = 0
Player_Score = 0

while True:
    Player = input("Rock, Paper, Lizard, Spock or Scissors? ").capitalize()

    if Player == Computer:
        print("Tie!")
    elif Player == "Rock":
        if Computer == "Paper":
            print("You Lose", Computer, "covers", Player)
            Computer_Score += 1
        elif Computer == "Spock":
            print("you lose", Computer, "vaporizes", Player)
            Computer_Score += 1
        else:
            print("YOu win", Player, "smashes", Computer)
            Player_Score += 1
    elif Player == "Paper":
        if Computer == "Scissors":
            print("you Lose", Computer, "cut", Player)
            Computer_Score += 1
        elif Computer == "Lizard":
            print("you lose", Computer, "eats", Player)
            Computer_Score += 1
        else:
            print("you win", Player, "covers", Computer)
            Player_Score += 1
    elif Player == "Scissors":
        if Computer == "Rock":
            print("you lose", Computer, "smashes", Player)
            Computer_Score += 1
        elif Computer == "Spock":
            print("you lose", Computer, "smashes", Player)
            Computer_Score += 1
        else:
            print("you win", Player, "cut", Computer)
            Player_Score += 1
    elif Player == "Lizard":
        if Computer == "Rock":
            print("You Lose", Computer, "crushes", Player)
            Computer_Score +=1
        elif Computer == "Scissors":
            print("You lose", Computer, "decapitates", Player)
            Computer_Score += 1
        else:
            print("you win", Player, "poisons", Computer)
            Player_Score += 1
    elif Player == "Spock":
        if Computer == "Lizard":
            print("You lose", Computer, "poisons", Player)
            Computer_Score += 1
        elif Computer == "Paper":
            print("You lose", Computer, "disproves", Player)
            Computer_Score += 1
        else:
            print("you win", Player)

    elif Player == "End":
        print("Final Scores")
        print(f"Computer: {Computer_Score}")
        print(f"Player: {Player_Score}")
        break
