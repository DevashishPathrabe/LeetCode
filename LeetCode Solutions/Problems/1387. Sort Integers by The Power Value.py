class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        check = list(range(lo,hi+1))
        j = 0
        temp = []
        for i in check:
            val = check[j]
            count = 0
            while i != 1:
                if i % 2 == 0:
                    i //= 2
                    count += 1
                else:
                    i = i * 3 + 1
                    count += 1
            temp.append((count, val))
            j += 1
        temp.sort()
        return temp[k-1][1]