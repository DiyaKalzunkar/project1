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
