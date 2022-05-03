class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations or not equations[0] or not values or not queries:
            return []
        N = len(queries)
        G = collections.defaultdict(list)
        for i,[A,B] in enumerate(equations):
            G[A].append((B, values[i]))
            G[B].append((A, 1/values[i]))        
        def bfs(start, end):
            if not start in G or not end: return -1.0
            visited = set()
            Q = deque([(start, 1)])
            while(Q):
                currNode, currProd = Q.popleft()
                if currNode == end:
                    return currProd
                visited.add(currNode)
                if not currNode in G: return -1.0
                for (nextNode, value) in G[currNode]:
                    if nextNode in visited: continue
                    Q.append((nextNode, currProd * value))
            return -1.0
        result = []        
        for [X,Y] in queries:
            result.append(bfs(X,Y))
        return result