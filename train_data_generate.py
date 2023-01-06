# Import thư viện
from move_MCST import *
import json
# ----------------------------------------------------------------
# Tên file viết tiếp vào
FILENAME = 'traindata/data00.json'
# Tạo một thế cờ cụ thể, chọn người chơi thực hiện nước cờ
board = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, -1],
        [-1, 0, 0, 0, -1],
        [-1, -1, -1, -1, -1]]
player = -1
# ----------------------------------------------------------------
# Gọi hàm giải thế cờ
ansMoveTuple = move(None, board, player, 1000, 1000)
# Viết đoạn code append kết quả train vào trong train data
new_data = {
    "player": player,
    "board": board,
    "moveTuple": ansMoveTuple
}
with open(FILENAME,'r+') as file:
    # First we load existing data into a dict.
    file_data = json.load(file)
    # Join new_data with file_data inside emp_details
    file_data["train_details"].append(new_data)
    # Sets file's current position at offset.
    file.seek(0)
    # convert back to json.
    json.dump(file_data, file)