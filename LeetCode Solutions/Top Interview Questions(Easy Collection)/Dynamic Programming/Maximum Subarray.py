class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        curr = nums[0]
        MaxSum = nums[0]
        for i in nums[1:]:
            if((curr+i > i) and (curr+i > curr)):
                curr += i
            else:
                MaxSum = max(MaxSum, curr)
                curr = max(curr+i, i)
        return max(MaxSum, curr)