class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    t = [i, j]
                    s.append(t)
        for i in range(len(s)):
            row, column = s[i][0], s[i][1]
            matrix[row] = [0]*len(matrix[row])
            for j in range(len(matrix)):
                matrix[j][column] = 0