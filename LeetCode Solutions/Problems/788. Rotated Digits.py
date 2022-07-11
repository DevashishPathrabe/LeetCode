class Solution:
    def rotatedDigits(self, n: int) -> int:
        a = ['2','5','6','9']
        g = {}
        g['0'] = '0'
        g['1'] = '1'
        g['2'] = '5'
        g['3'] = '-1'
        g['4'] = '-1'
        g['5'] = '2'
        g['6'] = '9'
        g['7'] = '-1'
        g['8'] = '8'
        g['9'] = '6'
        numberOfGoodIntegers = 0
        for i in range(n + 1):
            l = list(str(i).strip())
            p = ""
            fl = 0
            for j in l:
                if g[j] == '-1':
                    fl = -1
                    break
                else:
                    p += g[j]
            if fl == 0 and p != str(i):
                numberOfGoodIntegers += 1         
        return numberOfGoodIntegers