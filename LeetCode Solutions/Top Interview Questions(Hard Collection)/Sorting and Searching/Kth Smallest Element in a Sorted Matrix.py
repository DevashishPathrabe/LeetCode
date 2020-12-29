class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        var = sum(matrix, [])
        var.sort()
        return var[k-1]