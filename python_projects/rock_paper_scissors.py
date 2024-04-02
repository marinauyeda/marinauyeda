import random
import os

move_list = ["rock", "paper", "scissors"]
player_count = 0
computer_count = 0

print("================================")
print("Welcome to Rock, Paper, Scissors")
print("================================")

def main_print():
    print("================================")
    print("\nSCOREBOARD")
    print("You: {}".format(player_count))
    print("Computer: {}".format(computer_count))
    print("\n")
    print("Choose your move:")
    print("0 - Rock | 1 - Paper | 2 - Scissors")

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]

        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global player_count, computer_count

    if p_move == "paper":
        if c_move == "rock":
            player_count += 1
            return "p"

        elif c_move == "scissors":
            computer_count += 1
            return "c"

        else:
            return "d"
    
    if p_move == "rock":
        if c_move == "scissors":
            player_count += 1
            return "p"

        elif c_move == "paper":
            computer_count += 1
            return "c"
            
        else:
            return "d"

    if p_move == "scissors":
        if c_move == "paper":
            player_count += 1
            return "p"

        elif c_move == "rock":
            computer_count += 1
            return "c"
            
        else:
            return "d"

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print("")
    print("================================")
    print("Your move: {}".format(player_move.upper()))
    print("Computer move: {}".format(computer_move.upper()))

    if winner == "p":
        print("You win!")
    elif winner == "c":
        print("You lose!")
    else:
        print("It's a tie!")
    print("================================")

    while True:
        print("Play again?\n0 - YES | 1 - NO")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break
    os.system("clear")