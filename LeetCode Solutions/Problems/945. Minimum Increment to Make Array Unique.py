class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        low = -math.inf
        for x in nums:
            low = max(low+1, x)
            result += low - x
        return result