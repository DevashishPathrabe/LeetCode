class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = [[] for i in range(len(s))]
        for i,j in enumerate(parent):
            if j >= 0:
                children[j].append(i)
        result = [0]
        def helper(i):
            candidates = [0]
            for j in children[i]:
                current = helper(j)
                if s[i] != s[j]:
                    candidates.append(current)
            candidates = nlargest(2, candidates)
            result[0] = max(result[0], sum(candidates) + 1)
            return max(candidates) + 1
        helper(0)
        return result[0]