import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        print("-"*9)

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax(is_max):
    
    if check_winner('X'):
        return 1
    if check_winner('O'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best


def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            
            if score > best_score:
                best_score = score
                move = i

    board[move] = 'X'


while True:
    
    print_board()

    pos = int(input("Enter position (0-8): "))
    board[pos] = 'O'

    if check_winner('O'):
        print_board()
        print("You win!")
        break

    if is_draw():
        print("Draw!")
        break

    best_move()

    if check_winner('X'):
        print_board()
        print("AI wins!")
        break
