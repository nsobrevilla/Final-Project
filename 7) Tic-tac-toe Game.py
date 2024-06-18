def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, mark):
    # Check rows, columns and diagonals
    return any(
        all(cell == mark for cell in row) for row in board
    ) or any(
        all(row[i] == mark for row in board) for i in range(3)
    ) or all(
        board[i][i] == mark for i in range(3)
    ) or all(
        board[i][2-i] == mark for i in range(3)
    )

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    
    board = [[" " for _ in range(3)]]
    
    current_player, current_mark = player1, 'X'
    
    while True:
        print_board(board)
        
        row = int(input(f"{current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"{current_player}, enter the column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_mark
            
            if check_winner(board, current_mark):
                print_board(board)
                print(f"Congratulations {current_player}! You have won!")
                break
            elif is_full(board):
                print_board(board)
                print("The game is a draw!")
                break
            
            # Switch players
            if current_player == player1:
                current_player, current_mark = player2, 'O'
            else:
                current_player, current_mark = player1, 'X'
        else:
            print("This position is already taken. Try again.")
        
if __name__ == "__main__":
    tic_tac_toe()
