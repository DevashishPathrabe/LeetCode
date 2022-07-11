class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        trans = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        maximumSum = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                maximumSum += abs(grid[i][j] - min(max(grid[i]), max(trans[j])))
        return maximumSum