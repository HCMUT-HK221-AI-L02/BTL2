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
    # f.write("   -1    0    0    0   -1")
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