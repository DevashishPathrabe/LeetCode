class Solution:
    def isNumber(self, s: str) -> bool:
        num, exponent, sign, decimal = False, False, False, False
        for i in s:
            if(i >= '0' and i <= '9'):
                num = True
            elif(i == 'e' or i == 'E'):
                if(exponent or not num):
                    return False
                else:
                    exponent, num, sign, decimal = True, False, False, False
            elif(i == '+' or i == '-'):
                if(sign or num or decimal):
                    return False
                else:
                    sign = True
            elif(i == '.'):
                if(decimal or exponent):
                    return False
                else:
                    decimal = True
            else:
                return False
        return num