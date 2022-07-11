class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leading = []
        self.times = []
        count = defaultdict(int)
        ma = 0
        for i , p in enumerate(persons):
            count[p] += 1
            if count[p] >= ma:
                ma = count[p]
                self.leading.append(p)
                self.times.append(times[i])

    def search(self, arr , target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return l-1
    
    def q(self, t: int) -> int:
        index = self.search(self.times, t)
        return self.leading[index]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)