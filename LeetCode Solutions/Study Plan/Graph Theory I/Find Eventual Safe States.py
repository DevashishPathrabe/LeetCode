class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        D  = {}
        V  = set()
        def issafe(n):
            if n in D:
                return D[n]
            result = True
            V.add(n)
            for x in graph[n]:
                if x in V or not issafe(x):
                    result = False
                    break
            V.remove(n)
            D[n] = result
            return result
        return [n for n in range(len(graph)) if issafe(n)]