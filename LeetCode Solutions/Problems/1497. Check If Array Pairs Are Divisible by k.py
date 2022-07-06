class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = [0]*k 
        for i in arr: 
            d[i % k] += 1 
        for i in range(k):
            if i == 0:
                if d[i] % 2 != 0:
                    return 0
            elif d[i] != d[k-i]:
                return 0
        return 1