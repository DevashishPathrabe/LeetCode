class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        final = []
        for i in s:
            if i == '(':
                stack.append(i)
            try:
                if i == ')':
                    stack.pop()
            except:
                final.append(i)
        return len(final) + len(stack)