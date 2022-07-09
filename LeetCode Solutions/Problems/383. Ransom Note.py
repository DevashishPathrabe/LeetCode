class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for i in magazine:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for i in ransomNote:
            if i in table and table[i] > 0:
                table[i] -= 1
            else:
                return False
        return True