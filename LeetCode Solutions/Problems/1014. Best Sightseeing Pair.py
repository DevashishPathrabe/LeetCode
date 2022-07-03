class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        a, b = values[0], 0
        for i in range(1, len(values)):
            b, a = max(a + values[i] - i, b), max(values[i] + i, a)
        return b