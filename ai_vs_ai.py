import sys
import time

from minimax_alpha_beta import *
from minimax import *
from board import *


def ai_vs_ai(board, player_turn, depth=4, evaluation_function=2):
    game_over = False
    rounds = 0
    turn = player_turn
    while not game_over:
        if len(board.get_valid_locations()) == 0:
            label = pygame.font.SysFont("monospace", 24).render("DRAW!", 0, board.white)
            board.screen.blit(label, (40, 10))
            pygame.display.update()
            game_over = True

        if turn == 0 and not game_over:

            # if rounds == 0 or rounds == 1:
            #   column = random.randint(0, 6)
            # else:
            column, minimax_score = minimax_alpha_beta(board, depth, -math.inf, math.inf, True, 1, evaluation_function)

            if board.is_empty(column):
                pygame.time.wait(500)
                row = board.get_next_row(column)
                board.place_piece(row, column, 1)

                if board.check_win(1):
                    label = pygame.font.SysFont("monospace", 24).render("Red (AI) wins!", 1, board.red)
                    board.screen.blit(label, (40, 10))
                    game_over = True

                board.print_board()
                board.draw_board(1, 2)

                rounds += 1
                turn += 1
                turn = turn % 2

        if turn == 1 and not game_over:

            # if rounds == 0 or rounds == 1:
            #     column = random.randint(0, 6)
            # else:

            column, minimax_score = minimax_alpha_beta2(board, depth, -math.inf, math.inf, True, 2, evaluation_function)

            if board.is_empty(column):
                pygame.time.wait(500)
                row = board.get_next_row(column)
                board.place_piece(row, column, 2)

                if board.check_win(2):
                    label = pygame.font.SysFont("monospace", 24).render("Yellow (AI) wins!", 2, board.yellow)
                    board.screen.blit(label, (40, 10))
                    game_over = True

                board.print_board()
                board.draw_board(1, 2)

                rounds += 1
                turn += 1
                turn = turn % 2


        if game_over:
            pygame.time.wait(5000)



if __name__ == '__main__':
    pygame.init()
    player_turn = 0
    board = Board()

    board.print_board()
    board.draw_board(1, 2)
    ai_vs_ai(board, player_turn)
