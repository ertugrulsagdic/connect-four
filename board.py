import numpy as np
import pygame


class Board:
    def __init__(self):
        # colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)

        # board
        self.rows = 6
        self.columns = 7

        # create empty board
        self.board = create_board()

        # square size of the screen
        self.square_size = 100
        # piece radius of the screen
        self.radius = int(self.square_size / 2 - 5)

        # height and width of the screen
        self.width = self.columns * self.square_size
        self.height = (self.rows + 1) * self.square_size

        # size of the screen
        self.size = (self.width, self.height)

        # set screen for the game
        self.screen = pygame.display.set_mode(self.size)


# create board with zeros
def create_board():
    board = np.zeros((6, 7))
    return board


# place the piece on board
def drop_piece(board, row, column, piece):
    board.board[row][column] = piece


# check if the place for piece empty
def is_empty(board, column):
    if board.board[board.rows - 1][column] == 0:
        return True
    else:
        return False


def get_next_row(board, column):
    for row in range(board.rows):
        if board.board[row][column] == 0:
            return row


def print_board(board):
    print(np.flip(board.board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for column in range(board.columns - 3):
        for row in range(board.rows):
            if board.board[row][column] == piece \
                    and board.board[row][column + 1] == piece \
                    and board.board[row][column + 2] == piece \
                    and board.board[row][column + 3] == piece:
                return True

    # Check vertical locations for win
    for column in range(board.columns):
        for row in range(board.rows - 3):
            if board.board[row][column] == piece \
                    and board.board[row + 1][column] == piece \
                    and board.board[row + 2][column] == piece \
                    and board.board[row + 3][column] == piece:
                return True

    # Check positively sloped diagonals
    for column in range(board.columns - 3):
        for row in range(board.rows - 3):
            if board.board[row][column] == piece \
                    and board.board[row + 1][column + 1] == piece \
                    and board.board[row + 2][column + 2] == piece \
                    and board.board[row + 3][column + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for column in range(board.columns - 3):
        for row in range(3, board.rows):
            if board.board[row][column] == piece \
                    and board.board[row - 1][column + 1] == piece \
                    and board.board[row - 2][column + 2] == piece \
                    and board.board[row - 3][column + 3] == piece:
                return True


def draw_board(board, player_1, player_2):
    for column in range(board.columns):
        for row in range(board.rows):
            pygame.draw.rect(board.screen, board.white, (
                column * board.square_size, row * board.square_size + board.square_size, board.square_size,
                board.square_size))
            pygame.draw.circle(board.screen, board.black, (
                int(column * board.square_size + board.square_size / 2),
                int(row * board.square_size + board.square_size + board.square_size / 2)), board.radius)

    for column in range(board.columns):
        for row in range(board.rows):
            if board.board[row][column] == player_1:
                pygame.draw.circle(
                    board.screen,
                    board.red,
                    (
                        int(column * board.square_size + board.square_size / 2),
                        board.height - int(row * board.square_size + board.square_size / 2)
                    ),
                    board.radius
                )
            elif board.board[row][column] == player_2:
                pygame.draw.circle(
                    board.screen,
                    board.yellow,
                    (
                        int(column * board.square_size + board.square_size / 2),
                        board.height - int(row * board.square_size + board.square_size / 2)
                    ),
                    board.radius
                )
    pygame.display.update()
