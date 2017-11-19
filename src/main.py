from libs.io import Data
import sys

TRAIN_FILE = sys.argv[1]

def main():
    train_data = Data(TRAIN_FILE);

if __name__ == '__main__':
    main()
