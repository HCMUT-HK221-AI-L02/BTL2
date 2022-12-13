# model test đánh với người thường
# Nếu một moveTupple không hợp lệ thì bắt chọn lại moveTupple

# Import thư viện và hàm
from app.state import *

def main():
    # Khởi tạo bàn cờ đầu tiên
    start_board = [[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
    master_board = State(start_board)
    # Chọn ai đi trước và ai là 'X' hoặc 'O'
        # Yêu cầu nhập xem ai là 'X' hoặc 'O'
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