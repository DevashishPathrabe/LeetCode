class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(math.ceil(math.sqrt(1+8*target)/2 - 0.5))
        while (target%2 != n*( n + 1 )/2%2):
            n += 1
        return n