class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maximum = 1
        count = 0
        for i in range(len(flips)):
            if flips[i] > maximum:
                maximum = flips[i]
            if i+1 == maximum:
                count += 1
        return count