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
        integer = previous = d[s[-1]]
        for i in range(len(s)-2, -1, -1):
            current = d[s[i]]
            if current < previous:
                integer -= current
            else:
                integer += current
            previous = current
        return integer