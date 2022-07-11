class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = Counter(ages)
        return sum(c[a] * (c[b] - int(a == b)) for a in c for b in c if not (b <= a * 0.5 + 7 or b > a))