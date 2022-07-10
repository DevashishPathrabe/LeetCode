class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] != 0:
                    if i > 0:
                        top = matrix[i-1][j]
                    else:
                        top = float('inf')
                    if j > 0:
                        right = matrix[i][j-1]
                    else:
                        right = float('inf')
                    matrix[i][j] = min(top, right) + 1
        for i in range(rows - 1, -1, -1):
            for j in range(columns-1,-1,-1):
                if matrix[i][j] != 0:
                    if j < columns - 1:
                        left = matrix[i][j+1]
                    else:
                        left = float('inf')
                    if i < rows - 1:
                        down = matrix[i+1][j]
                    else:
                        down = float('inf')
                    matrix[i][j] = min(matrix[i][j], min(left, down) + 1)
        return matrix