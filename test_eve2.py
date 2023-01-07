# model test Machine Learning vs random 

import random
import time
from app.state import *
from move_ML import *
SLEEP_TIME = 0

# ----------------------------------------------------------------

def main():
    # Khởi tạo bàn cờ đầu tiên
    start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
    master_board = State(None, start_board)

    # Chọn Machine Learning là 'X' (-1) hoặc 'O' (1)
    side = int(input("Input Machine Learning side, 1 or -1: "))
    # Chọn bên đi trước  
    turn = int(input("Who go first (1_(O) | -1_(X)) ?"))

    remain_time = {
        "remain_time_x": 20000,
        "remain_time_o": 20000
    }
    
    remain_move = {
        "remain_move_-1": 50,
        "remain_move_1": 50
    }

    outOfMove = False

    while True:
        print("------------------------------------------------------------------")

        #Machine Learning Turn
        if turn == side:
            print("MACHINE LEARNING TURN: ", side)
            # Hiện tại đang gọi hàm move, sẽ thay bằng hàm train Machine Learning sau khi define xong
            moveTuple = move(master_board.prev_board, master_board.board, turn, remain_time["remain_time_x"], remain_time["remain_time_o"])
            
        #Random Turn
        else:
            print("RANDOM TURN: ", side*(-1))
            # Lấy list các quân cờ thuộc phe Random
            validPiece = []
            for item in master_board.pieceList:
                if item.team == turn and len(item.posibleMove) > 0:
                    validPiece.append(item)
            piece = random.choice(validPiece)
            # Random move in validPiece
            moveTuple = random.choice(piece.posibleMove)

        print("MAKE MOVE: ", moveTuple)
        master_board.boardMove(moveTuple)
        time.sleep(SLEEP_TIME)

        #Giảm remain_move
        if turn == 1:
            remain_move["remain_move_1"] -= 1
        else:
            remain_move["remain_move_-1"] -= 1

        # Viết file txt kết quả:
        nowBoard = master_board.board
        writeStateFile("test/eve.txt", nowBoard)
        # Kiểm tra thắng cuộc
        if master_board.victor:
            win_side = "Machine Learning" if turn == side else "Random"
            print("End of game, the victory is " + str(win_side))
            printState(nowBoard)
            break
        if remain_move["remain_move_-1"] == 0:
            print("End of game, player -1 is out of moves!")
            outOfMove = True

        elif remain_move["remain_move_1"] == 0:
            print("End of game, player 1 is out of moves!")
            outOfMove = True
            
        if outOfMove:
            if master_board.advantageTeam() == 0:
                print("Hòa!!!")
            elif master_board.advantageTeam() == side:
                print("End of game, the victory is Machine Learning!")
            else:
                print("End of game, the victory is Random!")
            break

        print(remain_move)
        printState(nowBoard)

        turn *= -1
    return 

if __name__ == "__main__":
    main()