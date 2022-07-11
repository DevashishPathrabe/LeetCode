class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        path_cost = [inf]*(n+1)
        path_cost[k] = 0
        import collections
        g = collections.defaultdict(list)
        for u, v, w in times:
    	    g[u] += [(w, v)]
        q = [(k, 0)]
        while q:
    	    start, sw = q.pop()
    	    for dw, dest in g[start]:
    		    if sw + dw < path_cost[dest]:
    			    path_cost[dest] = sw + dw
    			    q += [(dest, path_cost[dest])]
        worst_case = max(path_cost[1:])
        if worst_case < inf:
    	    return worst_case
        return -1