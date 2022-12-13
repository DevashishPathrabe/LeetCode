class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [[-1,-1], [-1,0], [-1,1]]
        def isInBounds(i,j):
            return 0 <= i < m and 0 <= j < n
        def getMin(i,j):
            return min(matrix[i+x][j+y] for x,y in dirs if isInBounds(i+x,j+y))
        for i in range(1,m):
            for j in range(n):
                matrix[i][j] += getMin(i,j)
        return min(matrix[-1])