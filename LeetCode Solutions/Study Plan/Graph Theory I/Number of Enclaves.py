class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 1:
                return 
            if grid[i][j] == 1:
                grid[i][j] = -1
            dfs(i-1, j, grid)
            dfs(i+1, j, grid)
            dfs(i, j-1, grid)
            dfs(i, j+1, grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0])-1:
                    if grid[i][j] == 1:
                        dfs(i, j, grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
        return count