class Solution:
    def rob(self, nums: List[int]) -> int:
        previous, current = 0, 0
        for i in nums:
            current, previous = max(previous+i, current), current
        return current