class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        v1, v2, v3, v4 = [], [], [], []
        n = len(arr1)
        for i in range(n):
            v1.append(i + arr1[i] + arr2[i])
            v2.append(i - arr1[i] - arr2[i])
            v3.append(i - arr1[i] + arr2[i])
            v4.append(i + arr1[i] - arr2[i])
        result = 0
        result = max(result, max(v1) - min(v1))
        result = max(result, max(v2) - min(v2))
        result = max(result, max(v3) - min(v3))
        result = max(result, max(v4) - min(v4))
        return result