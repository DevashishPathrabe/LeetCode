class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix[0])
        m = len(matrix)
        minRow = []
        maxCol = []
        for i in range(m):
            minRow.append(min(matrix[i]))
        for j in range(n):
            x = 0
            for i in range(m):
                    if matrix[i][j] > x:
                        x = matrix[i][j]
            maxCol.append(x)
        for i in maxCol:
            if i in minRow:
                return [i]