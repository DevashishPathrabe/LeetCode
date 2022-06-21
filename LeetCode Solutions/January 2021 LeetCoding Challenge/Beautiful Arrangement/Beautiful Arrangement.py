class Solution:
    def countArrangement(self, n: int) -> int:
        self.beautifulArrangements = 0
        def dfs(i, y):
            if (i <= 1):
                self.beautifulArrangements += 1
                return
            for j, x in enumerate(y):
                if (i%x == 0 or x%i == 0):
                    dfs(i-1, y[:j] + y[j+1:])
        dfs(n, list(range(1, n+1)))
        return self.beautifulArrangements