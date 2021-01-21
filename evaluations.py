from board import *
import math

def evaluation1(board, piece):
    return 10

def evaluation2(board, piece):
    pass

def evaluation3(board, piece):
    window_length = 4
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board.board[:, board.columns // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(board.rows):
        row_array = [int(i) for i in list(board.board[r, :])]
        for c in range(board.columns - 3):
            window = row_array[c:c + window_length]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(board.columns):
        col_array = [int(i) for i in list(board.board[:, c])]
        for r in range(board.rows - 3):
            window = col_array[r:r + window_length]
            score += evaluate_window(window, piece)

    ## Score posiive sloped diagonal
    for r in range(board.rows - 3):
        for c in range(board.columns - 3):
            window = [board.board[r + i][c + i] for i in range(window_length)]
            score += evaluate_window(window, piece)

    for r in range(board.rows - 3):
        for c in range(board.columns - 3):
            window = [board.board[r + 3 - i][c + i] for i in range(window_length)]
            score += evaluate_window(window, piece)

    return score

def evaluate_window(window, piece):
    score = 0
    opponent_piece = 1
    if piece == 1:
        opponent_piece = 2

    if window.count(piece) == 4 and window.count(0) == 0:
        score += math.inf
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opponent_piece) == 4 and window.count(0) == 0:
        score -= math.inf
    elif window.count(opponent_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score

    return score