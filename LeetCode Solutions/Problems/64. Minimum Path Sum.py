class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if(i == 0 and j == 0):
                    continue
                elif(i == 0):
                    grid[i][j] += grid[i][j-1]
                elif(j == 0):
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]