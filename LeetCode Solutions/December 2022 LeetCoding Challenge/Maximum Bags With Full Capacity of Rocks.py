class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        track, count = [], 0
        for i in range(len(rocks)):
            difference = capacity[i] - rocks[i]
            heappush(track, difference)
        for i in range(len(rocks)):
            additionalRocks -= heappop(track)
            if additionalRocks >= 0:
                count += 1  
        return count