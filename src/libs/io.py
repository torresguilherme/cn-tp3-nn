import numpy
from keras.utils import to_categorical

class Data():
    def __init__(self, filename, start, end):
        self.details = numpy.loadtxt(filename, delimiter=';', dtype=numpy.str)
        self.X = self.details[start:end, 0:8].astype(numpy.float)
        self.Y = []
        for i in self.details[start:end,8]:
            if i == 'CYT':
                self.Y.append(0)
            elif i == 'NUC':
                self.Y.append(1)
            elif i == 'EXC':
                self.Y.append(2)
            elif i == 'MIT':
                self.Y.append(3)
            elif i == 'ME1':
                self.Y.append(4)
            elif i == 'ME2':
                self.Y.append(5)
            elif i == 'ME3':
                self.Y.append(6)
        self.Y = to_categorical(self.Y)
