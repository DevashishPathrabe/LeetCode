class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n >= k + maxPts - 1:
            return 1
        p = [0] * (n + 1)
        p[0] = 1
        prev = 0
        for i in range(1, k + 1):
            prev += p[i - 1]
            if (i - maxPts - 1) >= 0:
                prev -= p[i - 1 - maxPts]
            p[i] = prev * 1 / (maxPts * 1.0)
        result = p[k]
        for i in range(k + 1, n + 1):
            if i - 1 - maxPts >= 0:
                prev -= p[i - 1 - maxPts]
            p[i] = prev * 1 / (maxPts * 1.0)
            result += p[i]
        return result