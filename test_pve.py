# model test đánh với người thường
# Nếu một moveTupple không hợp lệ thì bắt chọn lại moveTupple

# Import thư viện và hàm
import random
from app.state import *

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
    turn = int(input("Who go first (1 | -1) ?"))

    while True:
        # User Turn
        if turn == side:
            isPossibleMove = False
            while not isPossibleMove:
                print("Please input a valid move.")
                printCanPickPiece(master_board, turn)
                startString = input("Input position of picked piece: ")
                startTuple = eval(startString)
                if printCanPickDes(master_board, startTuple): continue
                endString = input("Input position of destination: ")
                endTuple = eval(endString)
                moveTuple = (startTuple, endTuple)
                if master_board.boardMoveChk(moveTuple, side): 
                    isPossibleMove = True
        # Com turn
        else:
            # Random piece in pieceList
            piece = random.choice(master_board.pieceList)
            # Random move in pieceList.possibleMove
            moveTuple = random.choice(piece.posibleMove)
            return
        master_board.boardMove(moveTuple)
        # Check Victory
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