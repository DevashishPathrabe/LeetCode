class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        maximum = 0
        minimum = 0
        for num in nums:
            maximum = max(maximum, num - minimum)
            minimum = min(minimum, num - maximum)
        return maximum