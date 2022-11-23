class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        lenNums, i = len(nums), 1
        while(i < lenNums and nums[i] == nums[i-1]):
            i += 1
        if(i == lenNums):
            return 1
        up, length = nums[i-1] > nums[i], 1
        while(i < lenNums):
            if((up and nums[i] < nums[i-1]) or (not up and nums[i] > nums[i-1])):
                up = not up
                length += 1
            i += 1
        return length