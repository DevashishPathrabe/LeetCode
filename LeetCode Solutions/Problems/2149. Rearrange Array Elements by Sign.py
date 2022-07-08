class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        PositiveList = []
        NegativeList = []
        result = []
        for i in nums:
            if (i < 0):
                NegativeList.append(i)
            else:
                PositiveList.append(i)
        for i in range (len(nums) // 2):
            result.append(PositiveList[i])
            result.append(NegativeList[i])
        return (result)