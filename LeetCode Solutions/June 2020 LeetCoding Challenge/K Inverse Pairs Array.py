class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        prefix = [0] + [1] * (k+1)
        for i in range(2, n+1):
            p = [0]
            for j in range(k+1):
                p += p[-1] + (prefix[j+1] - prefix[max(0, j-i+1)]) % (10**9+7),
            prefix = p
        return prefix[-1] - prefix[-2]