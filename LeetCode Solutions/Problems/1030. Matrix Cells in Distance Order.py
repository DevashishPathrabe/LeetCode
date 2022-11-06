class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        ans = [[r, c] for c in range(cols) for r in range(rows)]
        return sorted(ans, key = lambda ans: abs(ans[0] - rCenter) + abs(ans[1] - cCenter))