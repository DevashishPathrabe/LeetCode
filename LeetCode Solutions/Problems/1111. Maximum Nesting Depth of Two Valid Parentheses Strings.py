class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result, depth = [], 0
        for element in seq:
            if element == '(':
                depth += 1
            result.append(depth % 2)
            if element == ')':
                depth -= 1
        return result