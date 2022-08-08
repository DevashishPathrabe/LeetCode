class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for i in S:
            if (i in J):
                result = result + 1
        return result