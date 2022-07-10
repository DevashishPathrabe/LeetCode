class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        rows = [""] * numRows
        level, step = 0, -1
        for i in s:
            rows[level] += i
            if(level == 0 or level == numRows - 1):
                step *= -1
            level += step
        result = ""
        for i in rows:
            result += i
        return result