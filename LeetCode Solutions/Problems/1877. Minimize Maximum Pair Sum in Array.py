class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maximumPairSum = 0
        for i in range(n//2 + 1):
            maximumPairSum = max(maximumPairSum, nums[i]+nums[-i-1])
        return maximumPairSum