class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        result = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                result += i + num//i
        return num == result