class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        s = 1
        result = [s]
        for i in range(rowIndex):
            s = s * (rowIndex-i) // (i+1)
            result.append(s)
        return result