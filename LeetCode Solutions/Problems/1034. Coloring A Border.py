class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def dfs(r, c, current, border, seen):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != current or (r, c) in seen:
                return
            seen.add((r, c))
            if (r == 0 or c == 0 or r == len(grid)-1 or c == len(grid[0])-1 or grid[r-1][c] != current or grid[r+1][c] != current or grid[r][c-1] != current or grid[r][c+1] != current):
                border.add((r, c))
            dfs(r-1, c, current, border, seen)
            dfs(r+1, c, current, border, seen)
            dfs(r, c-1, current, border, seen)
            dfs(r, c+1, current, border, seen)
            return
        if not grid:
            return grid
        current = grid[row][col]
        border = set()
        seen = set()
        dfs(row, col, current, border, seen)
        for element in border:
            grid[element[0]][element[1]] = color
        return grid