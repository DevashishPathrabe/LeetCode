class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        resultingNumber = sorted([int(i) for i in str(n)])
        for i in range(30):
            if(sorted([int(j) for j in str(1 << i)]) == resultingNumber):
                return True
        return False