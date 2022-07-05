class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numCount = defaultdict(int)
        for num in arr:
            numCount[num] += 1
        luckyNumber = -1
        for num, count in numCount.items():
            if num == count:
                luckyNumber = max(num, luckyNumber)
        return luckyNumber