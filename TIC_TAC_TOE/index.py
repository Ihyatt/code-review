def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        # Introducing a bug by mistakenly checking for all columns in rows
        if all(board[j][i] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Introducing a bug by changing the condition for winning diagonally
    if all(board[i][i] == player for i in range(3)) or all(board[i][i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Introducing a bug by checking for empty cells using '==' instead of '!='
    return all(cell == " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

        # Introducing a bug by swapping row and column indices
        if 0 <= col < 3 and 0 <= row < 3 and board[row][col] == " ":
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()