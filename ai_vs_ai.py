import sys
from minimax_alpha_beta import *


def ai_vs_ai(board, player_turn):
    game_over = False
    turn = player_turn
    while not game_over:
        if turn == 0 and not game_over:

            column, minimax_score = minimax_alpha_beta(board, 2, -math.inf, math.inf, True)

            if board.is_empty(column):
                pygame.time.wait(500)
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

            column, minimax_score = minimax_alpha_beta(board, 4, -math.inf, math.inf, True)

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
            pygame.time.wait(30000000)



if __name__ == '__main__':
    pygame.init()
    player_turn = 0
    board = Board()

    board.print_board()
    board.draw_board(1, 2)
    ai_vs_ai(board, player_turn)
