class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result = 1
        previous = 1
        for i in nums:
            if i + previous < 1:
                result += 1 - (i + previous)
                previous = 1
            else:
                previous = i + previous
        return result