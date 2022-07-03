class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        def helper(initHealth):
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = initHealth + dungeon[0][0]
            for row in range(m):
                for column in range(n):
                    if row > 0 and dp[row-1][column] > 0:
                        dp[row][column] = max(dp[row][column], dp[row-1][column] + dungeon[row][column])
                    if column > 0 and dp[row][column-1] > 0:
                        dp[row][column] = max(dp[row][column], dp[row][column-1] + dungeon[row][column])
            return dp[m-1][n-1] > 0
        left = 1
        right = 1000 * (m + n) + 1
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            if helper(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result