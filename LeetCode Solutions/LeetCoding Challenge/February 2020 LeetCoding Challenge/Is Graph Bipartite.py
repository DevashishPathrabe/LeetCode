class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        def isNotBipartite(node, color):
            if(node not in colors):
                colors[node] = color
                for i in graph[node]:
                    if(isNotBipartite(i, color^1)):
                        return True
            elif(colors[node] != color):
                return True
            return False
        for node in range(len(graph)):
            if(node not in colors):
                if(isNotBipartite(node,0)):
                    return False
        return True