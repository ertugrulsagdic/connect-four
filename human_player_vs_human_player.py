from board import *
import pygame
import sys
import math


class HumanPlayerVsHumanPlayer:
    def __init__(self):
        self.game_over = False
        self.turn = 0
        self.board = Board()

        self.my_font = pygame.font.SysFont("monospace", 75)

    def play_game(self):

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(
                        self.board.screen,
                        self.board.black,
                        (0, 0, self.board.width, self.board.square_size)
                    )
                    position_x = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(
                            self.board.screen,
                            self.board.red,
                            (position_x, int(self.board.square_size / 2)),
                            self.board.radius
                        )
                    else:
                        pygame.draw.circle(
                            self.board.screen,
                            self.board.yellow,
                            (position_x, int(self.board.square_size / 2)),
                            self.board.radius
                        )
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(
                        self.board.screen,
                        self.board.black,
                        (0, 0, self.board.width, self.board.square_size)
                    )
                    position_x = event.pos[0]
                    column = int(math.floor(position_x / self.board.square_size))
                    if self.turn == 0:

                        if self.board.is_empty(column):
                            row = self.board.get_next_row(column)
                            self.board.drop_piece(row, column, 1)

                            if self.board.wining_move(1):
                                label = self.my_font.render("Player 1 wins!", 1, self.board.red)
                                self.board.screen.blit(label, (40, 10))
                                self.game_over = True
                    else:

                        if self.board.is_empty(column):
                            row = self.board.get_next_row(column)
                            self.board.drop_piece(row, column, 2)

                            if self.board.wining_move(2):
                                label = self.my_font.render("Player 2 wins!", 2, self.board.yellow)
                                self.board.screen.blit(label, (40, 10))
                                self.game_over = True

                    self.board.print_board()
                    self.board.draw_board(1, 2)

                    self.turn += 1
                    self.turn = self.turn % 2

                    if self.game_over:
                        pygame.time.wait(3000)


if __name__ == '__main__':
    pygame.init()
    human_vs_human = HumanPlayerVsHumanPlayer()
    human_vs_human.board.print_board()
    human_vs_human.board.draw_board(1, 2)
    human_vs_human.play_game()
