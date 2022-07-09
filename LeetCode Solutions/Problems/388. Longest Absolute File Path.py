class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths, stack, LongestAbsoluteFilePath = input.split('\n'), [], 0
        for path in paths:
            p = path.split('\t')
            depth, name = len(p) - 1, p[-1]
            l = len(name)
            while stack and stack[-1][1] >= depth:
                stack.pop()
            if not stack:
                stack.append((l, depth))
            else:
                stack.append((l+stack[-1][0], depth))
            if '.' in name:
                LongestAbsoluteFilePath = max(LongestAbsoluteFilePath, stack[-1][0] + stack[-1][1])
        return LongestAbsoluteFilePath