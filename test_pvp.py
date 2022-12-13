# model test người đánh với người để hiện thực luật chơi
# Nếu một moveTupple không hợp lệ thì bắt chọn lại moveTupple

# Import thư viện và hàm
from app.state import *

def main():
    # Khởi tạo bàn cờ đầu tiên
    # 1 là 'O', -1 là 'X', 0 là ô trống.
    start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
    master_board = State(None, start_board)
    # Chọn 'X' đi trước hay 'O' đi trước
    turnOf = 0
    while turnOf != 1 and turnOf != -1:
        turnOf = int(input("Input start player, 1 or -1: "))
    # Tạo file txt để theo dõi lượt chơi
    writeStateFile("test/pvp.txt", start_board)
    # Tạo vòng lặp while, lần lượt người chơi thực hiện lượt đi
    victor = 0
    while victor == 0:
        # Nhập vào terminal moveTuple, có kiểm tra nước đi hợp lệ
        isPossibleMove = False
        while isPossibleMove == False:
            print("Please input a valid move.")
            startString = input("Input position of picked piece of player " + str(turnOf) + ": ")
            startTuple = eval(startString)
            endString = input("Input position of destination of player " + str(turnOf) + ": ")
            endTuple = eval(endString)
            moveTupple = (startTuple, endTuple)
            if master_board.boardMoveChk(moveTupple, turnOf) == True: isPossibleMove = True                
        # Nhập move vào trong master_board, trả kết quả ra là board và prev_board
        master_board.boardMove(moveTupple)
        # Phân biệt thắng thua hoặc đi tiếp, đổi lượt
        victor = master_board.victor
        turnOf = turnOf*(-1)
        # Viết file txt kết quả
        nowBoard = master_board.board
        writeStateFile("test/pvp.txt", nowBoard)
    print("End of game, the victor is " + str(victor))

if __name__ == "__main__":
    main()