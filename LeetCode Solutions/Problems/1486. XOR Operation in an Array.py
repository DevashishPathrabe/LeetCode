class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        current = start
        for i in range(1, n):
            current = current ^ (start + (i * 2))
        return current