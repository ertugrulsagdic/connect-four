import random

from board import *
import pygame
import sys
import math


def human_vs_ai(board, player_turn):
    game_over = False
    turn = player_turn
    while not game_over:

        if turn == 0 and not game_over:

            column = random.randint(0, 6)

            if is_empty(board, column):
                pygame.time.wait(500)
                row = get_next_row(board, column)
                drop_piece(board, row, column, 1)

                if winning_move(board, 1):
                    label = pygame.font.SysFont("monospace", 75).render("Player 1 wins!", 1, board.yellow)
                    board.screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board, 1, 2)

                turn += 1
                turn = turn % 2

        if turn == 1 and not game_over:

            column = random.randint(0, 6)

            if is_empty(board, column):
                pygame.time.wait(500)
                row = get_next_row(board, column)
                drop_piece(board, row, column, 2)

                if winning_move(board, 2):
                    label = pygame.font.SysFont("monospace", 75).render("Player 2 wins!", 2, board.yellow)
                    board.screen.blit(label, (40, 10))
                    game_over = True

                print_board(board)
                draw_board(board, 1, 2)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)


if __name__ == '__main__':
    pygame.init()
    player_turn = 0
    board = Board()

    print_board(board)
    draw_board(board, 1, 2)
    human_vs_ai(board, player_turn)
