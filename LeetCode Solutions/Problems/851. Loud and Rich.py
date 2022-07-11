class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dict = defaultdict(list)
        for i in range(0, len(quiet)):
            dict[i] = []
        for i, j in richer:
            dict[j].append(i)
        print(dict)
        n = len(quiet)
        vis = [False]*n
        ans = [98765]*n
        def dfs(dict, quiet, ans, node, vis):
            vis[node] = True
            minimum = quiet[node]
            index = node
            ans[node] = index
            for i in dict[node]:
                if vis[i] == False:
                    dfs(dict, quiet, ans, i, vis)
                if quiet[ans[i]] < minimum:
                    minimum = quiet[ans[i]]
                    index = ans[i]
            ans[node] = index
        for i in range(0, n):
            if vis[i] == False:
                dfs(dict, quiet, ans, i, vis)
        return ans