class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        maxHeap = []
        for i, s in enumerate(score):
            maxHeap.append([-s, i])
        heapq.heapify(maxHeap)
        result = [""] * len(score)
        place = 1
        while maxHeap:
            i = heapq.heappop(maxHeap)[-1]
            if place == 1:
                result[i] = "Gold Medal"
            elif place == 2:
                result[i] = "Silver Medal"
            elif place == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(place)
            place += 1
        return result