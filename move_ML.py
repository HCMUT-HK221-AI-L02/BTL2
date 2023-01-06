# import thư viện
import numpy as np
from app.ml_model import *
from app.state import State
from app.utils import xMove_to_xModel, yModel_to_yMove
CHECKPOINT_FILE = 'weights/my_model_weights.h5'


# Định nghĩa hàm move đưa ra kết quả dựa trân model FNN đã train
def move(prev_board, board, player, remain_time_x, remain_time_o):
    # Tạo State và liệt kê ra posibleMove
    rootState = State(prev_board, board)
    posibleMoveList = rootState.posibleMoveListTeam(player)
    # Tạo model và đọc vào weight đã train
    model = initModel()
    model.load_weights(CHECKPOINT_FILE)
    # Đổi input của move thành input của model
    x = xMove_to_xModel(player, board)
    x = np.array(x)
    x = np.expand_dims(x, axis = 0)
    # Nhập input vào model
    y = model.predict(x)
    y = y.tolist()
    y = y[0]
    # Đổi output của model thành output của hàm move
    ansMoveTuple = yModel_to_yMove(y, posibleMoveList)
    # xuất move được chọn ra
    return ansMoveTuple