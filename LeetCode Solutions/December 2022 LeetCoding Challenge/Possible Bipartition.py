class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        queue, visited = deque(),{}
        graph = defaultdict(set)
        for f, t in dislikes: 
            graph[f].add(t)
            graph[t].add(f)
        for i in range(1, n+1):
            if i not in visited:
                queue.append(i)
                visited[i] = 0 if i-1 in visited and visited[i-1] == 1 else 1 
            while queue:
                current = queue.popleft()
                for nbr in graph[current]:
                    if nbr not in visited:
                        queue.append(nbr)
                        visited[nbr] = 1 if visited[current] == 0 else 0
                    else:
                        if visited[nbr] == visited[current]:
                            return False
        return True