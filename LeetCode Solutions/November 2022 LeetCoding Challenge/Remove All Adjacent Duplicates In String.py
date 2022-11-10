class Solution:
    def removeDuplicates(self, s: str) -> str:
        finalString = []
        for c in s:
            if finalString and finalString[-1] == c:
                finalString.pop()
            else:
                finalString.append(c)
        return "".join(finalString)