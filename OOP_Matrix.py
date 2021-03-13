# Matrix class and operation with matrix
from sys import stdin


class Matrix:
    """matrix class was created. following methods were added: matrix size, matrix add, matrix mul"""
    def __init__(self, inputs):
        self.inputs = [raw.copy() for raw in inputs]

    def __str__(self):
        st = ''
        for i in range(len(self.inputs)):
            for j in range(len(self.inputs[i])):
                if j != len(self.inputs[i]) - 1:
                    st += str(self.inputs[i][j]) + '\t'
                else:
                    st += str(self.inputs[i][j])
            if i != len(self.inputs) - 1:
                st += '\n'
        return st

    def size(self):
        return len(self.inputs), len(self.inputs[0])

    def __add__(self, other):
        string = ""
        for i in range(len(self.inputs)):
            for j in range(len(self.inputs)):
                if j != len(self.inputs) - 1:
                    string += str(self.inputs[i][j] + other.inputs[i][j]) \
                              + '\t'
                else:
                    string += str(self.inputs[i][j] + other.inputs[i][j])
            if i != len(self.inputs) - 1:
                string += '\n'
        return string

    def __mul__(self, other):
        string = ""
        for i in range(len(self.inputs)):
            for j in range(len(self.inputs)):
                if j != len(self.inputs) - 1:
                    string += str(self.inputs[i][j] * other) + '\t'
                else:
                    string += str(self.inputs[i][j] * other)
            if i != len(self.inputs) - 1:
                string += '\n'
        return string
    __rmul__ = __mul__


exec(stdin.read())
