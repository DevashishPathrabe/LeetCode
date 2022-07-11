class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        totalSurfaceArea, row, column = 0, len(grid), len(grid[0])      
        for i in range(row):
            for j in range(column):
                temp = grid[i][j]
                if(not temp):
                    continue
                totalSurfaceArea += 4 * temp + 2
                if(row-1-i):
                    totalSurfaceArea -= 2 * min(temp, grid[i+1][j])
                if(column-1-j):
                    totalSurfaceArea -= 2 * min(temp, grid[i][j+1])        
        return totalSurfaceArea