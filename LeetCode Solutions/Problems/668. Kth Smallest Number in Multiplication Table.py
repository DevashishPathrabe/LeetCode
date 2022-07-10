class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            return sum(min(x//i, n) for i in range(1, m+1))
        left, right, mid, smallestNumber = 0, m*n, 0, 0
        while left <= right:
            mid = (left + right) >> 1
            if count(mid) < k:
                left = mid + 1
            else:
                right, smallestNumber = mid - 1, mid
        return smallestNumber