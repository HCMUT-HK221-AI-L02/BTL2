#--- Thiết kế model Machine Learning cho bài toán

# Import library
from tensorflow import keras

# Code
def initModel():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(26)),         # input layer
        keras.layers.Dense(128),                        # hidden layer
        keras.layers.Dense(112, activation = 'relu')    # output layer
    ])
    return model