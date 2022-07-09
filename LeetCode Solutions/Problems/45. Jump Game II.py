class Solution:
    def jump(self, nums: List[int]) -> int:
        Nlen, current, next, ans, i = len(nums) - 1, -1, 0, 0, 0
        while next < Nlen:
            if i > current:
                ans += 1
                current = next
            next = max(next, nums[i] + i)
            i += 1
        return ans