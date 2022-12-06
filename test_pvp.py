# model test người đánh với người để hiện thực luật chơi
# Nếu một moveTupple không hợp lệ thì bắt chọn lại moveTupple

# Import thư viện và hàm
from app.boardstate import *

def main():
    # Khởi tạo bàn cờ đầu tiên
    # 1 là 'O', -1 là 'X', 0 là ô trống.
    start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
    master_board = BoardState(None, start_board)
    # Chỉ cần chọn 'X' đi trước hay 'O' đi trước
        # Yêu cầu nhập xem ai là 'X' hoặc 'O'
        # Yêu cầu nhập xem ai đi trước
    # Tạo vòng lặp while, lần lượt người chơi thực hiện lượt đi
        # Nếu là Human:
            # Nhập vào terminal tuple
            # Kiểm tra nước đi hợp lệ
            # Trả ra tuple move kết quả
        # Nhập move vào trong master_board, trả kết quả ra là board và prev_board
        # Phân biệt thắng thua hoặc đi tiếp, đổi lượt
    return