class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        operation = list(perm)
        arr = [0] * n
        result = 0
        x = n//2
        while arr != operation:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[int(x + (i - 1) // 2)]
            perm = list(arr)
            result += 1
        return result