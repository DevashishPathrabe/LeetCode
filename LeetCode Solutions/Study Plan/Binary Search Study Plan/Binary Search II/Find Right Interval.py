class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n
        start_dict = defaultdict(int)
        for i, [start, _] in enumerate(intervals):
            start_dict[start] = i
        max_val = max(start_dict.keys())
        for i, [_, end] in enumerate(intervals):
            while end <= max_val and end not in start_dict.keys():
                end += 1
            if end <= max_val:
                result[i] = start_dict[end]
        return result