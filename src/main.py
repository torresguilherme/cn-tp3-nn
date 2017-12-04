from libs.io import Data
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model 
import matplotlib.pyplot as plt
import sys

TRAIN_FILE = sys.argv[1]
WEIGHT_INIT = sys.argv[2]
ACTIVATION_FUNC = sys.argv[3]
HIDDEN_LAYER_NUMBER = int(sys.argv[4])
HIDDEN_LAYER_SIZE = int(sys.argv[5])
EPOCHS = int(sys.argv[6])
BATCH_SIZE = int(sys.argv[7])

def main():
    train_data = Data(TRAIN_FILE, 0, 1000)
    test_data = Data(TRAIN_FILE, 1001, 1429)

    # inicializa o modelo
    model = Sequential()
    model.add(Dense(8, input_dim=8, activation=ACTIVATION_FUNC))
    for i in range(HIDDEN_LAYER_NUMBER-1):
        model.add(Dense(HIDDEN_LAYER_SIZE, activation=ACTIVATION_FUNC))
    model.add(Dense(7, activation=ACTIVATION_FUNC))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # treina o modelo
    history = model.fit(train_data.X, train_data.Y, validation_data=(test_data.X, test_data.Y), epochs=(EPOCHS * BATCH_SIZE), batch_size=BATCH_SIZE)

    print(history.history.keys())
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()


if __name__ == '__main__':
    main()
