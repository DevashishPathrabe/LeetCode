class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        maxValue = max(instructions)
        nodes = [0]*(maxValue+1)
        def query(x):
            result = 0
            while(x > 0):
                result += nodes[x]
                x -= x&-x
            return result
        def update(x):
            while(x <= maxValue):
                nodes[x] += 1
                x += x&-x
        count = 0 
        for index, x in enumerate(instructions):
            left = query(x-1)
            right = index - query(x)
            count += min(right, left)
            update(x)
        return count%(10**9 + 7)