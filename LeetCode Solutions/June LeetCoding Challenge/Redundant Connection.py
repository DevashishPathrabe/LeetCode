class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parentArray = [i for i in range(len(edges) + 1)]
        def find(x: int) -> int:
            if(x != parentArray[x]):
                parentArray[x] = find(parentArray[x])
            return parentArray[x]
        def union(x: int, y: int) -> None:
            parentArray[find(y)] = find(x)
        for a,b in edges:
            if(find(a) == find(b)):
                return [a,b]
            else:
                union(a,b)