class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        numbers1 = [0]*26
        numbers2 = [0]*26
        for i in s1:
            numbers1[ord(i) - ord('a')] += 1
        for index in range(0, len(s2)):
            numbers2[ord(s2[index]) - ord('a')] += 1
            if index >= len(s1) - 1:
                if numbers1 == numbers2:
                    return True
                numbers2[ord(s2[index - len(s1) + 1]) - ord('a')] -= 1
        return False