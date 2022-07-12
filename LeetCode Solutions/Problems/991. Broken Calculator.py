class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        result = 0
        while(x < y):
            result += 1
            if(y % 2):
                y += 1
            else:
                y //= 2
        return result + x - y