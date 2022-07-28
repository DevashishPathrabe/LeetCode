class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set(range(n))
        for x, y in edges:
            if y in result:
                result.remove(y)
        return list(result)