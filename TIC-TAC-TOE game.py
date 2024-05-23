#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_board(board):
    for row in board:
        print(" || ".join(row))
        print("-" * 15)

def check_win(board, player):
    for i in range(3):
        # Check rows and columns for a win
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    # Initialization of the empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Assuming X starts
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        
        # Get player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        # Check if the chosen position is valid
        if board[row][col] != " ":
            print("Invalid move. The cell is already taken. Try again.")
            continue
            
        # Make the move
        board[row][col] = current_player
        
        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Call the function to start the game
tic_tac_toe()




# In[ ]:




