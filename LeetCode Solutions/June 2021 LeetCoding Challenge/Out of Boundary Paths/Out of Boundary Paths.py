class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if(maxMove == 0):
            return 0
        dpCurrent = [[0] * (n+2) for _ in range(m+2)]
        dpLast = [[0] * (n+2) for _ in range(m+2)]
        for i in range(1, m+1):
            dpCurrent[i][1] += 1
            dpCurrent[i][n] += 1
        for j in range(1, n+1):
            dpCurrent[1][j] += 1
            dpCurrent[m][j] += 1
        ans = dpCurrent[startRow+1][startColumn+1]
        for d in range(maxMove-1):
            dpCurrent, dpLast = dpLast, dpCurrent
            for i, j in product(range(1, m+1), range(1, n+1)):
                dpCurrent[i][j] = (dpLast[i-1][j] + dpLast[i+1][j] + dpLast[i][j-1] + dpLast[i][j+1]) % 1000000007
            ans = (ans + dpCurrent[startRow+1][startColumn+1]) % 1000000007
        return ans