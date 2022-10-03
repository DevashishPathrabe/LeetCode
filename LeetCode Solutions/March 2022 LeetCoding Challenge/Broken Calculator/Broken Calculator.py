class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        result = 0
        while(startValue < target):
            result += 1
            if(target % 2):
                target += 1
            else:
                target //= 2
        return result + startValue - target