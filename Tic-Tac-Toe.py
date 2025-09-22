import random

# The game board and logic for a simple Tic-Tac-Toe game

#The game board is represented as a list of 9 elements and as a string
    
board = ["1","2","3","4","5","6","7","8","9"]
current_player = 'X'  # Player always starts first
game_over = False

def print_board():
    """Prints the current state of the game board in a 3x3 grid format."""
    
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(player):
    # Checks if the specified player has won the game.
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Row
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # column
            (0, 4, 8), (2, 4, 6)] # diagonal
    
    for combo in wins:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def check_tie():
    # Checks if the game has ended in a tie.
    for position in board:
        if position.isdigit():
            return False
    return True

def check_winner_on_board(player, board_state):
# Checks if the specified player has won on the given board state.
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Row
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # column
            (0, 4, 8), (2, 4, 6)] # diagonal
    
    for combo in wins:
        if board_state[combo[0]] == player and board_state[combo[1]] == player and board_state[combo[2]] == player:
            return True
    return False

# simple AI agent logic for the computer player
def Ai_move():
    #AI agent logic determine the best move
    available_moves = [i for i, spot in enumerate(board) if spot.isdigit()]
    print("available moves before AI plays: ", available_moves)

# check for winning move for the AI ('0')
    for i in available_moves:
        board_copy = board[:]
        board_copy[i] = 'O'
        if check_winner_on_board('O', board_copy):
            board[i] = 'O'
            print("AI plays winning move at", i+1)
            return 

# check for winning move for the player ('X')
    for i in available_moves:
        board_copy = board[:]
        board_copy[i] = 'X'
        if check_winner_on_board('X', board_copy):
            board[i] = 'O'
            print("AI blocks player's at", i+1)
            return
        
# take the center if available
    if 4 in available_moves:
        board[4] = 'O'
        print("AI takes center")
        return
    
# take a corner if available
    corners = [c for c in [0, 2, 6, 8] if c in available_moves]
    if corners:
        move = random.choice(corners)
        board[move] = 'O'
        print("AI takes corner at", move+1)
        return 
    
# take a side spot if available
    sides = [s for s in [1, 3, 5, 7] if s in available_moves]
    if sides:
        move = random.choice(sides)
        board[move] = 'O'
        print("AI takes side at", move+1)
        return 

# fallback (shouldn't be needed but safe)
    if available_moves:
        move = random.choice(available_moves)
        board[move] = 'O'
        print("AI fallback move at", move+1)

# The main game loop

# Initialize game state variables

while not game_over:
    print_board()
    #main function to play the Tic-Tac-Toe game'
    if current_player == 'X': # Player always starts first
        move = input("Enter your move (1-9): ")
        try:
            position = int(move) - 1
            if 0 <= position <= 8 and board[position].isdigit():
                board[position] = current_player
                print_board() # Print board after player move
                # Check for win or tie
                if check_winner(current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif check_tie():
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = '0'  # Switch to AI
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    else:  # AI's turn
        print("AI's turn...")
        Ai_move()
        print_board() # Print board after AI move
        if check_winner('O'):
            print("AI wins!")
            game_over = True
        elif check_tie():
            print("It's a tie!")
            game_over = True
        else:
            current_player = 'X'  # Switch back to player

print("Game over. Please restart to play again.")


