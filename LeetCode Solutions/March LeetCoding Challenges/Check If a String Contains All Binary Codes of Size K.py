class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        count = 1 << k
        seen = set()
        for i in range(len(s)-k, -1, -1):
            num = s[i:i+k]
            if(num not in seen):
                seen.add(num)
                count -= 1
            if(not count):
                return True
            if(i < count):
                return False