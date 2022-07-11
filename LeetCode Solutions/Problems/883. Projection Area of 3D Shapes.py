class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        for i in grid:
            area += max(i) + len(i) - i.count(0)
        for j in zip(*grid):
            area += max(j)
        return area