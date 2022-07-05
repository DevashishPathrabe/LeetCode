class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        st = str(n) 
        productNum = 1
        sumNum = 0
        for i in st:
            productNum *= int(i)
            sumNum += int(i)
        return productNum - sumNum