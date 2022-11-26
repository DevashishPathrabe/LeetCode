class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = int(math.sqrt(c) + 1)
        for i in range(limit):
            target = c - i * i
            if int(math.sqrt(target)) == math.sqrt(target):
                return True
        return False