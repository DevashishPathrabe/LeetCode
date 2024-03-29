class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n 
        ap = [None] * n
        for i in range(n):
            ap[i] = dict()
        for j in range(1, n):
            for i in range(0, j):
                diff = nums[j] - nums[i]
                ap[j][diff] = ap[i].get(diff, 1) + 1
        ans = 0
        for item in ap[1:]:
            vals = max(item.values())
            ans = max(ans, vals)
        return ans