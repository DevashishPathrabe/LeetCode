class Solution:
    def numberOfSteps(self, num: int) -> int:
        numberOfSteps = 0
        while(num):
            if(num%2 == 1):
                num -= 1
            else:
                num /= 2
            numberOfSteps += 1
        return numberOfSteps