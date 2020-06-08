class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        return self.__matrix()[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.__matrix()]

    def __matrix(self):
        str_lines = self.matrix_string.splitlines()
        return [[int(i) for i in row.split()] for row in str_lines]
