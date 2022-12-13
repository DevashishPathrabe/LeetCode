class Solution:
    def pivotInteger(self, n: int) -> int:
        value = n*(n+1)//2
        if isqrt(value)**2 == value:
            return isqrt(value)
        else:
            return -1