class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        differences = [i for i in range(len(s1)) if s1[i] != s2[i]]
        return len(differences) == 2 and s1[differences[0]] == s2[differences[1]] and s1[differences[1]] == s2[differences[0]]