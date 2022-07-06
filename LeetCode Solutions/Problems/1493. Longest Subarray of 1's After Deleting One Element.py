class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(0) == 0:
            return n-1
        if nums.count(1) == 0:
            return 0
        nums.append(0)
        zeroes = [-1]
        ones = []
        longestNESubarray = 0 
        for i, num in enumerate(nums):
            if num == 0:
                if len(zeroes) == 1:
                    zeroes.append(i)
                else:
                    zeroes = [zeroes[1], i]
                one = zeroes[1] - zeroes[0] -1 
                if len(ones) <= 1:
                    ones.append(one)
                elif len(ones) == 2:
                    ones = [ones[1], one]
                if len(ones) == 2:
                    longestNESubarray = max(longestNESubarray, ones[1] + ones[0])
        return longestNESubarray