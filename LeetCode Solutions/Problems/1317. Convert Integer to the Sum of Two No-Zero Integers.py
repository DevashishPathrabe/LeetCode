class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        left, right, List = 0, n, []
        while True:
            if str(left).count("0") == 0 and str(right).count("0") == 0:
                List.append(left)
                List.append(right)
                break
            left += 1
            right -= 1
        return List