class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        result = 0
        while(X < Y):
            result += 1
            if(Y%2):
                Y += 1
            else:
                Y //= 2
        return result + X - Y