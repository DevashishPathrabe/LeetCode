class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        n = len(input)
        nums = set(input)
        entropy = 0.
        for num in nums:
            p_i = input.count(num)/n
            entropy -= p_i * math.log2(p_i)
        return entropy