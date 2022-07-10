class Solution:
    def checkValidString(self, s: str) -> bool:
        l, w = 0, 0
        for i in s:
            if i == '(':
                l += 1
            elif i == ')':
                l -= 1
                if l < 0:
                    if l + w  < 0:
                        return False
                    w -= 1
                    l = 0
            else:
                w += 1
        r, w = 0, 0
        for i in s[::-1]:
            if i == ')':
                r += 1
            elif i == '(':
                r -= 1
                if r < 0:
                    if r + w < 0:
                        return False
                    w -= 1
                    r = 0
            else:
                w += 1
        return True