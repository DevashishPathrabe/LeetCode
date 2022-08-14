class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        minimum, maximum = min(bloomDay), max(bloomDay)
        while minimum < maximum:
            mid = minimum + (maximum - minimum)//2
            count, adj = 0, 0
            for days in bloomDay:
                if days > mid:
                    adj = 0
                else:
                    adj += 1
                    if adj == k:
                        count += 1
                        adj = 0
                if count >= m:
                    break
            if count < m:
                minimum = mid + 1
            else:
                maximum = mid
        return minimum