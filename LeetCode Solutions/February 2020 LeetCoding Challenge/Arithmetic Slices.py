class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        arithmeticSlices = combination = lastDifference = 0
        for i in range(len(A)-1):
            difference = A[i+1] - A[i]
            if(i!=0 and difference == lastDifference):
                combination += 1
                arithmeticSlices += combination
            else:
                combination = 0
            lastDifference = difference
        return arithmeticSlices