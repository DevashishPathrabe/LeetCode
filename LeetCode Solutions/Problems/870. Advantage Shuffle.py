class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        order = [i for i in range(len(nums2))]
        permutation = [0 for _ in range(len(nums1))]
        order.sort(key=lambda x: -nums2[x])
        nums1.sort()
        for ix in order:
            permutation[ix] = nums1.pop() if(nums1[-1] > nums2[ix]) else nums1.pop(0)
        return permutation