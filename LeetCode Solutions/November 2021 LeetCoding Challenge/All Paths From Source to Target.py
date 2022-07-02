class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        def helper(p, visited, paths):
            visited.append(p)
            if p == N-1:
                paths.append([item for item in visited])
            else:
                for nei in graph[p]:			
                    helper(nei, visited, paths)
            visited.pop()
        visited, paths = [], []
        helper(0, visited, paths)
        return paths