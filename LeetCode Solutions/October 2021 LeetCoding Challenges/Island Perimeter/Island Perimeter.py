class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        perimeter = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 0:
                    continue
                perimeter += 4
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == row or nc < 0 or nc == column or grid[nr][nc] == 0:
                        continue
                    perimeter -= 1
        return perimeter