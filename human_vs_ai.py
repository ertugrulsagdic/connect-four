import random
from board import *
import pygame
import sys
import math
from minimax_alpha_beta import *


def human_vs_ai(board, player_turn):
    game_over = False
    turn = player_turn
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(
                    board.screen,
                    board.black,
                    (0, 0, board.width, board.square_size)
                )
                position_x = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(
                        board.screen,
                        board.red,
                        (position_x, int(board.square_size / 2)),
                        board.radius
                    )
                else:
                    pygame.draw.circle(
                        board.screen,
                        board.yellow,
                        (position_x, int(board.square_size / 2)),
                        board.radius
                    )
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(
                    board.screen,
                    board.black,
                    (0, 0, board.width, board.square_size)
                )
                position_x = event.pos[0]
                column = int(math.floor(position_x / board.square_size))
                if turn == 0:

                    if board.is_empty(column):
                        row = board.get_next_row(column)
                        board.drop_piece(row, column, 1)

                        if board.winning_move(1):
                            label = pygame.font.SysFont("monospace", 75).render("Player 1 wins!", 1, board.red)
                            board.screen.blit(label, (40, 10))
                            game_over = True

                        board.print_board()
                        board.draw_board(1, 2)

                        turn += 1
                        turn = turn % 2

        if turn == 1 and not game_over:

            column, minimax_score = minimax_alpha_beta(board, 3, -math.inf, math.inf, 2)

            if board.is_empty(column):
                pygame.time.wait(500)
                row = board.get_next_row(column)
                board.drop_piece(row, column, 2)

                if board.winning_move(2):
                    label = pygame.font.SysFont("monospace", 75).render("Player 2 wins!", 2, board.yellow)
                    board.screen.blit(label, (40, 10))
                    game_over = True

                board.print_board()
                board.draw_board(1, 2)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


if __name__ == '__main__':
    pygame.init()
    player_turn = 0
    board = Board()

    board.print_board()
    board.draw_board(1, 2)
    human_vs_ai(board, player_turn)