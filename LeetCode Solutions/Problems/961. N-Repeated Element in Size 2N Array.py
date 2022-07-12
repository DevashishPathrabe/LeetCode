class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if(i in d):
                n = i
                break
            else:
                d[i] = 1
        return i