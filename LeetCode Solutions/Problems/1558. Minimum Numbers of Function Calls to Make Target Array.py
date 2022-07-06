class Solution:
    def minOperations(self, nums: List[int]) -> int:
        add = 0
        multiply = 0
        for i in nums:
            binary = bin(i)[2:]
            multiply = max(multiply, len(binary)-1)
            add += sum([int(x) for x in binary])
        return add + multiply