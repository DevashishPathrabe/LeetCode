class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ylength, xlength = len(matrix) + 1, len(matrix[0]) + 1
        self.arr = [[0] * xlength for _ in range(ylength)]
        for i in range(1, ylength):
            for j in range(1, xlength):
                self.arr[i][j] = matrix[i-1][j-1] + self.arr[i-1][j] + self.arr[i][j-1] - self.arr[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.arr[row2+1][col2+1] - self.arr[row2+1][col1] - self.arr[row1][col2+1] + self.arr[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)