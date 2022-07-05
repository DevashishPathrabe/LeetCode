class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= sum(n % 2 for n in Counter(s).values())