from random import sample
from colorama import Fore
from pyfiglet import figlet_format
from time import sleep
from os import system

def board(row_index, col_index, move):
    if not (0 <= row_index <= 2) or not (0 <= col_index <= 2) or move not in ["X", "O"]:
        if not (0 <= row_index <= 2):
            print("Row must be 0, 1, or 2")

        elif not (0 <= col_index <= 2):
            print("Column must be 0, 1, or 2")

        else:
            print("Choose play X or O")
        return

    if tictactoe_board[row_index][col_index] == "#":
        tictactoe_board[row_index][col_index] = move

    else:
        print("This location is not empty")
    
    for row in tictactoe_board:
        print(Fore.LIGHTGREEN_EX)
        print("\t\t"+"\t".join(row))
        print(Fore.LIGHTBLUE_EX)


def check_win(tic_tac_toe_board):
    for row in tic_tac_toe_board:
        if row[0] == row[1] == row[2] and row[0] != "#":
            return row[0]

    for i in range(3):
        if tic_tac_toe_board[0][i] == tic_tac_toe_board[1][i] == tic_tac_toe_board[2][i]:
            if tic_tac_toe_board[0][i] != "#":
                return tic_tac_toe_board[0][i]

    if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2]:
        if tic_tac_toe_board[0][0] != "#":
            return tic_tac_toe_board[0][0]

    if tic_tac_toe_board[0][2] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][0]:
        if tic_tac_toe_board[0][2] != "#":
            return tic_tac_toe_board[0][2]

    for row in tic_tac_toe_board:
        if "#" in row:
            return None

    return "Draw"

startup = figlet_format("Tic Tac Toe")
print(Fore.YELLOW)
print(startup)
print(Fore.LIGHTBLUE_EX)

player_score = 0
computer_score = 0
draw = 0

while True:
    if player_score == 3 or computer_score == 3:
        break
    tictactoe_board = [
        ["#",   "#",   "#"],
        ["#",   "#",   "#"],
        ["#",   "#",   "#"],
    ]
    for row in tictactoe_board:
        print(Fore.LIGHTGREEN_EX)
        print("\t\t"+"\t".join(row))
        print(Fore.LIGHTBLUE_EX)

    print("-"*50)
    while True:
        try:
            print("Choose play X or O")
            player_move = input("Player - Move:").upper()
            row_index = int(input("Player -  Row:"))
            col_index = int(input("Player -  Col:"))
            print("-"*50)
            board(row_index, col_index, player_move)
            computer_moves = [0, 1, 2]
            cpu_move = ""
            while True:
                if player_move == "X" or player_move == "O":
                    cpu_row_index = sample(computer_moves, 1)
                    cpu_col_index = sample(computer_moves, 1)
                    sleep(0.25)

                    if player_move == "X":
                        cpu_move = "O"

                    elif player_move == "O":
                        cpu_move = "X"

                    if tictactoe_board[cpu_row_index[0]][cpu_col_index[0]] == "#":
                        print("-"*50)
                        print(f"Computer - Move: {cpu_move}")
                        print(f"Computer - Row:  {int(cpu_row_index[0])}")
                        print(f"Computer - Col:  {int(cpu_col_index[0])}")
                        print("-"*50)
                        board(int(cpu_row_index[0]), int(
                            cpu_col_index[0]), cpu_move)
                        break

                    if check_win(tictactoe_board):
                        break
                else:
                    break

            winner = check_win(tictactoe_board)
            if winner is not None:
                if winner == "Draw":
                    draw += 1
                    print("Draw")
                    break
                else:
                    player_score += 1
                    print(f"Player {winner} wins!")
                    break

            if check_win(tictactoe_board):
                computer_score += 1
                print(f"Computer - {cpu_move} wins!")
                break

        except Exception as e:
            print(e)

    print(f"Player score:   {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Game Draw:      {draw}")
    input("Enter to continue...")
    system("cls")