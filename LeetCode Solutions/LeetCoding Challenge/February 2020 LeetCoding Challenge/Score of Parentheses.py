class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        power, score = 0, 0
        for i in range(1, len(S)):
            if(S[i] == "("):
                power += 1
            elif(S[i-1] == "("):
                score += 1 << power
                power -= 1
            else:
                power -= 1
        return score