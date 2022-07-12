class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        prison_size = len(cells)
        if cells[0] == 1 or cells[-1] == 1:
            n = (n-1) % 14 + 1
        else:
            n = n % 14
        for d in range(n):
            cells = [0] + [1-cells[i-1]^cells[i+1] for i in range(1, prison_size-1)] + [0]
        return cells