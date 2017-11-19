import csv

class Data():
    def __init__(self, filename):
        with open(filename, "r") as csvfile:
            csvinput = csv.reader(csvfile)
            self.details = list(csvinput)

    def get_element(self, row, col):
        return self.details[row][col]

    def get_line(self, row):
        return self.details[row]

    def get_details(self):
        return self.details

    def get_lenght(self):
        return len(self.details)
