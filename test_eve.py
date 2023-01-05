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
    turn = int(input("Who go first (1_(O) | -1_(X)) ?"))

    remain_time = {
        "remain_time_x": 20000,
        "remain_time_o": 20000
    }

    while True:
        #MCST X(-1) Turn
        if turn == -1:
            # Hiện tại đang gọi hàm move, sẽ thay bằng hàm train MCST sau khi define xong
            moveTuple = move(master_board.prev_board, master_board.board, turn, remain_time["remain_time_x"], remain_time["remain_time_o"])

        #Random O(1) Turn
        else:
            # Lấy list các quân cờ thuộc phe Random
            validPiece = []
            for item in master_board.pieceList:
                if item.team == turn and len(item.posibleMove) > 0:
                    validPiece.append(item)
            piece = random.choice(validPiece)
            # Random move in validPiece
            moveTuple = random.choice(piece.posibleMove)

        print(moveTuple)
        master_board.boardMove(moveTuple)
        # Viết file txt kết quả:
        nowBoard = master_board.board
        writeStateFile("test/eve.txt", nowBoard)
        # Kiểm tra thắng cuộc
        if master_board.victor:
            side = "MCST" if turn == -1 else "Random"
            print("End of game, the victory is " + str(side))
            break
        turn *= -1
    return 

if __name__ == "__main__":
    main()