class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums)
        count = defaultdict(lambda: 0)
        for n in nums:
            count[n] += 1
        for n in nums:
            if count[n] == 0:
                continue
            count[n] -= 1
            for j in range(1, k):
                if count[n+j] == 0:
                    return False
                count[n+j] -= 1
        return True