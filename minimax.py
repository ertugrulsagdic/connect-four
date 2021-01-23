import random
from evaluations import *


def minimax(board, depth, maximizing_player, piece):
    opponent_piece = 1
    if piece == 1:
        opponent_piece = 2
    valid_locations = board.get_valid_locations(board)
    if depth == 0:
        if len(valid_locations) == 0:
            return None, 0
        else:  # Depth is zero
            return None, evaluation2(board, piece)
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = board.get_next_row(col)
            b_copy = Board()
            b_copy.board = board.board.copy()
            b_copy.drop_piece(row, col, piece)
            new_score = minimax(b_copy, depth - 1, False, piece)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value
    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = board.get_next_row(col)
            b_copy = Board()
            b_copy.board = board.board.copy()
            b_copy.drop_piece(row, col, opponent_piece)
            new_score = minimax(b_copy, depth - 1, True, piece)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value
