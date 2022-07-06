class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        return len(set(sorted( arr, key=lambda x: (c[x], x), reverse=False)[k:]))