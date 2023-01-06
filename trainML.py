from tensorflow import keras
import json
import numpy as np
from app.ml_model import initModel
from app.legalmove import LEGALMOVE
from app.utils import xMove_to_xModel, yMove_to_yModel, list_to_tuple
TRAINDATAFILE = 'traindata/data00.json'
TRAIN_FROM_CHECKPOINT = False
CHECKPOINT_FILE = ''
CHECKPOINT_SAVE = 'weights/my_model_weights.h5'

# ------ Tạo model
model = initModel()
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ------ Nhập Checkpoint
if TRAIN_FROM_CHECKPOINT:
    model.load_weights(CHECKPOINT_FILE)


# ------ Lấy data huấn luyện
# --- Đọc file
fileName = TRAINDATAFILE
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
x_train = np.array(x_train)
y_train = np.array(y_train)


# ------ Thực hiện huấn luyện
model.fit(x_train, y_train, epochs = 10)


# ------ Lưu lại weights
model.save_weights(CHECKPOINT_SAVE)