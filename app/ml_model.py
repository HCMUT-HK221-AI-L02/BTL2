#--- Thiết kế model Machine Learning cho bài toán

# Import library
from tensorflow import keras

# Code
def initModel():
    model = keras.Sequential([
        keras.layers.Input(shape = (26)),
        keras.layers.Dense(32),                            # hidden layer
        keras.layers.Dense(112, activation = 'sigmoid')     # output layer
    ])
    return model