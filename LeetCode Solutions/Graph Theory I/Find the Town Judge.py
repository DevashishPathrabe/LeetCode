class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * n
        outcoming = [0] * n
        for a, b in trust:
            outcoming[a - 1] += 1
            incoming[b - 1] += 1
        judges = []
        for i in range(n):
            if incoming[i] == n - 1 and outcoming[i] == 0:
                judges.append(i + 1)
        if len(judges) != 1:
            return -1
        return judges[0]