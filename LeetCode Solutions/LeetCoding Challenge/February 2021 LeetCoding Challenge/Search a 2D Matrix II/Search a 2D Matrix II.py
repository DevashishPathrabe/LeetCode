class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = 0, len(matrix[0]) - 1
        while (row < len(matrix) and column >= 0):
            if (matrix[row][column] > target):
                column -= 1
            elif (matrix[row][column] < target):
                row += 1
            else:
                return True
        return False