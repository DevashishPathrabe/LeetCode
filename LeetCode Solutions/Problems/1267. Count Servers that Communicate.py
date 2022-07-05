class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        Sum = sum(sum(x) for x in grid)
        row_sum = [sum(i) for i in grid]
        col_sum = [*map(sum,zip(*grid))]
        for i, val in enumerate(row_sum):
            if val == 1:
                cl = grid[i].index(val)
                if col_sum[cl] == 1:
                    Sum -= 1
        return Sum