class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def helper(node,parent):
            result = 0
            for child in graph[node]:
                if child != parent:
                    result += helper(child, node)
            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return result + 2
            return result
        return helper(0, 0)