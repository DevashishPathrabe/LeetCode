class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currentTime = 60 * int(current[0:2]) + int(current[3:5])
        targetTime = 60 * int(correct[0:2]) + int(correct[3:5])
        difference = targetTime - currentTime
        count = 0
        for i in [60, 15, 5, 1]:
            count += difference // i
            difference %= i
        return count