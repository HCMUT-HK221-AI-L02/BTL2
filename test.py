from tensorflow import keras
import json
from app.ml_model import initModel
from app.legalmove import LEGALMOVE
from app.utils import xMove_to_xModel, yMove_to_yModel, list_to_tuple




model = initModel()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# ------ Lấy data huấn luyện
# --- Đọc file
fileName = 'traindata/data00.json'
file = open(fileName, 'r')
fileData = json.load(file)
trainData = fileData["train_details"]
# --- Dịch data trong file json thành data để train
x_train = []
y_train = []
for data in trainData:
    x = xMove_to_xModel(data["player"], data["board"])
    moveTuple = list_to_tuple(data["moveTuple"])
    y = yMove_to_yModel(moveTuple)
    x_train.append(x)
    y_train.append(y)

# ------ Kiểm tra chiều dữ liệu
print(len(x_train))
print(len(y_train))


# ------ Thực hiện huấn luyện
model.fit(x_train, y_train, epochs = 10)



# ------ Lưu lại weights
model.save_weights('weights/my_model_weights.h5')