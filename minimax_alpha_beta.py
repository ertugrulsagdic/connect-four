import math
import random
from board import *
from evaluations import *


def get_valid_locations(board):
    valid_locations = []
    for column in range(board.columns):
        if board.board[board.rows - 1][column] == 0:
            valid_locations.append(column)
    return valid_locations


def is_terminal_node(board):
    return board.winning_move(1) or board.winning_move(2) or len(get_valid_locations(board)) == 0


def minimax_alpha_beta(board, depth, alpha, beta, maximizingPlayer, piece):
    opponent_piece = 1
    if piece == 1:
        opponent_piece = 2
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0:
        if len(get_valid_locations(board)) == 0:
            return None, 0
        else:  # Depth is zero
            return None, evaluation3(board, piece)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = board.get_next_row(col)
            b_copy = Board()
            b_copy.board = board.board.copy()
            b_copy.drop_piece(row, col, piece)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, False, piece)[1]
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
            row = board.get_next_row(col)
            b_copy = Board()
            b_copy.board = board.board.copy()
            b_copy.drop_piece(row, col, opponent_piece)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, True, piece)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
