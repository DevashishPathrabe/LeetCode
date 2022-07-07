class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = []
        for key in set(nums1):
            if key in set(nums2) or key in set(nums3):
                result.append(key)
        for key in set(nums2):
            if key in set(nums3) and key not in result:
                result.append(key)
        return result