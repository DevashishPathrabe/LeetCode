class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        low, high = 0, len(tokens)-1
        score, max_score = 0, 0
        while low <= high:
            if tokens[low] <= power:
                power -= tokens[low]
                score += 1
                max_score = max(score, max_score)
                low += 1
            elif score >= 1:
                power += tokens[high]
                score -= 1
                high -= 1
            else:
                break
        return max_score