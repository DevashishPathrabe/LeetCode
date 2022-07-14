class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for str in strs:
            zeroes = str.count("0")
            ones = len(str) - zeroes
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    arr[i][j] = max(arr[i][j], arr[i-zeroes][j-ones] + 1)
        return arr[m][n]