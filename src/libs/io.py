import numpy

class Data():
    def __init__(self, filename):
        self.details = numpy.loadtxt(filename, delimiter=';', dtype=numpy.str)
        self.X = self.details[:, 0:8].astype(numpy.float)
        self.Y = self.details[:,8]

    def get_element(self, row, col):
        return self.details[row][col]

    def get_line(self, row):
        return self.details[row]

    def get_details(self):
        return self.details

    def get_lenght(self):
        return len(self.details)
