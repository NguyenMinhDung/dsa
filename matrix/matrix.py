class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    # def __add__(self, other):
    #     if self.rows != other.rows or self.cols != other.cols:
    #         raise ValueError("Matrices must have the same dimensions")
    #     result = Matrix(self.rows, self.cols)
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.data[i][j] = self.data[i][j] + other.data[i][j]
    #     return result

    # def __sub__(self, other):
    #     if self.rows != other.rows or self.cols != other.cols:
    #         raise ValueError("Matrices must have the same dimensions")
    #     result = Matrix(self.rows, self.cols)
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.data[i][j] = self.data[i][j] - other.data[i][j]
    #     return result

    # def __mul__(self, other):
    #     if self.cols != other.rows:
    #         raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    #     result = Matrix(self.rows, other.cols)
    #     for i in range(self.rows):
    #         for j in range(other.cols):
    #             for k in range(self.cols):
    #                 result.data[i][j] += self.data[i][k] * other.data[k][j]
    #     return result

    # def __str__(self):
    #     return "\n".join([" ".join([str(cell) for cell in row]) for row in self.data])

    # def __repr__(self):
    #     return f"Matrix({self.rows}, {self.cols})"

    # def __eq__(self, other):
    #     return self.data == other.data

    # def __ne__(self, other):
    #     return not self == other

    # def __getitem__(self, index):
    #     return self.data[index]

    # def __setitem__(self, index, value):
    #     self.data[index] = value

    # def transpose(self):
    #     result = Matrix(self.cols, self.rows)
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.data[j][i] = self.data[i][j]
    #     return result

    # def copy(self):
    #     result = Matrix(self.rows, self.cols)
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.data[i][j] = self.data[i][j]

    def print(self):
        for row in self.data:
            print(" ".join([str(cell) for cell in row]))

maxtrix = Matrix(2, 2)
maxtrix.print()