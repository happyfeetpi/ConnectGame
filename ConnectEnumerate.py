from random import Random
from ConnectBoard import ConnectBoard


def connect_enumerate(iterations=1000, connect=4, shape=(7, 6), rand=Random()):
    probs = [0]*3

    for _ in range(iterations):
        board = ConnectBoard(connect, shape)

        while board.board_state == 0:
            x = rand.randrange(shape[0])
            while board.take_turn(x) == -1:
                x = rand.randrange(shape[0])

        probs[board.board_state-1] += 1

    return probs


if __name__ == "__main__":
    print(connect_enumerate())
