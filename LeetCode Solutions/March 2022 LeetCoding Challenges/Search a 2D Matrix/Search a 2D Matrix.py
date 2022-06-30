class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = -1, len(matrix[0])
        for i in range(len(matrix)):
            if target <= matrix[i][column-1]:
                row = i
                break
        if row == -1:
            return False
        for j in range(len(matrix[0])):
            if matrix[row][j] == target:
                return True
        return False