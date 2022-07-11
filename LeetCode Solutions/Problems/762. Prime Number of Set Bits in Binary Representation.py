class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        s = [2,3,5,7,11,13,17,19,23,29,31]
        for i in range(left, right+1):
            if bin(i).count('1') in s:
                count += 1
        return count