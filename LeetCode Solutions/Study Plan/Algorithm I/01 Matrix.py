class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] != 0:
                    if i > 0:
                        top = mat[i-1][j]
                    else:
                        top = float('inf')
                    if j > 0:
                        right = mat[i][j-1]
                    else:
                        right = float('inf')
                    mat[i][j] = min(top, right) + 1
        for i in range(rows - 1, -1, -1):
            for j in range(columns-1,-1,-1):
                if mat[i][j] != 0:
                    if j < columns - 1:
                        left = mat[i][j+1]
                    else:
                        left = float('inf')
                    if i < rows - 1:
                        down = mat[i+1][j]
                    else:
                        down = float('inf')
                    mat[i][j] = min(mat[i][j], min(left, down) + 1)
        return mat