class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(digit for digit in nums if nums.count(digit) == 1)