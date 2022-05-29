class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        array = []
        for i in sorted(intervals):
            if (len(array) == 0 or array[-1][1] < i[0]):
                array.append(i)
            else:
                array[-1][1] = max(array[-1][1], i[1])
        return array