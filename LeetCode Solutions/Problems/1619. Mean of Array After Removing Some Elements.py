class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        trim = n // 20
        return sum(sorted(arr)[trim:n-trim]) / (n - 2*trim)