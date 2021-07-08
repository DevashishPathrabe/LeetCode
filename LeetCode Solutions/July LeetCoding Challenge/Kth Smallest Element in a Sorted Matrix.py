class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        def countLessOrEqual(x):
            count = 0
            column = n - 1
            for r in range(m):
                while column >= 0 and matrix[r][column] > x: column -= 1
                count += (column + 1)
            return count
        left, right = matrix[0][0], matrix[-1][-1]
        kthSmallestElement = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                kthSmallestElement = mid
                right = mid - 1
            else:
                left = mid + 1
        return kthSmallestElement