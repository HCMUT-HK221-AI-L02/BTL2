# Định nghĩa bàn cờ
# Các move có thể đi được tại một vị trí nhất định được khai dưới dạng static
# Có thủ tục tạo object

from app.legalmove import *
from app.piece import *

class BoardState:

    # Khởi tạo obj boardState nếu cần, có chứa danh sách các piece và placement
    # Nhập vào board từ move để khởi tạo
    def __init__(self, prev_board: list, board: list):
        self.prev_board = prev_board
        self.board = board
        self.pieceList = []
        self.boardPlacement = []
        self.trapMoveList = []
        self.createPieceListAndBoardPlacement()
        self.createTrapMoveList()
        self.updatePosibleMove()


    # Tạo danh sách piece, lưu ý tạo mới piece cho state vì mỗi state sẽ
    # có posibleMove của piece khác nhau
    # Đồng thời tạo placement, mỗi ô trong array 2D sẽ chứa một piece
    def createPieceListAndBoardPlacement(self):
        # Tạo list mới
        newPieceList = []
        newBoardPlacement = [[],[],[],[],[]]
        # Duyệt qua board
        for boardRow in self.board:
            for boardColumn in boardRow:
                # Nếu ô board đang xét có chứa piece thì tạo piece và thêm vào list
                newPiece = None
                if self.board[boardRow][boardColumn] != 0:
                    pos = (boardRow, boardColumn)
                    newPiece = Piece(self.board[boardRow][boardColumn], pos)
                    newPieceList.append(newPiece)
                # Đặt piece vào trong boardPlacement
                newBoardPlacement[boardRow].append(newPiece)
        # Gán kết quả thu được
        self.pieceList = newPieceList
        self.boardPlacement = newBoardPlacement


    # Hàm tạo danh sách các trapMove
    def createTrapMoveList(self):
        # Liệt kê 4 ô nằm kế bên đích đến của move vừa thực hiện
        # Liệt kê các nước đi có thể đi đến 4 ô đó MÀ ĐỐI PHƯƠNG THỰC HIỆN ĐƯỢC
        # Dựa vào danh sách nước đi trên, liệt kê nước đi nào có thể xảy ra gánh
        # Xuất danh sách thu được
        return


    # Hàm cập nhật lại posibleMove cho các piece
    # Có xét cả trường hợp bị bẫy nên giảm posiblemove
    def updatePosibleMove(self):
        # Nếu có trapMove thì làm khác
        if len(self.trapMoveList) == 0:
            # Duyệt qua danh sách piece
            for piece in self.pieceList:
                posibleMove = []
                # Copy legal move qua
                pos = piece.pos
                legalMove = LEGALMOVE[pos[0]][pos[1]]
                # Duyệt qua list các legal move
                for move in legalMove:
                    # Nếu đích đến không có quân cờ chiếm chỗ thì thêm vào posibleMove
                    des = move[1]
                    if self.boardPlacement[des[0]][des[1]] == None: posibleMove.append(move)
                # Nhập posibleMove vào trong piece
                piece.inputPosibleMove(posibleMove)
        


    # Hàm kiểm tra tupleMove có thực hiện được hay không
    def boardMoveChk(self, moveTupple):
        # Từ moveTupple lấy ra vị trí bắt đầu và kết thúc
        # Từ vị trí bắt đầu lấy ra piece -> có thể return false
        # Từ piece lấy ra posible move -> có thể return
        return


    # Định nghĩa hàm di chuyển một quân cờ trong board này
    def boardMove(self, moveTupple):
        # Backup lại prev_move
        # Thực hiện di chuyển quân cờ
            # Cập nhật danh sách quân cờ và bàn cờ sau khi di chuyển
        # Cập nhật vị trí mới của quân cờ vừa đi
        # Thực hiện thay đổi màu do gánh
        # Thực hiện thay đổi màu do vây
        # Cập nhật board
        # update posiblemove
        return


    # Định nghĩa hàm kiểm tra việc gánh quân cờ
    def ganh(board, position):
        # Kiểm tra xem quân cờ nào bị đổi màu
        # Trả ra danh sách quân cờ bị đổi màu do gánh
        return


    # Định nghĩa hàm kiểm tra việc vây quân cờ
    def vay(board):
        # Duyệt qua toàn bộ board, xem quân nào bị vây
        # Trả ra danh sách quân cờ bị đổi màu
        return