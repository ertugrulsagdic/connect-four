from board import *
import pygame
import sys
import math


def human_vs_human(board, player_turn):
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

                    if is_empty(board, column):
                        row = get_next_row(board, column)
                        drop_piece(board, row, column, 1)

                        if winning_move(board, 1):
                            label = pygame.font.SysFont("monospace", 75).render("Player 1 wins!", 1, board.red)
                            board.screen.blit(label, (40, 10))
                            game_over = True
                else:

                    if is_empty(board, column):
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
    human_vs_human(board, player_turn)
