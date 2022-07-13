class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        def helper(s, n, o, c):
            if(n == 0 and o == c):
                parentheses.append(s)
                return None
            if(n >= 0):
                helper(s+"(", n-1, o+1, c)
                if(o > c):
                    helper(s+")", n, o, c+1)
            else:
                return None
        helper("", n, 0,0)
        return parentheses