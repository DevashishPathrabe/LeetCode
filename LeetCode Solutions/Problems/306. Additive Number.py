class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(num, numList):
            if not num:
                if len(numList) <= 2:
                    return
                result.append(numList)
                return
            for i in range(1, len(num)+1):
                if len(numList) > 1:
                    if numList[-1] + numList[-2] != int(num[:i]):
                        continue
                if len(num[:i]) > 1 and num[:i][0] == '0':
                	continue
                helper(num[i:], numList + [int(num[:i])])
        result = []
        helper(num, [])
        return len(result) != 0