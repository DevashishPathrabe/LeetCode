class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        result = ""
        for i in words:
            result += i
        s = set(result)
        for i in s:
            if result.count(i) % n == 0:
                pass
            else:
                return False
        return True