class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        temp, longest, count = nums[0], 1, 1
        for i in range(1, len(nums)):
            if temp < nums[i]:
                count += 1
            else:
                count = 1
            temp = nums[i]
            if count > longest:
                longest = count
        return longest