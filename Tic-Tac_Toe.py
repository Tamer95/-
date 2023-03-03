def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def tic_tac_toe():
    board = [' ']*9
    print_board(board)
    player = 'X'

    while True:
        move = input("Игрок " + player + ", ВВедите число от: (1-9): ")
        move = int(move) - 1

        if board[move] != ' ':
            print("Не верное решение, пожалуйста повторите снова.")
            continue

        board[move] = player
        print_board(board)

        if check_win(board, player):
            print("Игрок " + player + " выиграл!")
            break

        if ' ' not in board:
            print("Tie game.")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

tic_tac_toe()