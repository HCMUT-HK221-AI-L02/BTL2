# Định nghĩa một quân cờ, có màu, tọa độ, nước đi có thể đi
class Piece:
    def __init__(self, team, pos: tuple):
        self.team = team
        self.pos = pos
        # posibleMove là danh sách các tuple, mỗi tuple là một move có thể đi
        self.posibleMove = []

    def inputPosibleMove(self, posibleMove: list):
        self.posibleMove = posibleMove

    def movePiece(self, des: tuple):
        self.pos = des