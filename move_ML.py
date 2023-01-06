# import thư viện
from app.ml_model import *
from app.state import State

# Hàm dịch outputModel thành moveTuple
def toMoveTuple(outputModel, posibleMoveList):
    # Lấy ra index và xác suất của posibleMove
    # Lấy ra index của move có xác suất lớn nhất
    # Dịch index này thành moveTuple
    # Trả kết quả
    ans = tuple()
    return ans

# Định nghĩa hàm move đưa ra kết quả dựa trân model FNN đã train
def move(prev_board, board, player, remain_time_x, remain_time_o):
    # Tạo State và liệt kê ra posibleMove
    rootState = State(prev_board, board)
    posibleMoveList = rootState.posibleMoveListTeam(player)
    # Tạo model và đọc vào weight đã train
    model = initModel()
    model.load_weights('weights/my_model_weights.h5')
    # Đổi input của move thành input của model
    inputVector = []
    inputVector.append(player)
    for row in board:
        for cell in row: inputVector.append(cell)
    # Nhập input vào model
    outputModel = model.predict(inputVector)
    # Đổi output của model thành output của hàm move
    ansMoveTuple = toMoveTuple(outputModel, posibleMoveList)
    # xuất move được chọn ra
    return ansMoveTuple