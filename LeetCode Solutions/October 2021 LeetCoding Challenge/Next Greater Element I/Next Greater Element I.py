class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            length = len(result)
            k = nums2.index(i)
            for j in nums2[k:]:
                if j > i:
                    result.append(j)
                    break
            if len(result) == length:
                result.append(-1)
        return result