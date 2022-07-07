class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        previous, minimumNumberOfRungs = 0, 0
        for r in rungs:
            minimumNumberOfRungs += (r-previous-1) // dist
            previous = r
        return minimumNumberOfRungs