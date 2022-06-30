class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        power, score = 0, 0
        for i in range(1, len(s)):
            if (s[i] == "("):
                power += 1
            elif (s[i-1] == "("):
                score += 1 << power
                power -= 1
            else:
                power -= 1
        return score