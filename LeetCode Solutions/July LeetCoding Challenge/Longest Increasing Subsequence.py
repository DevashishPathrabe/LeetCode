class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for n in nums:
            idx = bisect.bisect_left(tails, n)
            tails[idx:idx+1] = [n]
        return len(tails)