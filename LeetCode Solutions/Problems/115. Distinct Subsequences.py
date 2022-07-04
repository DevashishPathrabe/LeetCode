class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def helper(s, t):
            A = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
            for j in range(len(s) + 1):
                A[0][j] = 1
            for i in range(1, len(t) + 1):
                for j in range(1, len(s) + 1):
                    A[i][j] = A[i][j - 1]
                    if t[i - 1] == s[j - 1]:
                        A[i][j] += A[i - 1][j - 1]
            return A[-1][-1]
        return helper(s, t)