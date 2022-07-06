class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        base = sum(bobValues)
        piles = [a + b for (a,b) in zip(aliceValues, bobValues)]
        piles = list(reversed(sorted(piles)))
        score = sum(piles[::2])
        if score > base:
            return 1
        if score < base:
            return -1
        if score == base:
            return 0