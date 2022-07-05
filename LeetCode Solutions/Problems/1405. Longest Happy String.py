class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        total = a + b + c
        A = B = C = 0
        longestPossibleHappyString = ""
        while total > 0:
            if (a >= b and a >= c and A != 2) or (a > 0 and (B == 2 or C == 2)):
                longestPossibleHappyString += "a"
                A += 1
                B = C = 0
                a -= 1
            elif (b >= a and b >= c and B != 2) or (b > 0 and (A == 2 or C == 2)):
                longestPossibleHappyString += "b"
                B += 1
                A = C = 0
                b -= 1
            elif (c >= b and c >= a and C != 2) or (c > 0 and (B == 2 or A == 2)):
                longestPossibleHappyString += "c"
                C += 1
                A = B = 0
                c -= 1
            total -= 1
        return longestPossibleHappyString