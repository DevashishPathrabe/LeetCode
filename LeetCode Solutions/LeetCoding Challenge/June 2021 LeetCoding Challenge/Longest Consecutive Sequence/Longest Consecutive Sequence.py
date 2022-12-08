class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longestConsecutive, c = 0, 0
        for i in nums:
            if (i-1 not in s):
                k = i
                while (k in s):
                    c += 1
                    k += 1
                longestConsecutive = max(c, longestConsecutive)
                c = 0
        return longestConsecutive