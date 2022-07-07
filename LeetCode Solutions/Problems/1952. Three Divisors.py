class Solution:
    def isThree(self, n: int) -> bool:
        sqrt = math.sqrt(n)
        if sqrt % 1 == 0 and n > 1:
            for i in range(2, int(sqrt)):
                if n % i == 0:
                    return False
            return True
        return False