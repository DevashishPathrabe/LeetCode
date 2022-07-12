class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        maximum = len(s)
        minimum = 0
        result = []
        for i in s:
            if i == 'I':
                result.append(minimum)
                minimum += 1
            else:
                result.append(maximum)
                maximum -= 1
        if s[-1] == 'I':
            result.append(minimum)
        else:
            result.append(maximum)
        return result