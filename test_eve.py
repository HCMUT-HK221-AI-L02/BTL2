# model test MCST vs random 

import random
import time
from app.state import *
from move_MCST import *

def main():
    # Khởi tạo bàn cờ đầu tiên
    start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
    master_board = State(None, start_board)

    # MCST là 'X' (-1) và random 'O' (1)
    turn = 1
    remain_time = {
        "remain_time_x": 20000,
        "remain_time_o": 20000
    }

    while True:
        #MCST Turn
        if turn == -1:
            # Hiện tại đang gọi hàm move, sẽ thay bằng hàm train MCST sau khi define xong
            moveTuple = move(master_board.prev_board, master_board.board, turn, remain_time["remain_time_x"], remain_time["remain_time_o"])

        #Random Turn
        else:
            # Random piece in pieceList
            piece = random.choice(master_board.pieceList)
            # Random move in pieceList.possibleMove
            moveTuple = random.choice(piece.posibleMove)

        master_board.boardMove(moveTuple)
        # Viết file txt kết quả:
        nowBoard = master_board.board
        writeStateFile("test/eve.txt", nowBoard)
        # Kiểm tra thắng cuộc
        if master_board.victor:
            side = "MCST" if turn == 1 else "Random"
            print("End of game, the victory is " + str(side))
            break
        turn *= -1
    return 

if __name__ == "__main__":
    main()