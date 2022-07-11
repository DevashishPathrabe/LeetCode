class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict = defaultdict(int)
        Sum, result = 0, 0
        dict[0] = 1
        for n in nums:
            Sum += n
            result += dict.get(Sum - goal, 0)
            dict[Sum] += 1
        return result