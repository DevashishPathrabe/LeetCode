class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        c = Counter()
        for i in nums:
            if counts[i] == 0:
                continue
            elif c[i] > 0:
                c[i] -=1
                c[i+1] += 1
            elif (counts[i+1] > 0 and counts[i+2] > 0):
                counts[i+1] -= 1
                counts[i+2] -= 1
                c[i+3] += 1
            else:
                return False
            counts[i] -= 1
        return True