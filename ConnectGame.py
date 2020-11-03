from ConnectBoard import ConnectBoard
import pygame
import math
import sys


class ConnectGame(object):

    def __init__(self, connect=4, shape=(7, 6), sizes=(100, 45), colors=((0, 0, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0))):
        self._board = ConnectBoard(connect, shape)
        self._colors = colors
        self._sizes = sizes
        self._screen = pygame.display.set_mode(((shape[0])*self._sizes[0], (shape[1]+1)*self._sizes[0]))
        pygame.init()

    def draw_board(self):
        shape = self._board.shape
        rectangle_size = self._sizes[0]
        circle_radius = self._sizes[1]

        pygame.draw.rect(self._screen, self._colors[1], (0, rectangle_size, shape[0]*rectangle_size, (shape[1]+1)*rectangle_size))
        for x in range(shape[0]):
            for y in range(shape[1]):
                current_piece = self._board.piece((x, y))
                current_color = self._colors[0]
                if current_piece == 1:
                    current_color = self._colors[2]
                elif current_piece == 2:
                    current_color = self._colors[3]
                pygame.draw.circle(self._screen, current_color, (int((x + 0.5) * rectangle_size), int((shape[1] - y + 0.5) * rectangle_size)), circle_radius)

        board_state = self._board.board_state
        if board_state != 0:
            if board_state == 3:
                label = pygame.font.SysFont("monospace", rectangle_size).render("Tie!!", 1, self._colors[1])
            else:
                label = pygame.font.SysFont("monospace", rectangle_size).render("Player " + str(board_state) + " Wins!!", 1, self._colors[board_state + 1])
            self._screen.blit(label, (40, 10))

        pygame.display.update()

    def play_game(self):
        shape = self._board.shape
        rectangle_size = self._sizes[0]
        circle_radius = self._sizes[1]
        self.draw_board()

        while self._board.board_state == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self._screen, self._colors[0], (0, 0, shape[0]*rectangle_size, rectangle_size))
                    x_screen = event.pos[0]
                    pygame.draw.circle(self._screen, self._colors[self._board.current_player+1], (x_screen, rectangle_size // 2), circle_radius)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = int(math.floor(event.pos[0] / rectangle_size))
                    if self._board.take_turn(x) != -1:
                        pygame.draw.rect(self._screen, self._colors[0], (0, 0, shape[0] * rectangle_size, rectangle_size))
                        pygame.draw.circle(self._screen, self._colors[self._board.current_player + 1], (x_screen, rectangle_size // 2), circle_radius)

                self.draw_board()

        pygame.time.wait(3000)


if __name__ == "__main__":
    connect_game = ConnectGame()
    connect_game.play_game()