class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(number * number for number in nums)