class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        return sum(sum(x[0:3]) == x[3] for x in combinations(nums, 4))