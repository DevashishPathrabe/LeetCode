class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk, arr=[], []
        for i in s:
            if i != ')':
                stk.append(i)
            else:
                popelement = stk.pop()
                while popelement != '(':
                    arr.append(popelement)
                    popelement = stk.pop()
                for j in arr:
                    stk.append(j)
                arr = []
        ans = ''
        for k in stk:
            ans += k
        return ans