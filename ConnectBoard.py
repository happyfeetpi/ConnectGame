import numpy

directions = [(1, 0), (1, 1), (0, 1), (-1, 1)]


class ConnectBoard(object):

    def __init__(self, connect=4, shape=(7, 6)):
        self.connect = connect
        self._pieces = numpy.zeros(shape)
        self._turn = 1
        self._board_state = 0

    def copy(self):
        pass

    @property
    def shape(self):
        return self._pieces.shape

    def piece(self, coord):
        return self._pieces[coord]

    @property
    def turn(self):
        return self._turn

    @property
    def current_player(self):
        return ((self._turn + 1) % 2) + 1

    @property
    def board_state(self):
        return self._board_state

    def take_turn(self, x):
        for y in range(self.shape[1]):
            if self._pieces[x, y] == 0:
                break
        else:
            return -1

        current_player = self.current_player
        self._pieces[x, y] = current_player
        self._turn += 1

        if self.board_state != 0:
            return self._board_state

        if self._turn > self.shape[0]*self.shape[1]:
            self._board_state = 3
            return 3

        for direction in directions:
            num_connected = -1

            piece_index = (x, y)
            try:
                a = self._pieces[piece_index]
                while self._pieces[piece_index] == current_player:
                    num_connected += 1
                    piece_index = (piece_index[0] + direction[0], piece_index[1] + direction[1])
            except IndexError:
                pass

            piece_index = (x, y)
            try:
                while self._pieces[piece_index] == current_player:
                    num_connected += 1
                    piece_index = (piece_index[0] - direction[0], piece_index[1] - direction[1])
            except IndexError:
                pass

            if num_connected >= self.connect:
                self._board_state = current_player
                return self._board_state

        return self._board_state
