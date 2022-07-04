class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neighbors = defaultdict(set)
        for a, b in paths:
            neighbors[a].add(b)
            neighbors[b].add(a)
        answer = [0] * n
        for i in range(1, n + 1):
            available = {1, 2, 3, 4}
            for neighbor in neighbors[i]:
                if answer[neighbor - 1] in available:
                    available.remove(answer[neighbor - 1])
            answer[i - 1] = available.pop()
        return answer