import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'): return 1
    if check_winner(board, 'X'): return -1
    if is_board_full(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Main Game Loop
print("Welcome to AI Tic-Tac-Toe! You are 'X' and AI is 'O'.")
while True:
    print_board()
    if check_winner(board, 'O'):
        print("AI wins! Better luck next time.")
        break
    if is_board_full(board):
        print("It's a draw!")
        break
        
    try:
        move = int(input("Enter move (0-8): "))
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'
    except (ValueError, IndexError):
        print("Please enter a number between 0 and 8.")
        continue

    if not is_board_full(board) and not check_winner(board, 'X'):
        ai_move()