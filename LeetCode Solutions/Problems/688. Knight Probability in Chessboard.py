class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def boundry(x, y):
            return x >= 0 and y >= 0 and x < n and y < n
        d = {}
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        def knightProb(r, c, m):
            if m == 0:
                return 1
            if (r, c, m) in d:
                return d[(r, c, m)]
            if boundry(r, c):
                ans = 0
                for dx, dy in moves:
                    ans += knightProb(r + dx, c + dy, m - 1)
                ans = ans / 8
                d[(r, c, m)] = ans
                return ans
            else:
                return 0
        return knightProb(row, column, k + 1)