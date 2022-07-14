class Solution:
    def romanToInt(self, s: str) -> int:
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        resInt = prev = d[s[-1]]
        for i in range(len(s)-2, -1, -1):
            cur = d[s[i]]
            if(cur < prev):
                resInt -= cur
            else:
                resInt += cur
            prev = cur
        return resInt