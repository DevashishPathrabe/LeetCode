class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        List = []
        for i in range(0, 100):
            x = 2**i
            List.append(x)
        if n in List:
            return True
        return False