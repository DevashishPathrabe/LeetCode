class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if(len(nums) < 1):
            return []
        arr = []
        result = []
        for num in nums[::-1]:
            index = bisect.bisect_left(arr, num)
            result.append(index)
            arr.insert(index, num)
        return result[::-1]