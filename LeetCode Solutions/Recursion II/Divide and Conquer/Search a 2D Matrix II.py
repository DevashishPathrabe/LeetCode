class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0):
            return False
        r, c = len(matrix)-1, 0
        while(r >= 0 and c < len(matrix[0])):
            if(matrix[r][c] == target):
                return True
            else:
                if(matrix[r][c] < target):
                    c += 1
                else:
                    r -= 1
        return False