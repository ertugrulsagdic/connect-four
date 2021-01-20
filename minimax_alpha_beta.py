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


def minimax_alpha_beta(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if board.winning_move(2):
                return None, 100000000000000
            elif board.winning_move(1):
                return None, -100000000000000
            else:  # Game is over, no more valid moves
                return None, 0
        else:  # Depth is zero
            return None, evaluation3(board, 2)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = board.get_next_row(col)
            b_copy = Board()
            b_copy.board = board.board.copy()
            b_copy.drop_piece(row, col, 2)
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
            row = board.get_next_row(col)
            b_copy = Board()
            b_copy.board = board.board.copy()
            b_copy.drop_piece( row, col, 1)
            new_score = minimax_alpha_beta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
