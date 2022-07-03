class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0
        for n in nums:
            num = (num * 2 + n) % 5
            result.append(num == 0)
        return result