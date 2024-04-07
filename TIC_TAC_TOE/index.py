
from collections import defaultdict


rows = {0: {'X':0, 'O':0}, 1:{'X':0, 'O':0}, 2: {'X':0, 'O':0}}
cols = {0: {'X':0, 'O':0}, 1:{'X':0, 'O':0}, 2: {'X':0, 'O':0}}
diag_left = {'X':0, 'O':0}
diag_right = {'X':0, 'O':0}


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(player):
    for i in range(3):
        if rows[i][player] == 3:
            return True
        if cols[i][player] == 3:
            return True
    return  diag_left[player] == 3 or diag_right[player] == 3

def main():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    remaining_cells = 9

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

        if 0 <= col < 3 and 0 <= row < 3 and board[row][col] == " ":
            board[row][col] = player
            rows[row][player] += 1
            cols[col][player] += 1
            if col == row:
                diag_left[player] += 1
            if row + col == 2:
                diag_right[player] += 1


            remaining_cells -= 1

            if check_winner(player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if remaining_cells == 0:
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
   