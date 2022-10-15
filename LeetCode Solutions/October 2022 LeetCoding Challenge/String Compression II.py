class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def compress(i, previous, previous_count, k):
            if i == len(s):
                return 0
            current = s[i]
            if current == previous:
                if previous_count == 1 or previous_count == 9 or previous_count == 99:
                    length = 1
                else:
                    length = 0
                return length + compress(i + 1, previous, previous_count + 1, k)
            keep = 1 + compress(i + 1, current, 1, k)
            if k - 1 >= 0:
                delete = compress(i + 1, previous, previous_count, k - 1)
            else:
                delete = float('inf')
            return min(keep, delete)
        return compress(0, None, None, k)