class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        maxLength = 0
        Sum = 0
        d = {}
        for i in range(n):
            Sum = Sum + nums[i]
            if Sum == 0:
                maxLength = i + 1
            if Sum in d:
                maxLength = max(maxLength, i - d[Sum])
            if Sum not in d:
                d[Sum] = i
        return maxLength