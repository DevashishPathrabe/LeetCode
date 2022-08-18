class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        frequencies = list(count.values())
        frequencies.sort()
        result, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            result += 1
            removed += frequencies.pop()
        return result