class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maximum, x, y = arr[0], arr[0], 0
        for num in arr[1:]:
            x, y = max(x + num, num), max(y + num, x)
            maximum = max(y, maximum)
        return max(maximum, x)