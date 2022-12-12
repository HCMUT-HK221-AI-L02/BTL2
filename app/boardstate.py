# Định nghĩa bàn cờ
# Các move có thể đi được tại một vị trí nhất định được khai dưới dạng static
# Có thủ tục tạo object

from app.legalmove import *
from app.positionstep import *
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
        self.victor = 0
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
        

    # Hàm update lại board của state
    def updateBoard(self):
        for i in range(5):
            for j in range(5):
                if self.boardPlacement[i][j] == None: self.board[i][j] = 0
                else: self.board[i][j] = self.boardPlacement[i][j].team


    # Hàm kiểm tra tupleMove có thực hiện được hay không
    def boardMoveChk(self, moveTupple, turnOf):
        # Từ moveTupple lấy ra vị trí bắt đầu và kết thúc
        startTuple = moveTupple[0]
        # Từ vị trí bắt đầu lấy ra piece -> có thể return false
        piece = self.boardPlacement[startTuple[0]][startTuple[1]]
        if piece == None: return False
        # Nếu piece này thuộc lượt người khác thì return false
        if piece.team != turnOf: return False
        # Từ piece lấy ra posible move -> có thể return
        posibleMove = piece.posibleMove
        if len(posibleMove) == 0: return False
        if moveTupple in posibleMove: return True



    def victorCHK(self):
        flag = True
        leadTeam = self.pieceList[0].team
        for piece in self.pieceList:
            if piece.team != leadTeam:
                flag = False
                break
        if flag == True:
            self.victor = leadTeam
            return leadTeam
        else: return 0


    # Định nghĩa hàm di chuyển một quân cờ trong board này
    def boardMove(self, moveTupple):
        # Backup lại prev_move
        self.prev_board = self.board
        # Thực hiện lấy piece
        startTuple = moveTupple[0]        
        piece = self.boardPlacement[startTuple[0]][startTuple[1]]
        # Cập nhật bàn cờ sau khi di chuyển
        endTuple = moveTupple[1]
        self.boardPlacement[endTuple[0]][endTuple[1]] = piece
        self.boardPlacement[startTuple[0]][startTuple[1]] = None
        # Cập nhật vị trí mới của quân cờ vừa đi
        piece.movePiece(endTuple)
        # Thực hiện thay đổi màu do gánh
        self.ganh(endTuple)
        # Thực hiện thay đổi màu do vây
        self.vay()
        # Cập nhật board
        self.updateBoard()
        # update posiblemove
        self.updatePosibleMove()  
        # Kiểm tra người chiến thắng
        self.victorCHK()


    # Định nghĩa hàm kiểm tra việc gánh quân cờ
    def ganh(self, position) -> bool:
        # Tạo danh sách quân cờ bị đổi màu
        enemy = self.boardPlacement[position[0]][position[1]].team*(-1)
        toChange = []
        # Loop qua 4 cặp ô cần xét
        for i in range(4):
            # Tạo cặp pos cần xet
            if i == 0: 
                pos1 = (position[0] + POSITIONSTEP[0][0], position[1] + POSITIONSTEP[0][1])
                pos2 = (position[0] + POSITIONSTEP[7][0], position[1] + POSITIONSTEP[7][1])
            elif i == 1:
                pos1 = (position[0] + POSITIONSTEP[1][0], position[1] + POSITIONSTEP[1][1])
                pos2 = (position[0] + POSITIONSTEP[6][0], position[1] + POSITIONSTEP[6][1])
            elif i == 2:
                pos1 = (position[0] + POSITIONSTEP[2][0], position[1] + POSITIONSTEP[2][1])
                pos2 = (position[0] + POSITIONSTEP[5][0], position[1] + POSITIONSTEP[5][1])
            elif i == 3:
                pos1 = (position[0] + POSITIONSTEP[3][0], position[1] + POSITIONSTEP[3][1])
                pos2 = (position[0] + POSITIONSTEP[4][0], position[1] + POSITIONSTEP[4][1])
            # Kiểm tra pos có nằm ngoài bàn cờ, nếu faile thì ko thêm vào list
            if pos1[0] < 0 or pos2[0] < 0 or pos1[0] > 4 or pos2[0] > 4: continue
            if pos1[1] < 0 or pos2[1] < 0 or pos1[1] > 4 or pos2[1] > 4: continue
            # Kiểm tra legal move, nếu faile thì ko thêm vào List
            moveTupple = (position, pos1)
            if legalMoveChk(moveTupple) == False: continue
            moveTupple = (position, pos2)
            if legalMoveChk(moveTupple) == False: continue
            # Kiểm tra xem nếu không có đủ 2 quân cờ đối xứng thì skip
            if self.boardPlacement[pos1[0]][pos1[1]].team != enemy: continue
            if self.boardPlacement[pos2[0]][pos2[1]].team != enemy: continue
            # Thêm 2 quân cờ trên vào trong danh sách đổi team
            toChange.append(self.boardPlacement[pos1[0]][pos1[1]])
            toChange.append(self.boardPlacement[pos2[0]][pos2[1]])
        # Đổi team các quân cờ trong list
        if len(toChange) == 0: return False
        else: 
            for piece in toChange: piece.changeTeam()
            return True



    # Định nghĩa hàm kiểm tra việc vây quân cờ
    def vay(self):
        # Duyệt qua toàn bộ board, xem quân nào bị vây
        # Trả ra danh sách quân cờ bị đổi màu
        return