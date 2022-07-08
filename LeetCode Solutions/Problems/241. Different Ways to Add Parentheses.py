class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def helper(s):
            result = []
            for i in range(len(s)):
                if '+' not in s and '-' not in s and '*' not in s:
                    return [int(s)]
                if s[i] in ('+','-','*'):
                    L1 = helper(s[:i])
                    L2 = helper(s[i+1:])
                    if s[i] == '+':
                        for x in L1:
                            for y in L2:
                                result.append(x+y)
                    elif s[i] == '-':
                        for x in L1:
                            for y in L2:
                                result.append(x-y)
                    else:
                        for x in L1:
                            for y in L2:
                                result.append(x*y)
            return result
        return helper(expression)