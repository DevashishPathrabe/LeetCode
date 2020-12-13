class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while(n!=1 and i<50):
            x=0
            while(n != 0):
                x += (n%10)**2
                n //= 10
                i += 1
            n=x
        return n==1