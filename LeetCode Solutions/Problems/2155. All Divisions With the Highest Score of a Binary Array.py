class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        currentScore = sum(nums)
        currentMax = currentScore
        result = [0]
        for i in range(1, len(nums) + 1):
            currentScore += 1 - 2 * nums[i - 1]
            if currentScore > currentMax:
                currentMax = currentScore
                result = [i]
            elif currentScore == currentMax:
                result.append(i)
        return result