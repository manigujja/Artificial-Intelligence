import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        print("-"*9)

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board


def alphabeta(is_max, alpha, beta):

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
                score = alphabeta(False, alpha, beta)
                board[i] = ' '
                
                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break
        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = alphabeta(True, alpha, beta)
                board[i] = ' '
                
                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break
        return best


def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = alphabeta(False, -math.inf, math.inf)
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
