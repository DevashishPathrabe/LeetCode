class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        numberOfSteps = 0
        for i in range(1, len(s)):
            if int(s[-i]) + carry == 1:
                numberOfSteps += 2
                carry = 1
            elif int(s[-i]) + carry == 2:
                numberOfSteps += 1
                carry = 1
            else:
                numberOfSteps += 1
                carry = 0
        if s[0] == '1' and carry == 1:
            return numberOfSteps + 1
        return numberOfSteps