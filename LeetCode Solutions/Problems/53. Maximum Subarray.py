class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        current = nums[0]
        MaxSum = nums[0]
        for i in nums[1:]:
            if((current+i > i) and (current+i > current)):
                current += i
            else:
                MaxSum = max(MaxSum, current)
                current = max(current+i, i)
        return max(MaxSum, current)