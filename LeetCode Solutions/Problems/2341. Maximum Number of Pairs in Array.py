class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        pairs = 0
        remaining = 0
        for key, value in c.items():
            if value % 2 == 0:
                count = value // 2
                pairs += count
            else:
                count = (value + 1) // 2
                pairs += count - 1
                remaining += 1
        return [pairs, remaining]