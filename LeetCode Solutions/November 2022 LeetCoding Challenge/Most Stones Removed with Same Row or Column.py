class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            parent[p2] = p1
        n = len(stones)
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        par = set()
        for i in range(n):
            par.add(find(i))
        return n-len(par)