class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def helper(row, column):
            grid[row][column] = 0
            area = 1
            for y, x in ((row-1, column), (row+1, column), (row, column+1), (row, column-1)):
                if(0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == 1):
                    area += helper(y, x)
            return area
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if(grid[row][column] == 1):
                    maxArea = max(maxArea, helper(row, column))
        return maxArea