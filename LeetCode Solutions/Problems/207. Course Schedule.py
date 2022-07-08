class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for current, previous in prerequisites:
            graph[previous].append(current)
        visited = set()
        def find(nodes: List[int]) -> bool:
            for i, node in enumerate(nodes):
                if node == -1:
                    continue
                if node in visited:
                    return False
                visited.add(node)
                gn = graph[node]
                if not find(gn):
                    return False
                visited.remove(node)
                nodes[i] = -1
            return True
        for gn in graph:
            if not find(gn):
                return False
        return True