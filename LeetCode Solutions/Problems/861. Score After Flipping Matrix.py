class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n, maximumScore = len(grid), len(grid[0]), 0
        for c in range(n):
            col = sum(grid[r][c] == grid[r][0] for r in range(m))
            maximumScore += max(col, m-col) * 2 ** (n-1-c)
        return maximumScore