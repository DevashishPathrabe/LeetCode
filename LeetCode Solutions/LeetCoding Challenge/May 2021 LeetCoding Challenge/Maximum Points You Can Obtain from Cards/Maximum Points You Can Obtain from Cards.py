class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maximumScore = total = sum(cardPoints[:k])
        for i in range(k-1, -1, -1):
            total += cardPoints[i+len(cardPoints)-k] - cardPoints[i]
            maximumScore = max(maximumScore, total)
        return maximumScore