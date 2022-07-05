class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        a = list(range(1, m+1))
        result = []
        for i in range(len(queries)):
            x = queries[i]
            y = a.index(x)
            result.append(y)
            z = a.pop(y)
            a.insert(0, z)
        return result