class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)