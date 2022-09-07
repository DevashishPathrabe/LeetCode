class Solution:
    def numSquares(self, n: int) -> int:
        if((n**0.5) == (int)(n**0.5)):
            return 1
        while(n&3 == 0):
            n >>= 2
        if(n&7 == 7):
            return 4
        for i in range(1, (int)(n**0.5)+1):
            if((n-i*i)**0.5 == (int)((n-i*i)**0.5)):
                return 2
        return 3