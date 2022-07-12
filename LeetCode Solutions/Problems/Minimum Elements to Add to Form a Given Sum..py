class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        difference = abs(sum(nums)-goal)
        div, mod = divmod(difference, limit)
        return div+1 if mod else div