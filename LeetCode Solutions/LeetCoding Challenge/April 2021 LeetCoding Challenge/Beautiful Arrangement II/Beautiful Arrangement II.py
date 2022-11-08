class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result, a, z = [0]*n, 1, k+1
        for i in range(k+1):
            if (i % 2):
                result[i] = z
                z -= 1
            else:
                result[i] = a
                a += 1
        for i in range(k+1, n):
            result[i] = i+1
        return result