class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        arr.sort()
        for x in arr:
            if count[x] == 0:
                continue
            if x < 0 and x % 2 != 0:
                return False
            y = x * 2 if x > 0 else x // 2
            if count[y] == 0:
                return False
            count[x] -= 1
            count[y] -= 1
        return True