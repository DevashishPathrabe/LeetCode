class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer, distance = [10001]*len(s), 10001
        for i in range(len(s)):
            if s[i] == c:
                distance = 0
            answer[i] = distance
            distance += 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                distance = 0
            answer[i] = min(answer[i], distance)
            distance += 1
        return answer