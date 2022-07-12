class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        numberOfColumns = 0
        for c in zip(*strs): 
            if(list(c) != sorted(c)): 
                numberOfColumns += 1
        return numberOfColumns