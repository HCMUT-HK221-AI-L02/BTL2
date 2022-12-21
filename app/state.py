# Định nghĩa bàn cờ
# Các move có thể đi được tại một vị trí nhất định được khai dưới dạng static
# Có thủ tục tạo object

from app.legalmove import *
from app.piece import *
from app.utils import *


class State:
    # Khởi tạo obj State nếu cần, có chứa danh sách các piece và placement
    # Nhập vào board từ move để khởi tạo
    def __init__(self, prev_board: list, board: list):
        self.prev_board = copyBoard(prev_board)
        self.board = copyBoard(board)
        self.pieceList = []
        self.boardPlacement = []
        self.trapMoveList = []
        self.victor = 0
        self.createPieceListAndBoardPlacement()
        self.updatePosibleMove()
        self.updateTrapMoveList()
        

    # Tạo danh sách piece, lưu ý tạo mới piece cho state vì mỗi state sẽ
    # có posibleMove của piece khác nhau
    # Đồng thời tạo placement, mỗi ô trong array 2D sẽ chứa một piece
    def createPieceListAndBoardPlacement(self):
        # Tạo list mới
        newPieceList = []
        newBoardPlacement = []
        # Duyệt qua board
        for boardRow in range(5):
            newBoardPlacementRow = []
            for boardColumn in range(5):
                # Nếu ô board đang xét có chứa piece thì tạo piece và thêm vào list
                newPiece = None
                if self.board[boardRow][boardColumn] != 0:
                    pos = (boardRow, boardColumn)
                    newPiece = Piece(self.board[boardRow][boardColumn], pos)
                    newPieceList.append(newPiece)
                # Đặt piece vào trong boardPlacement
                newBoardPlacementRow.append(newPiece)
            newBoardPlacement.append(newBoardPlacementRow)
        # Gán kết quả thu được
        self.pieceList = newPieceList
        self.boardPlacement = newBoardPlacement


    # Hàm tạo danh sách các trapMove
    def updateTrapMoveList(self):
        self.trapMoveList = []
        # Kiểm tra xem trước đó có hiện tượng ăn quân không, nếu có thì skip trap move
        if self.prev_board == None: return
        if countPieceTeam(self.prev_board, 1) != countPieceTeam(self.board, 1): return
        # Tìm vị trí vừa đi tới thông qua prev_board và board
        foundMove = False
        for i in range(5):
            for j in range(5):
                if self.prev_board[i][j] != 0:
                    if self.board[i][j] == 0:
                        pp = (i,j)
                        foundMove = True
                        break
            if foundMove: break
        beingTrap = self.prev_board[i][j] * (-1)
        # Lấy danh sách legalMove từ vị trí pp
        legalMoveFromPP: list = LEGALMOVE[pp[0]][pp[1]]
        # Lấy danh sách đối tượng bị trap từ legalMoveFromPP
        posibleBeingTrap = []
        for move in legalMoveFromPP:
            des = move[1]
            if self.board[des[0]][des[1]] == beingTrap: posibleBeingTrap.append(des)
        # Với mỗi cell bị trap, tạo state đệm
        for trapedPos in posibleBeingTrap:
            tState = State(None, self.board)
            # Đi thử move bị ép đi
            moveTuple = (trapedPos, pp)
            endTuple = tState.boardMovePiece(moveTuple)
            # Nếu move bị ép đi có xảy ra gánh thì thêm vào trong trapmove
            isLegitTrap = tState.ganh(endTuple)
            if isLegitTrap == True: self.trapMoveList.append(moveTuple)
        # Nếu có trapMove thì ghi đè lên posible move
        if len(self.trapMoveList) > 0:
            # Ép tất cả posiblemove của các piece là rỗng
            for piece in self.pieceList:
                posibleMove = []
                piece.inputPosibleMove(posibleMove)
            # Duyệt qua danh sách trapMoveList
            for move in self.trapMoveList:
                start = move[0]
                # Gán move vào trong piece tại start
                piece = self.boardPlacement[start[0]][start[1]]
                piece.addPosibleMove(move)


    # Hàm cập nhật lại posibleMove cho các piece
    # Có xét cả trường hợp bị bẫy nên giảm posiblemove
    def updatePosibleMove(self):
        # Duyệt qua danh sách piece
        piece: Piece
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


    # Hiện thực hàm chỉ move 1 piece
    def boardMovePiece(self, moveTupple) -> tuple:
        # Backup lại prev_move
        self.prev_board = copyBoard(self.board)
        # Thực hiện lấy piece
        startTuple = moveTupple[0]        
        piece = self.boardPlacement[startTuple[0]][startTuple[1]]
        # Di chuyển quân cờ trên bàn cờ
        endTuple = moveTupple[1]
        self.boardPlacement[endTuple[0]][endTuple[1]] = piece
        self.boardPlacement[startTuple[0]][startTuple[1]] = None
        # Cập nhật vị trí mới của quân cờ vừa đi
        piece.movePiece(endTuple)
        # update posiblemove và board
        self.updatePosibleMove()
        self.updateBoard()
        # Trả ra endTuple
        return endTuple


    # Định nghĩa hàm di chuyển một quân cờ đồng thời đổi màu do gánh hoặc vây
    # Kết quả trả ra là return Code:
    # 0: không có gánh và vây
    # 1: có gánh
    # 2: có vây
    # 3: vừa gánh vừa vây
    def boardMove(self, moveTupple) -> int:
        # Thực hiện move một piece trong bàn cờ
        endTuple = self.boardMovePiece(moveTupple)
        # Thực hiện thay đổi màu do gánh
        ganhChk =  self.ganh(endTuple)
        # Thực hiện thay đổi màu do vây
        vayChk = self.vay(endTuple)
        # Cập nhật board, posiblemove và trapmove
        self.updateBoard()
        self.updateTrapMoveList()
        # Kiểm tra người chiến thắng
        self.victorCHK()
        # Trả ra trạng thái có hay không gánh với vây
        return encodeBoardMoveReturn(ganhChk, vayChk)


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
            if self.boardPlacement[pos1[0]][pos1[1]] == None: continue
            if self.boardPlacement[pos2[0]][pos2[1]] == None: continue
            if self.boardPlacement[pos1[0]][pos1[1]].team != enemy: continue
            if self.boardPlacement[pos2[0]][pos2[1]].team != enemy: continue
            # Thêm 2 quân cờ trên vào trong danh sách đổi team
            toChange.append(self.boardPlacement[pos1[0]][pos1[1]])
            toChange.append(self.boardPlacement[pos2[0]][pos2[1]])
        # Đổi team các quân cờ trong list
        return changeTeamList(toChange)


    # Định nghĩa hàm kiểm tra việc vây quân cờ
    def vay(self, position) -> bool:
        # Tạo list để phân nhóm quân cờ, team mình thì đánh số 1 hết
        anyChange = False
        enemyTeam = self.boardPlacement[position[0]][position[1]].team * (-1)
        L1 = []
        pieceChk = []
        for piece in self.pieceList: 
            if piece.team == enemyTeam: pieceChk.append(False)
            else: pieceChk.append(True)
        # Duyệt qua các quân cờ trên bàn để phân nhóm
        for i in range(len(self.pieceList)):
            # Kiểm tra xem piece có trong list nào trong L1 chưa
            if pieceChk[i] == True: continue
            # Kiểm tra xem piece này thêm vào được list con nào trong L1 không
            inL2 = False
            for L2 in L1:
                # Duyệt qua từng pp trong L2
                for pp in L2:
                    # Lấy ra list legal move
                    legalMoveList = LEGALMOVE[pp.pos[0]][pp.pos[1]]
                    # Lấy ra list vị trí cần xét
                    legalNextPos = []
                    for move in legalMoveList: legalNextPos.append(move[1])
                    # Lấy ra piece nằm trong legalNextPos
                    ppNextList = []
                    for pos in legalNextPos:
                        if self.boardPlacement[pos[0]][pos[1]] != None:
                            ppNextList.append(self.boardPlacement[pos[0]][pos[1]])
                    # Nếu piece i nằm trong ppNextList thì báo rằng có thể thêm vào L2
                    if self.pieceList[i] in ppNextList: inL2 = True
                    if inL2 == True: break
                # Nếu được báo là có thể thêm vào L2 thì add vào L2 rồi break
                if inL2 == True:
                    L2.append(self.pieceList[i])  
                    pieceChk[i] = True       
                    break
            # Nếu piece i không nằm trong L2 nào đó thì tạo một L2 mới
            if inL2 == False: 
                L1.append([self.pieceList[i]])
                pieceChk[i] = True
        # Duyệt qua danh sách phân nhóm L1
        for L2 in L1:
            # Đếm số bước đi có thể thực hiện của L2
            totalPosibleMove = 0
            piece: Piece
            for piece in L2: totalPosibleMove += len(piece.posibleMove)
            # Nếu nhóm L2 không còn nước đi thì đổi màu cả nhóm
            if totalPosibleMove == 0: 
                changeTeamList(L2)
                anyChange = True
        return anyChange


    # Định nghĩa hàm đếm tổng số posibleMove của một phe
    def posibleMoveListTeam(self, team):
        posibleMoveListTeam = []
        piece: Piece
        for piece in self.pieceList:
            if piece.team != team: continue
            for move in piece.posibleMove: posibleMoveListTeam.append(move)
        return posibleMoveListTeam
