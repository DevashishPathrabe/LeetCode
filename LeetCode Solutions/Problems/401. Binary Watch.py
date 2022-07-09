class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        def toTime(num):
            h = num >> 6
            m = num & (~960)
            if h > 11 or m > 59:
                return None
            return '{}:{}'.format(h, format(m, '02'))
        def countBits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        i = 0
        while i < 1024:
            if countBits(i) == turnedOn:
                time = toTime(i)
                time and result.append(time)
            i += 1
        return result