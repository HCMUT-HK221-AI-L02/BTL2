def copyBoard(board):
    if board == None: return None
    newBoard = []
    for boardRow in board:
        newRow = []
        for cell in boardRow: newRow.append(cell)
        newBoard.append(newRow)
    return newBoard

# Định nghĩa hàm đổi màu toàn list
def changeTeamList(toChangeList: list) -> bool:
    if len(toChangeList) == 0: return False
    else: 
        for piece in toChangeList: piece.changeTeam()
        return True


# Định nghĩa hàm vẽ file xem kết quả
def writeStateFile(path, board):
    f = open(path, "w")
    f.write("      0    1    2    3    4")
    f.write("\n")
    f.write("---------------------------")
    f.write("\n")
    for row in range(5):
        f.write(str(row) + "|")
        s = ""
        for cell in board[row]:
            if cell == -1: s = s + "   " + str(cell)
            else: s = s + "    " + str(cell)
        f.write(s)
        f.write("\n")
        f.write(" |")
        f.write("\n")
    f.close()


# Định nghĩa hàm viết ra terminal kết quả
def printState(board):
    print("      0    1    2    3    4")
    print("---------------------------")
    for row in range(5):
        s = ""
        for cell in board[row]:
            if cell == -1: s = s + "   " + str(cell)
            else: s = s + "    " + str(cell)
        print(str(row) + "|" + s)
        print(" |")


# Đếm số lượng quân cờ trong một team
def countPieceTeam(board, team) -> int:
    ans = 0
    for row in board:
        for cell in row: 
            if cell == team: ans += 1
    return ans


# Hàm mã hóa boardMove return
# 0: không có gánh và vây
# 1: có gánh
# 2: có vây
# 3: vừa gánh vừa vây
def encodeBoardMoveReturn(ganhChk, vayChk):
    if ganhChk == False and vayChk == False: return 0
    elif ganhChk == True and vayChk == False: return 1
    elif ganhChk == False and vayChk == True: return 2
    elif ganhChk == True and vayChk == True: return 3


# Viết hàm in ra terminal danh sách piece có thể chọn
def printCanPickPiece(state, team):
    # Tạo danh sách posible piece position
    posiblePos = []
    # Duyệt qua từng piece
    for piece in state.pieceList:
        # Nếu piece này thuộc team khác thì skip
        if piece.team != team: continue
        # Nếu piece đó posibleMove thì thêm vào posiblePos
        if len(piece.posibleMove) > 0: posiblePos.append(piece.pos)
    # In ra danh sách piece có thể chọn
    print("List of piece can choose: ", posiblePos)


# Viết hàm in ra danh sách đích đến có thể chọn
def printCanPickDes(state, pos) -> bool:
    # Lấy ra piece cần xét
    # Nếu ko lấy ra được thì trả False
    piece = state.boardPlacement[pos[0]][pos[1]]
    if piece == None: return False
    else:
        posibleDes = []
        for move in piece.posibleMove: posibleDes.append(move[1])
        print("List of posible destination: ", posibleDes)
        return True


# --- Hàm hỗ trợ làm model Machine Learning
# Hàm dịch tupleMove đang ở dạng list về dạng tuple
def list_to_tuple(a: list) -> tuple:
    a[0] = tuple(a[0])
    a[1] = tuple(a[1])
    b = tuple(a)
    return b


# Hàm dịch moveTuple thành idx
def moveTuple_to_idx(moveTuple: tuple):
    from app.legalmove import LEGALMOVE
    idx = 0
    for row in LEGALMOVE:
        for col in row:
            for cell in col:
                if cell == moveTuple: return idx
                idx += 1
    return -1


# Hàm dịch idx thành moveTuple
def idx_to_moveTuple(idxFind) -> tuple:
    if idxFind == -1: return None
    from app.legalmove import LEGALMOVE
    idx = 0
    for row in LEGALMOVE:
        for col in row:
            for cell in col:
                if idxFind == idx: return cell
                idx += 1
    return None


# Hàm đổi x của hàm move thành x của model ML
def xMove_to_xModel(player, board: list) -> list:
    inputVector = []
    inputVector.append(player)
    for row in board:
        for cell in row: inputVector.append(cell)
    return inputVector


# Hàm đổi y của hàm move thành y của model ML
def yMove_to_yModel(moveTuple: tuple) -> list:    
    from app.legalmove import LEGALMOVE
    yModel = [0 for i in range(112)]
    idx = moveTuple_to_idx(moveTuple)
    yModel[idx] = 1
    return yModel


# Hàm đổi y của model ML thành y của hàm move
def yModel_to_yMove(yModel: list, posibleMove: list) -> tuple:
    # Lấy ra idx của posibleMove
    posibleIdx = []
    for moveTuple in posibleMove:
        idx = moveTuple_to_idx(moveTuple)
        posibleIdx.append(idx)
    # Duyệt qua yModel, lấy ra y lớn nhất và là posible
    maxValue = 0
    pickIdx = -1
    for i in range(112):
        if i in posibleIdx:
            if yModel[i] > maxValue:
                maxValue = yModel[i]
                pickIdx = i
    if pickIdx != -1: return None
    else: return idx_to_moveTuple(pickIdx)
