class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentAltitude = 0
        highAltitude = 0
        for i in gain:
            currentAltitude += i           
            highAltitude = max(highAltitude, currentAltitude)
        return highAltitude