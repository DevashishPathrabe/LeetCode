class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def recurse(i):
            if(i < 0):
                return False
            if(i > len(arr)-1):
                return False
            if(visited[i]):
                return False
            if(arr[i] == 0):
                return True
            visited[i] = True
            return recurse(i+arr[i]) or recurse(i-arr[i])
        visited = len(arr)*[False]
        return recurse(start)