from app.state import *
from move_ML import *

start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
master_board = State(None, start_board)
moveTuple = move(master_board.prev_board, master_board.board, -1, 1000, 1000)