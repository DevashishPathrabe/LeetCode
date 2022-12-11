class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = [0] * len(nums)
        Sum[0] = nums[0]
        for i in range(1, len(nums)):
            Sum[i] = Sum[i-1] + nums[i]
        return Sum