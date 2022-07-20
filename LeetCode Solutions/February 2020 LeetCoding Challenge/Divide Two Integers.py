class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend == -2147483648 and divisor == -1):
            return 2147483647
        quotient, sign = 0, 1
        if(dividend < 0):
            dividend, sign = -dividend, -sign
        if(divisor < 0):
            divisor, sign = -divisor, -sign
        if(dividend == divisor):
            return sign
        while(dividend >= divisor):
            d = 0
            while(divisor << d <= dividend):
                d += 1
            dividend -= divisor << d - 1
            quotient += 1 << d - 1
        if(sign < 0):
            return -quotient
        else:
            return quotient