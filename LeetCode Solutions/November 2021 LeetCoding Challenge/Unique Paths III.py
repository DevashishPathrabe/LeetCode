class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        result = 0
        def dfs(grid, r, c, vertexSet):
            nonlocal result, moves
            vertexSet.remove((r, c))
            if grid[r][c] == 2:
                if len(vertexSet) == 0:
                    result += 1
                return
            for x, y in moves:
                x, y = r + x, c + y
                if (x, y) in vertexSet:
                    dfs(grid, x, y, vertexSet.copy())
        vertexSet = set()
        r1, r2 = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != -1:
                    if grid[r][c] == 1:
                        r1, c1 = r, c
                    vertexSet.add((r, c))
        dfs(grid, r1, c1, vertexSet)
        return result