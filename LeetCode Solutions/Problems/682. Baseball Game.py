class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for j in ops:
            if j == '+':
                result.append(result[-1] + result[-2])
            elif j == 'D':
                result.append(2*result[-1])
            elif j == 'C':
                result.remove(result[-1])
            else:
                result.append(int(j))
        return sum(result)