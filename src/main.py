from libs.io import Data
from keras.models import Sequential
from keras.layers import Dense
import sys

TRAIN_FILE = sys.argv[1]
WEIGHT_INIT = sys.argv[2]
ACTIVATION_FUNC = sys.argv[3]
HIDDEN_LAYER_NUMBER = int(sys.argv[4])
HIDDEN_LAYER_SIZE = int(sys.argv[5])
EPOCHS = int(sys.argv[6])
BATCH_SIZE = int(sys.argv[7])

def main():
    train_data = Data(TRAIN_FILE)
    
    model = Sequential()
    model.add(Dense(8, input_dim=8, activation=ACTIVATION_FUNC))
    for i in range(HIDDEN_LAYER_NUMBER):
        model.add(Dense(HIDDEN_LAYER_SIZE, activation=ACTIVATION_FUNC))
    model.add(Dense(1, activation=ACTIVATION_FUNC))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

if __name__ == '__main__':
    main()
