from random import randrange

# Initialize the board as a 3x3 nested list
board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]

def print_board():
    """Prints the Tic-Tac-Toe board in the required format."""
    print("\n+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def check_winner(mark):
    """Checks if a player ('X' or 'O') has won the game."""
    # Winning conditions: rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):  # Row check
            return True
        if all(board[j][i] == mark for j in range(3)):  # Column check
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):  # Diagonals
        return True
    return False

def is_tie():
    """Checks if the game is a tie (no empty squares left)."""
    return all(cell in ["X", "O"] for row in board for cell in row)

def player_move():
    """Handles player's input and updates the board."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] not in ["X", "O"]:
                board[row][col] = "O"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def computer_move():
    """Selects a random available move for the computer."""
    while True:
        move = randrange(9)
        row, col = divmod(move, 3)
        if board[row][col] not in ["X", "O"]:
            board[row][col] = "X"
            break

# Game starts
print("Welcome to Tic-Tac-Toe!")
board[1][1] = "X"  # Computer starts with middle
print_board()

while True:
    player_move()
    print_board()
    if check_winner("O"):
        print("You won!")
        break
    if is_tie():
        print("It's a tie!")
        break

    computer_move()
    print_board()
    if check_winner("X"):
        print("Computer won!")
        break
    if is_tie():
        print("It's a tie!")
        break