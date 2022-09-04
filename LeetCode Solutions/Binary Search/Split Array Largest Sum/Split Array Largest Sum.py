class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(Sum):
            currentSum, k = 0, 1
            for num in nums:
                if (currentSum + num > Sum):
                    currentSum = num
                    k += 1
                else:
                    currentSum += num
            return k
        left, right = max(nums), sum(nums)
        while (left <= right):
            middle = (left + right) // 2
            k = split(middle)
            if (k > m):
                left = middle + 1
            else:
                right = middle - 1
        return left