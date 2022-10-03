class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arithmeticSlices = combination = lastDifference = 0
        for i in range(len(nums)-1):
            difference = nums[i+1] - nums[i]
            if (i != 0 and difference == lastDifference):
                combination += 1
                arithmeticSlices += combination
            else:
                combination = 0
            lastDifference = difference
        return arithmeticSlices