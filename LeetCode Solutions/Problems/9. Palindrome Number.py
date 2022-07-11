class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverseNumber = 0
        while x > 0:
            remainder = x % 10
            reverseNumber = (reverseNumber * 10) + remainder
            x = x // 10
        if temp == reverseNumber:
            return True
        else:
            return False