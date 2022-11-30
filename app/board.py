# Định nghĩa bàn cờ
# Các move có thể đi được tại một vị trí nhất định được khai dưới dạng static
# Có thủ tục tạo object

class Board:

    # Code cứng legal move dưới dạng static list 2 chiều
    legal_move = [[]]

    # Khởi tạo obj board nếu cần, có chứa danh sách các quân cờ và map
    def __init__(self, boardPlacement):
        self.createPiecesList(boardPlacement)
        self.createBoardPlacement(boardPlacement)
        self.updatePosibleMove()

    # Định nghĩa danh sách piece của board
    def createPiecesList(self, boardPlacement):
        # Tạo danh sách từng piece, lưu ý tạo mới piece cho board vì mỗi board sẽ
        # có posibleMove của piece khác nhau
        return

    # Hàm tạo board placement, mỗi ô trong list 2 chiều sẽ chứa một piece
    def createBoardPlacement(self, boardPlacement):
        return

    # Hàm cập nhật lại posibleMove cho các piece
    def updatePosibleMove(self):
        return

    # Hàm kiểm tra tupleMove có thực hiện được hay không
    def boardMoveChk(self, moveTupple):
        return

    # Định nghĩa hàm di chuyển một quân cờ trong board này
    # Kết quả trả ra là chuỗi string báo là có thế cờ mở hay không
    def boardMove(self, moveTupple):
        # Thực hiện di chuyển quân cờ
            # Cập nhật danh sách quân cờ và bàn cờ sau khi di chuyển
        # Thực hiện thay đổi màu do gánh
        # Thực hiện thay đổi màu do vây
        # Thực hiện kiểm tra thế cờ mở (không gánh, không vây mới kiểm)
        return