class Solution:
    def removeDuplicates(self, s: str) -> str:
        finalString = []
        for i in s:
            if finalString and finalString[-1] == i:
                finalString.pop()
            else:
                finalString.append(i)
        return "".join(finalString)