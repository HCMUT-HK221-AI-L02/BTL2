# model test đánh với người thường
# Nếu một moveTupple không hợp lệ thì bắt chọn lại moveTupple

# Import thư viện và hàm
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
    # Chọn ai đi trước và ai là 'X' (-1) hoặc 'O' (1)
    side = int(input("Input your side, 1 or -1: "))
    # Yêu cầu nhập xem ai là 'X' hoặc 'O'
    turn = int(input("Who go first (1_(O) | -1_(X)) ?"))
    # Set thời gian cho người chơi
    remain_time = {
        "remain_time_x": 1000,
        "remain_time_o": 1000
    }

    while True:
        # User Turn
        if turn == side:
            isPossibleMove = False
            #Start user time
            s_user_time = time.time()
            while not isPossibleMove:
                print("Please input a valid move.")
                printCanPickPiece(master_board, turn)
                startString = input("Input position of picked piece: ")
                startTuple = eval(startString)
                if printCanPickDes(master_board, startTuple): continue
                endString = input("Input position of destination: ")
                #End user Time
                e_user_time = time.time()
                endTuple = eval(endString)
                moveTuple = (startTuple, endTuple)
                if master_board.boardMoveChk(moveTuple, side): 
                    isPossibleMove = True
            # Giảm thời gian chơi của user
            if side == 1:
                remain_time["remain_time_x"] -= s_user_time - e_user_time
            else:
                remain_time["remain_time_o"] -= s_user_time - e_user_time

        # Com turn
        else:
            # # Random piece in pieceList
            # piece = random.choice(master_board.pieceList)
            # # Random move in pieceList.possibleMove
            # moveTuple = random.choice(piece.posibleMove)
            moveTuple = move(master_board.prev_board, master_board.board, turn, remain_time["remain_time_x"], remain_time["remain_time_o"])
            return
        master_board.boardMove(moveTuple)
        # Kiểm tra thời gian còn lại của X và O
        if remain_time["remain_time_x"] <= 0:
            print("End of game, player X is out of time!")
        elif remain_time["remain_time_o"] <= 0:
            print("End of game, player Y is out of time!")
        # Kiểm tra thắng cuộc
        if master_board.victor:
            print("End of game, the victory is " + str(side))
            break
        turn *= -1
        # Yêu cầu nhập xem ai đi trước
    # Tạo vòng lặp while, lần lượt người chơi thực hiện lượt đi
        # Nếu là Máy, gọi hàm move, trả ra tuple
        # Nếu là Human:
            # Nhập vào terminal tuple
            # Kiểm tra nước đi hợp lệ
            # Trả ra tuple move kết quả
        # Nhập move vào trong master_board, trả kết quả ra là board và prev_board
        # Phân biệt thắng thua hoặc đi tiếp, đổi lượt
    return