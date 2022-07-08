class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        a, b = startPos[0], startPos[1]
        c, d = homePos[0], homePos[1]
        result = 0
        while c > a:
            result += rowCosts[a + 1]
            a += 1
        while c < a:
            result += rowCosts[a - 1]
            a -= 1
        while d > b:
            result += colCosts[b + 1]
            b += 1
        while d < b:
            result += colCosts[b - 1]
            b -= 1
        return result