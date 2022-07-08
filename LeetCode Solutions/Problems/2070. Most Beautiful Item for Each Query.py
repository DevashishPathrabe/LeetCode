class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        dic = dict()
        result = []
        gmax = 0
        for p, b in items:
            gmax = max(b, gmax)
            dic[p] = gmax
        keys = sorted(dic.keys())
        for q in queries:
            ind = bisect.bisect_left(keys, q)
            if ind < len(keys) and keys[ind] == q:
                result.append(dic[q])
            elif ind == 0:
                result.append(0)
            else:
                result.append(dic[keys[ind-1]])
        return result