from libs.io import Data
import sys

TRAIN_FILE = sys.argv[1]
WEIGHT_INIT = sys.argv[2]
ACTIVATION_FUNC = sys.argv[3]
HIDDEN_LAYER_NUMBER = int(sys.argv[4])
EPOCHS = int(sys.argv[5])
BATCH_SIZE = int(sys.argv[6])

def main():
    train_data = Data(TRAIN_FILE);

if __name__ == '__main__':
    main()
