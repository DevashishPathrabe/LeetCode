class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDifference = -1
        minNumber = nums[0]
        for i in range(len(nums)):
            maxDifference = max(maxDifference, nums[i] - minNumber)
            minNumber = min(minNumber, nums[i])
        if maxDifference != 0:
            return maxDifference
        else:
            return -1