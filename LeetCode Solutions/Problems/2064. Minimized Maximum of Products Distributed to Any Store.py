class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high, result = 1, max(quantities), 0 
        while (low <= high):
            mid, numStore = ceil((low+high)/2), 0
            for i in quantities:
                numStore += ceil(i/mid)
                if numStore > n:
                    low = mid + 1
                    break
            if numStore <= n:
                result, high = mid, mid-1
        return result