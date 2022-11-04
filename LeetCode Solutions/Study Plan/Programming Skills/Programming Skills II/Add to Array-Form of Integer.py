class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ""
        for i in num:
            s += str(i)
        result = int(s) + k
        return  list("".join(str(result)))