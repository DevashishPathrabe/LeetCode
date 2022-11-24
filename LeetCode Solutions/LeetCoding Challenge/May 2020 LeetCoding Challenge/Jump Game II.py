class Solution:
    def jump(self, nums: List[int]) -> int:
        numsLength, current, Next, result, i = len(nums) - 1, -1, 0, 0, 0
        while(Next < numsLength):
            if(i > current):
                result += 1
                current = Next
            Next = max(Next, nums[i] + i)
            i += 1
        return result