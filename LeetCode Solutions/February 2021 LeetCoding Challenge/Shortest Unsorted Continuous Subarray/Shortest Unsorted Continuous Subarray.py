class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lenNums, left, right = len(nums)-1, -1, -1
        maxNums, minNums = nums[0], nums[lenNums]
        for i in range(1, len(nums)):
            a, b = nums[i], nums[lenNums-i]
            if (a < maxNums):
                right = i
            else:
                maxNums = a
            if (b > minNums):
                left = i
            else:
                minNums = b
        return max(0, left + right - lenNums + 1)