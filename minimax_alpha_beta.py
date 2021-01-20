import math
import random
from board import *


def get_valid_locations(board):
    valid_locations = []
    for column in range(board.columns):
        if board.board[board.rows - 1][column] == 0:
            valid_locations.append(column)
    return valid_locations


def is_terminal_node(board, piece, opponent_piece):
    return winning_move(board, piece) or winning_move(board, opponent_piece) or len(get_valid_locations(board)) == 0


def minimax_alpha_beta(board, depth, alpha, beta, piece):
    if piece == 1:
        opponent_piece = 2
    else:
        opponent_piece = 1

    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if board.winning_move(board, piece):
                return (None, 100000000000000)
            elif board.winning_move(board, opponent_piece):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if piece == 1:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, piece)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, opponent_piece)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
