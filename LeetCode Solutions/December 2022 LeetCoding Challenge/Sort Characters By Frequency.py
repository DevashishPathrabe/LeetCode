class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict(collections.Counter(s))
        d = dict(reversed(sorted(d.items(), key=lambda item: item[1])))
        result = ""
        for i, element in enumerate(d):
            result += element * d[element]
        return result