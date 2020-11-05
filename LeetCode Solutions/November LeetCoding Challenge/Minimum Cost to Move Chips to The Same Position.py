class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddNumbers, evenNumbers = 0, 0
        for i in position:
            if(i%2 == 0):
                evenNumbers += 1
            else:
                oddNumbers += 1
        if(evenNumbers > oddNumbers):
            return oddNumbers
        return evenNumbers