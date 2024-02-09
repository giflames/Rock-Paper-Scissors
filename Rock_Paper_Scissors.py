import random
import os

move_list = ["rock", "paper","scissors"]
player_count = 0
computer_count = 0


# Start game
print("================================\nWelcome to Rock, Paper, Scissors")


# Show points and choose move
def main_print():
    print("================================\n\nPOINTS:")
    print("Player: {}".format(player_count))
    print("Computer: {}".format(computer_count))

    print("\n\nChoose your move: 0 - Rock | 1 - Paper | 2 - Scissors")


# Computer move 
def select_move():
    return random.choice(move_list)

# player move 
def get_player_move():
    while True:
        try:
            player = int(input())
            if player not in [0, 1, 2]:
                raise ValueError("Invalid move. Please enter 0, 1, or 2.")
            return move_list[player]
        except ValueError as e:
            print(e)

# Win condition 
def select_winner(p_move, c_move):
    global player_count,computer_count

    if p_move == "paper":
        if c_move == "rock":
            player_count += 1
            return "p"
        elif c_move == "scissors":
            computer_count += 1
            return "c"
        else:
            return "d"
        
    elif p_move == "rock":
        if c_move == "scissors":
            player_count += 1
            return "p"
        elif c_move == "paper":
            computer_count += 1
            return "c"
        else:
            return "d"
        
    elif p_move == "scissors":
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

    print("\n\n================================\nPlayer's move: {}".format(player_move.upper())
          +"\nComputer's move: {}".format(computer_move.upper()))

    if winner == "d":
        print("Tie!")
    elif winner == "c":
        print("You lose!")
    elif winner =="p":
        print("You win!")
    
    print("================================")

    while True:
        print("Continue? 0 - YES | 1 - NO")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break

os.system("cls")
