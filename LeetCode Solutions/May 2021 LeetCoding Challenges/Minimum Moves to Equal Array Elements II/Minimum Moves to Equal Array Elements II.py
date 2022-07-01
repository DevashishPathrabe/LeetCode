class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        minimumNumberOfMoves, median = 0, nums[len(nums) // 2]
        for num in nums:
            minimumNumberOfMoves += abs(median - num)
        return minimumNumberOfMoves