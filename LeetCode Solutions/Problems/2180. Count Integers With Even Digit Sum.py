class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num+1):
            temp = []
            while i > 0:
                temp.append(i % 10)
                i //= 10
            if sum(temp) % 2 == 0:
                count += 1
        return count