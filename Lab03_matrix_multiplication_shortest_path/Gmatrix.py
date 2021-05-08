import math

infinity = math.inf

class GMatrix:
    """
    this class is used to store the matrices used for the graph
    """

    def __init__(self,n):
        self.n = n  # the number of vertices (also rows and col of matrix)
        self.path_m = [[0 for _ in range(self.n)] for _ in range(self.n)]   # matrix for paths
        self.matrix = [[infinity for _ in range(self.n)] for _ in range(self.n)]    # matrix for weigth/cost
        for i in range(self.n):
            self.matrix[i][i] = 0

    def __str__(self):
        s = ""
        for i in range(self.n):
            for j in range(self.n):
                s += str(self.matrix[i][j]) + " "
            s += "\n"
        s += "\n"
        for i in range(self.n):
            for j in range(self.n):
                s += str(self.path_m[i][j]) + " "
            s += "\n"
        return s

    def add_element(self, row, col, value):
        # asign value to a matrix element
        self.matrix[row][col] = value
        self.path_m[row][col] = row

    def raise_2(self):
        new_matrix = GMatrix(self.n)
        for i in range(self.n):
            # iterate through rows
            for j in range(self.n):
                # iterate through cols
                for k in range(self.n):
                    # we search for a shorter path using an extra edge
                    minimum = min(new_matrix.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])
                    if minimum < new_matrix.matrix[i][j]:
                        # we replace in the new matrix
                        new_matrix.matrix[i][j] = minimum
                        new_matrix.path_m[i][j] = k
        return new_matrix



def test_matrix():
    m = GMatrix(6)
    m.add_element(1,2,5)
    m.add_element(1,3,20)
    m.add_element(2,3,10)
    m.add_element(2,4,30)
    m.add_element(3,4,5)
    print(m)
    # print(str(m))
    m = m.raise_2()
    print(m)
    m = m.raise_2()
    print(m)


# test_matrix()