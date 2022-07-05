class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap = {}
        nums = []
        for i in sorted(arr):
            if i not in hashmap:
                hashmap[i] = len(hashmap) + 1
        for j in arr:
            nums.append(hashmap[j])
        return nums