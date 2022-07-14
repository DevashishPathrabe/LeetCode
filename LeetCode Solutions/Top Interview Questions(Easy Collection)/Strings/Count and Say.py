class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return '1'
        prev = '1'
        res = ''
        count = 1
        for i in range(n-1):
            res = ''
            for j in range(len(prev)):
                if(j == len(prev)-1 or prev[j] != prev[j+1]):
                    res += str(count) + prev[j]
                    count = 1
                else:
                    count += 1
            prev = res
        return res