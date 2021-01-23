import sys
import time

from minimax_alpha_beta import *
from minimax import *
from board import *


def ai_vs_ai(board, player_turn, depth=4, evaluation_function=2):
    game_over = False
    rounds = 0
    turn = player_turn

    decision_times0 = []
    decision_times1 = []
    while not game_over:
        if len(board.get_valid_locations()) == 0:
            label = pygame.font.SysFont("monospace", 24).render("DRAW!", 0, board.white)
            board.screen.blit(label, (40, 10))
            pygame.display.update()
            game_over = True

        if turn == 0 and not game_over:
            start_time0 = time.time()
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
                end_time0 = time.time()
                decision_time = end_time0 - start_time0
                decision_times0.append(decision_time)
                print('Red (AI) decision time (seconds):', decision_time)

        if turn == 1 and not game_over:
            start_time1 = time.time()
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
                end_time1 = time.time()
                decision_time1 = end_time1 - start_time1
                decision_times1.append(decision_time1)
                print('Yellow (AI) decision time (seconds):', decision_time1 )


        if game_over:
<<<<<<< HEAD
            pygame.time.wait(30000000)
=======
            pygame.time.wait(5000)
            print('Average decision time of Red (AI) (seconds) :', sum(decision_times0)/len(decision_times0))
            print('Average decision time of Yellow (AI) (seconds) :', sum(decision_times1)/len(decision_times1))
>>>>>>> c863c0646627b934e651dd626abcad30a57a12c7



if __name__ == '__main__':
    pygame.init()
    player_turn = 0
    board = Board()

    board.print_board()
    board.draw_board(1, 2)
    ai_vs_ai(board, player_turn)
