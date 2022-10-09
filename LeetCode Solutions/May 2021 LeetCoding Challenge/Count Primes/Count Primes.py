class Solution:
    def countPrimes(self, n: int) -> int:
        arr, count = [0] * n, 0
        for i in range(2, n):
            if (arr[i]):
                continue
            count += 1
            arr[i * i:n:i] = [1] * ((n-1) // i-i+1)
        return count