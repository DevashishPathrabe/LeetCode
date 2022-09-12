class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def helper(i, j, grid1, grid2):
            if i < 0 or j < 0 or i >= len(grid1) or j >= len(grid1[0]) or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            left = helper(i-1, j, grid1, grid2)
            right = helper(i+1, j, grid1, grid2)
            up = helper(i, j-1, grid1, grid2)
            down = helper(i, j+1, grid1, grid2)
            if grid1[i][j] == 0:
                return False
            else:
                return left and right and up and down
        result = 0
        m, n = len(grid1), len(grid1[0])
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if helper(i, j, grid1, grid2):
                        result += 1
        return result