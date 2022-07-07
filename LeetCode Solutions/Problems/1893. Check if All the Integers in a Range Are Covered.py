class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        result = []
        for i in ranges:
            result.extend(range(i[0], i[-1] + 1))
        result = set(result)
        for i in range(left, right+1):
            if i not in result:
                return False
        return True