# model test MCST vs random 

import random
import time
from app.state import *
from move_ML import *

def main():
    # Khởi tạo bàn cờ đầu tiên
    start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
    master_board = State(None, start_board)

    # Chọn MCST là 'X' (-1) hoặc 'O' (1)
    side = int(input("Input MCST side, 1 or -1: "))
    # Chọn bên đi trước  
    turn = int(input("Who go first (1_(O) | -1_(X)) ?"))

    remain_time = {
        "remain_time_x": 20000,
        "remain_time_o": 20000
    }
    
    remain_move = {
        "remain_move_x": 50,
        "remain_move_o": 50
    }

    outOfMove = False

    while True:
        #MCST Turn
        if turn == side:
            # Hiện tại đang gọi hàm move, sẽ thay bằng hàm train MCST sau khi define xong
            moveTuple = move(master_board.prev_board, master_board.board, turn, remain_time["remain_time_x"], remain_time["remain_time_o"])
            
        #Random Turn
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

        #Giảm remain_move
        if turn == 1:
            remain_move["remain_move_o"] -= 1
        else:
            remain_move["remain_move_x"] -= 1

        # Viết file txt kết quả:
        nowBoard = master_board.board
        writeStateFile("test/eve.txt", nowBoard)
        # Kiểm tra thắng cuộc
        if master_board.victor:
            win_side = "MCST" if turn == side else "Random"
            print("End of game, the victory is " + str(win_side))
            printState(nowBoard)
            break
        if remain_move["remain_move_x"] == 0:
            print("End of game, player X is out of moves!")
            outOfMove = True

        elif remain_move["remain_move_o"] == 0:
            print("End of game, player O is out of moves!")
            outOfMove = True
            
        if outOfMove:
            if master_board.advantageTeam() == 0:
                print("Hòa!!!")
            elif master_board.advantageTeam() == side:
                print("End of game, the victory is MCST!")
            else:
                print("End of game, the victory is Random!")
            break

        print(remain_move)
        printState(nowBoard)

        turn *= -1
    return 

if __name__ == "__main__":
    main()