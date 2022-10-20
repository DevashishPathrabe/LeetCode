class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for i in s:
            result += i.lower()
        return result