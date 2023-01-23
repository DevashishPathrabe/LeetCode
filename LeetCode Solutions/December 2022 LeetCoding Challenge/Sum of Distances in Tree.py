class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count, ans = [1]*n, [0]*n
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        def dfs(curr, parent):
            for child in tree[curr]:
                if child != parent:
                    dfs(child, curr)
                    count[curr] += count[child]
                    ans[curr] += ans[child] + count[child]
        def dfs2(curr, parent):
            for child in tree[curr]:
                if child != parent:
                    ans[child] = ans[curr] + (n-count[child]) - count[child]
                    dfs2(child, curr)
        dfs(0, -1)
        dfs2(0, -1)
        return ans