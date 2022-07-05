class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        reverse_order = {'a':'cb', 'b':'ca', 'c':'ba'}
        if n == 1:
            return chr(96+k) if k<=3 else ''
        else:
            temp = self.getHappyString(n-1, (k+1)//2)
            return temp if not temp else temp+reverse_order[temp[-1]][k%2]